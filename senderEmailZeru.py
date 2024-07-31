import smtplib

print('Note : kamu mengirim dengan pengguna zeruprogram@gmail.com')
target_email = input('Masukan email target mu : ')

subjek = input('Masukan subjek : ')
pesan = input('Masukan Pesan email : ')
spam = input("Apakah kamu mau spam? (y/n) : ")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login("zeruprogram@gmail.com", "fiqi jqbb cfzn qtcp")

teks = f"Subject: {subjek}\n\n{pesan}"

if spam == "y" or spam == "":
    lengthSpam = int(input("berapa kali kamu ingin spam email? : "))
    for x in range(lengthSpam):
        server.sendmail("zeruprogram@gmail.com", target_email, teks)
        print('berhasil mengirim email ke ', x)
else:
    server.sendmail("zeruprogram@gmail.com", target_email, teks)
    print('berhasil mengirim email!')
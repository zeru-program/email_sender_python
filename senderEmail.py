import smtplib

email = input('Masukan email mu : ')
target_email = input('Masukan email target mu : ')

subjek = input('Masukan subjek : ')
pesan = input('Masukan Pesan email : ')

teks = f"Subject: {subjek}\n\n{pesan}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, "fiqi jqbb cfzn qtcp")

server.sendmail(email, target_email, teks)

print('berhasil mengirim email!')
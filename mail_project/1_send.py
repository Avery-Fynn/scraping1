import smtplib
from email.message import EmailMessage
from account import *
from random import *

nicknames = ["A", "B", "C", "D", "E"]

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for nickname in nicknames:
        msg = EmailMessage()
        msg["Subject"] = "파이썬 특강 신청합니다."
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = "mzj733@gmail.com"

        content = nickname + "/" + str(randint(1000, 9999))
        # content = "/".join([nickname, str(randint(1000, 9999))])
        msg.set_content(content)
        smtp.send_message(msg)
        print(nickname + "님이 메일 발송 완료")

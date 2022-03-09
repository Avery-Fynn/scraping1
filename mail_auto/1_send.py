import smtplib
from account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()  # 연결 되는지 확인
    smtp.starttls()  # 모든 내용이 암호화되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = "test mail"  # 메일 제목
    body = "mail body"  # 메일 본문

    # 발신자 수신자 정해진 형식의 메세지
    msg = f"Subject: {subject}\n{body}"
    smtp.sendmail(EMAIL_ADDRESS, "mzj733@gmail.com", msg)

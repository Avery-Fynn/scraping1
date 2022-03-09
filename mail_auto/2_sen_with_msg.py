import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다"  # 제목
msg["From"] = EMAIL_ADDRESS  # 보내는 사람
msg["To"] = "mzj733@gmail.com"

# 여러명에게 보낼 때
# msg["To"] = "mzj733@gmail.com, ㅇㅇ@gmail.com"
# or 변수 만들어서 넣기
# to_list = ["","","","",~]
# msg["To"] = ", ".join(to_list)

# 참조
msg["Cc"] = "~@gmail.com", ""

# 비밀참조
msg["Bcc"] = "~@gmail.com", ""


# 본문 적기
msg.set_content("테스트 본문입니다.")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

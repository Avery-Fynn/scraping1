import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다"  # 제목
msg["From"] = EMAIL_ADDRESS  # 보내는 사람
msg["To"] = "mzj733@gmail.com"
msg.set_content("다운로드 하세요")

# 첨부 파일
# msg.add_attachment()

# MIME TYPE png
with open("daum.png", "rb") as f:
    msg.add_attachment(f.read(), maintype="image",
                       subtype="png", filename=f.name)

# PDF
with open("test.pdf", "rb") as f:
    msg.add_attachment(f.read(), maintype="application",
                       subtype="pdf", filename=f.name)

# 엑셀
with open("엑셀.xlsx", "rb") as f:
    msg.add_attachment(f.read(), maintype=" application",
                       sbutype="octet-stream", filename=f.name)


with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

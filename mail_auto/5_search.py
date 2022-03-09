from account import *
from imap_tools import MailBox

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    for msg in mailbox.fetch(limit=5, reverse=True):  # 전체 메일 다 가져오기
        print("[{}] {}".format(msg.from_, msg.sbuject))

    # 읽지 않은 메일 가져오기
    for msg in mailbox.fetch('(UNSEEN)', limit=5, reverse=True):  # 전체 메일 다 가져오기
        print("[{}] {}".format(msg.from_, msg.sbuject))

    # 특정 인이 보낸 메일 가져오기
    for msg in mailbox.fetch('(FROM mzj733@gamil.com)', limit=5, reverse=True):  # 전체 메일 다 가져오기
        print("[{}] {}".format(msg.from_, msg.sbuject))

    # 어떤 글자를 포함하는 메일 가져오기
    for msg in mailbox.fetch('(TEXT "test mail")', limit=5, reverse=True):  # 전체 메일 다 가져오기
        print("[{}] {}".format(msg.from_, msg.sbuject))

    # 어떤 글자가 한글인 경우
    for msg in mailbox.fetch(limit=5, reverse=True):  # 전체 메일 다 가져오기
        if "테스트" in msg.subject:
            print("[{}] {}".format(msg.from_, msg.sbuject))

    # 특정 날짜에 온 메일
    for msg in mailbox.fetch('(ON 07-Nov-2020)', limit=5, reverse=True):  # 전체 메일 다 가져오기
        print("[{}] {}".format(msg.from_, msg.sbuject))

    # 2가지 이상의 조건을 모두 충족하는 메일
    for msg in mailbox.fetch('(ON 07-Nov-2020 SUBJECT "test mail")', limit=5, reverse=True):  # 전체 메일 다 가져오기
        print("[{}] {}".format(msg.from_, msg.sbuject))

    # 2가지 이상의 조건 중 하나라도 충족하는 메일
    for msg in mailbox.fetch('(OR ON 07-Nov-2020 SUBJECT "test mail")', limit=5, reverse=True):  # 전체 메일 다 가져오기
        print("[{}] {}".format(msg.from_, msg.sbuject))


# import time
# print(time.strftime('%d-%a-%Y))

# import datetime
# dt = datetime.datetime.strptime("2020-12-30", "%Y-%m-%d")

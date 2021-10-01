import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailMan:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"

    def send_mail(self, subject: str, recipients: list, message: str):
        mail = MIMEMultipart()
        mail['From'] = self.login
        mail['To'] = ', '.join(recipients)
        mail['Subject'] = subject
        mail.attach(MIMEText(message))
        send_connect = smtplib.SMTP(self.GMAIL_SMTP, 587)
        send_connect.ehlo()
        send_connect.starttls()
        send_connect.ehlo()
        send_connect.login(self.login, self.password)
        send_connect.sendmail(self.login, send_connect, mail.as_string())
        send_connect.quit()

    def receive_mail(self, folder='inbox', header=None):
        receiver_conn = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        receiver_conn.login(self.login, self.password)
        receiver_conn.list()
        receiver_conn.select(folder)
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = receiver_conn.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = receiver_conn.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        receiver_conn.logout()
        return email_message


if __name__ == '__main__':
    email = EmailMan('login@gmail.com', 'qwerty')
    email.send_mail('Subject', ['vasya@email.com', 'petya@email.com'], 'Message')
    print(email.receive_mail())





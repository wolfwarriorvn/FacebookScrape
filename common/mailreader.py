from imapclient import IMAPClient
from email import message_from_bytes
from bs4 import BeautifulSoup
import mailparser

IMAP_SERVER = "imap-mail.outlook.com"
IMAP_PORT = 993
class MailReader:
    def __init__(self, user, password) -> None:
        self.server = IMAPClient(IMAP_SERVER)
        self.server.login(user, password)
    
    def read_all(self):
        self.server.select_folder('INBOX')
        messages = self.server.search(['UNSEEN', ])  # in your case: ['FROM', 'email@outlook.example']

        # for each unseen email in the inbox
        for uid, message_data in self.server.fetch(messages, 'RFC822').items():
            pass
    
    def get_email(self):
        msg_body = []
        self.server.select_folder('INBOX')
        messages = self.server.search(['UNSEEN', ])  # in your case: ['FROM', 'email@outlook.example']

        # for each unseen email in the inbox
        for uid, message_data in self.server.fetch(messages, 'RFC822').items():
            # print(uid, message_data)
            # email_message = mailparser.parse_from_string(message_data[b'RFC822'])
            email_message = mailparser.parse_from_bytes(message_data[b'RFC822'])
            soup = BeautifulSoup(email_message.body, "html.parser")
            msg_body.append(soup.get_text())
        
        return msg_body


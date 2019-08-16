from twilio.rest import Client
from imapclient import IMAPClient
import os

def main():
    server = IMAPClient('imap.gmail.com', use_uid=True)
    GMAIL_PASS = os.environ['GMAIL_PASS']
    server.login('cscarlossamaniego@gmail.com', GMAIL_PASS)

    select_info = server.select_folder('INBOX')
    #print('%d messages in INBOX' % select_info[b'EXISTS'])

    messages = server.search(['FROM', 'samaca16@wfu.edu'])
    print("%d messages from our my school account" % len(messages))

    for msgid, data in server.fetch(messages, ['ENVELOPE']).items():
        envelope = data[b'ENVELOPE']
        print('"%s"' % (envelope.subject.decode()))

    #sendText()

def sendText():
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    myTwilioNumber = os.environ['MY_TWILIO_NUMBER']
    myCellPhone = os.environ['MY_CELL_PHONE_NUMBER']

    message = client.messages.create(body="testing env", from_=myTwilioNumber, to=myCellPhone)  
    print(message.sid)

if __name__ == '__main__':
    main() 
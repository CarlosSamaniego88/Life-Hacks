from twilio.rest import Client
from imapclient import IMAPClient
import os

def main():
    checkEmail()

def checkEmail():
    condition = 0
    while condition = 0:
        server = IMAPClient('imap.gmail.com', use_uid=True)                                     #connect to IMAP server
        GMAIL_PASS = os.environ['GMAIL_PASS']                                                   #insert gmail password, may need to make an app account
        server.login('cscarlossamaniego@gmail.com', GMAIL_PASS)                                 #log in

        select_info = server.select_folder('INBOX')                                             #Select folder you want to search in
        topic_to_search = 'testing'                                                             #INPUT WHAT YOU WANT TO SEARCH FOR!
        unseen_messages_subject = server.search(['(UNSEEN)', 'SUBJECT', topic_to_search])       #Searching unread emails with topic to search in subject or body
        unseen_messages_body = server.search(['(UNSEEN)', 'TEXT', topic_to_search])
        
        if unseen_messages_subject:                                                             #send text if topic to search is in body/subject of unread email
            print("unread message about: '{0}'".format(topic_to_search))
            sendText(topic_to_search)
        elif unseen_messages_body:
            print("unread message about: '{0}'".format(topic_to_search))
            sendText(topic_to_search)

def sendText(topic_to_search):                                                      
    account_sid = os.environ['TWILIO_ACCOUNT_SID']                                          #created Twilio account with Accound SID and token
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)                                                #create connection

    myTwilioNumber = os.environ['MY_TWILIO_NUMBER']                                         #input twilio number
    myCellPhone = os.environ['MY_CELL_PHONE_NUMBER']                                        #input ur phone number

    #sends message
    message = client.messages.create(body="Email about '{0}'".format(topic_to_search), from_=myTwilioNumber, to=myCellPhone)  
    print(message.sid)

if __name__ == '__main__':
    main() 
import email
import imaplib 
import string
import os
import re

def get_payment_info():
 

    email_message = []

    from_email_address = 'sultancse12@gmail.com' #here I have to set email address
    coming_subject = 'Forwarded message from mizan cse bl' # here I have to subject of the email address
    username = 'microcir13@gmail.com'
    password = 'test@1234'
    mail = imaplib.IMAP4_SSL("imap.gmail.com") 
    mail.login(username, password)
    mail.select("inbox")
    result, data = mail.uid('search', None, "ALL") 
    inbox_item_list = data[0].split()


    for item in inbox_item_list:
        result2, email_data = mail.uid('fetch', item, '(RFC822)')
        raw_email = email_data[0][1].decode("utf-8")
        email_message.append(email.message_from_string(raw_email))
    message_len = len(email_message)
    bkash_payment_info = []
    for i in range(message_len):
        if email_message[i]['From'] == from_email_address and email_message[i]['subject'] == coming_subject:
            for part in email_message[i].walk():
                if part.get_content_maintype() == "multipart":
                    continue
            bytes_type_content = part.get_payload(decode=True)
            string_type_content =  bytes_type_content.decode('utf-8')
            x = [float(s) for s in re.findall(r'-?\d+\.?\d*', string_type_content)]
            bkash_payment_info.append({'amount':x[0],
                                        'number':x[1],
                                        'reference':x[2] })
    mail.logout()
    print(bkash_payment_info)
    return bkash_payment_info
import email
import imaplib
from hugchat import hugchat
import requests
import json

url = "http://127.0.0.1:8000/api/put"

chatbot = hugchat.ChatBot(cookie_path="cookies.json")
id = chatbot.new_conversation()
chatbot.change_conversation(id)


imap_address = "imap.gmail.com"

email_address = "y1820915@gmail.com"
password = "iavguqbgdbyzbbxc"

imap = imaplib.IMAP4_SSL(imap_address)

imap.login(email_address,password)

imap.select("Inbox")

_, msgnums = imap.search(None,"All")

emails = []

for msgnum in msgnums[0].split(): 
    _, data = imap.fetch(msgnum,"(RFC822)")
    message = email.message_from_bytes(data[0][1])
    user_input = f'If you were given this line {message.get("Subject")} as an email subject in which category will you put it in professional or personal no need to explain just give the answer in one of these two words only'
    mail_info ={
        "message_no": msgnum.decode("utf-8"),
        "sender": message.get('From'),
        "reciever": message.get('To'),
        "date":  message.get('Date'),
        "subject": str(message.get('Subject')),
        "category": chatbot.chat(user_input) 
    } 
    for part in message.walk():
        if part.get_content_type() == "text/plain":
            mail_info['content'] = part.as_string()
    # json_data = json.dumps(mail_info)
    # headers = {'Content-Type': 'application/json'}

    # response = requests.post(url,data = json_data,headers= headers) 

    # if response.status_code == 200:
    #     print("Data added successfully.")
    # else:
    #     print("Error:", response.status_code)


    emails.append(mail_info)               


print(emails)
imap.close()   
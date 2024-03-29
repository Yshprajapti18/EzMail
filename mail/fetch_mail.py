import json
from tag_classifier import tagClassify
import requests



with open('data.json','r') as read_file:
    data = json.load(read_file)

for email in data:
    tag = tagClassify(email['subject'])
    email['tag'] = tag
    print(email['subject']+" : "+email['tag'])
    mail_json = json.dumps(email)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url='http://localhost:8000/inbox/send/',data=mail_json,headers=headers)
    print(response)
    
    # print(mail_json)
    






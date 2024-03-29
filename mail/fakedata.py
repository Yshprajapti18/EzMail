from faker import Faker
import random
import json
from datetime import datetime
import requests

fake = Faker()

def generate_fake_email():
    email_data = {
        "sender": fake.email(),
        "recipients": fake.email(),
        "subject": fake.sentence(),
        "body": fake.paragraph(),
    }
    return email_data



# Generate fake email data
fake_emails = generate_fake_email()



fake_emails_json = json.dumps(fake_emails)
headers = {'Content-Type': 'application/json'}

response = requests.post(url='http://localhost:8000/inbox/send/',data=fake_emails_json,headers=headers)

with open('data.json','w') as file:
    json.dump(fake_emails_json,file)



print(response)

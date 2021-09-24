# import os
from os import environ


import environ
from twilio.rest import Client

def create_twilio_client():
    # account_sid = os.environ['TWILIO_ACCOUNT_SID']
    # auth_token = os.environ['TWILIO_AUTH_TOKEN']
    env = environ.Env()
    environ.Env.read_env()
    account_sid = env('TWILIO_ACCOUNT_SID')
    auth_token = env('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    print(account_sid)
    print(auth_token)
    return client

def send_twilio_message(client):
    print("TWILIO ###############")
    message = client.messages \
                    .create(
                        body="Test message.",
                        from_='+16084733994',
                        to='+15624570545'
                    )

    print(message.sid)
import environ
from twilio.rest import Client

env = environ.Env()
environ.Env.read_env()

def create_twilio_client():
    account_sid = env('TWILIO_ACCOUNT_SID')
    auth_token = env('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    return client





def send_twilio_sms(client, to_number, content):
    print("##### Send TWILIO SMS #####")
    from_number = env('TWILIO_SMS_FROM_NUMBER')
    message = client.messages \
                    .create(
                        body=content,
                        from_=from_number,
                        to=to_number
                    )
    
    return
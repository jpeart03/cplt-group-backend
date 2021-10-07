import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_sendgrid_email(to_email, content):
    print("##### Send SENDGRID Email #####")
    from_email = os.environ.get('SENDGRID_FROM_EMAIL')

    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject='You have a new appreciation note!',
        html_content=content)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
    except Exception as e:
        print(e)

    return
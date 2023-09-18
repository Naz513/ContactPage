import json
import boto3 # AWS SDK for Python. Helps in sending email using SES

def lambda_handler(event, context):
    # Create an SES client
    ses = boto3.client('ses')

    # Define email parameters
    sender = "your_verified_email@example.com"
    recipient = "your_verified_email@example.com"
    subject = "New message from your contact page"

    # Extracting the message from the eent (data sent to the lambda)
    body = event['message']

    # Sending the email
    response = ses.send_email(
        Source=sender,
        Destination={
            'ToAddresses': [
                recipient,
            ],
        },
        Message={
            'Subject': {
                'Data': body,
            },
            'Body':{
                'Text': {
                    'Data': body,
                },
            },
        }
    )

    # Returning a response to inform the caller
    return {
        'statusCode': 200,
        'body': json.dumps('Email sent!')
    }
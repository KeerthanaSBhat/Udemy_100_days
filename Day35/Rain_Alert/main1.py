from twilio.rest import Client

account_sid = 'SID'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)
for i in range(10):
    message = client.messages.create(
        body=''
        ,
        from_='your_sample_no',
        to='your_no'
    )

    print(message.sid)
    print(message.status)

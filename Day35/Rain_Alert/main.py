import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "your_apikey"
account_sid = "your_SID"
auth_token = "your_auth_token"
weather_params = {
    "lat": 12.977661,
    "lon": 75.313709,
    "appid": api_key,
    "cnt": 4
}
response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
weather_data = response.json()
will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 803:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="""

       It's raining today""",
        from_='your_phone_no',
        to='your_friends_phone_no'
    )

    print(message.status)

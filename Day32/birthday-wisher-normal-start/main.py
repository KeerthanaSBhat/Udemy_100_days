##################### Normal Starting Project ######################
import random
from datetime import datetime
import pandas
import smtplib
MY_EMAIL = "bhatkeerthanas007@gmail.com"
MY_PASSWORD = "ilja kzsg tiwc rxrp"
today = datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthdays_person["name"])
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthdays_person["email"],
                            msg=f"Subject: Happy birthday!!!\n\n{contents}")





##################### Normal Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "appbreweryinfo@gmail.com"
MY_PASSWORD = "abcd1234()"

today_tuple = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("Day032/birthday-wisher-normal-start/birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthay_person = birthdays_dict[today_tuple]
    file_path = f"Day032/birthday-wisher-normal-start/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthay_person["name"])
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=birthay_person["email"], 
            msg=f"Subject: Happy Birthday!\n\n{contents}")

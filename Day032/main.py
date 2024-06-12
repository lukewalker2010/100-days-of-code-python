import smtplib
import datetime as dt
import random

MY_EMAIL = "appbreweryinfo@gmail.com"
MY_PASSWORD = "abcd1234()"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("Day032\quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smpt.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=MY_EMAIL, 
            msg=f"Subject: Monday Motivation\n\n{quote}")






# import smtplib

# my_email = "appbreweryinfo@gmail.com"
# password = "vexnarxlphojwuzh"


# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user="appbreweryinfo@gmail.com", password=password)
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs="appbrewerytesting@yahoo.com", 
#                         msg="Subject:hello\n\nThis is the body of the email")

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=5)
# print(date_of_birth)
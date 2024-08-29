import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://appbrewery.github.io/instant_pot/"
url_live = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=header)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]

price_as_float = float(price_without_currency)
print(price_as_float)

#Send allert
SMTP_ADDRESS="smtp.gmail.com"
EMAIL_ADDRESS="your_email@email.com"
EMAIL_PASSWORD="your app password"

# Get the product title
title = soup.find(id="productTitle").get_text().strip()
print(title)

# Set the price below which you would like to get a notification
BUY_PRICE = 70

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    # ====================== Send the email ===========================

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
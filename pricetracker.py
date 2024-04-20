import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = input("Enter Amazon URL: ")
offer_price = float(input("Enter Wanted Price: "))
user_email = input("Enter your email:) 

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "DNT": "1", 
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
}

    def send_mail(url):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('email@gmail.com', 'password')

        subject = 'Price Fell Down'
        body = f"Check the amazon link: {url}"

        msg = f"Subject: {subject}\n\n{body}"
        
        server.sendmail(
            'sender@gmail.com',
            'receiver@gmail.com', 
            msg
        )
        print('Email has been sent')
        server.quit()
            
for i in range(24):
    check_price()
    time.sleep(3600)

        

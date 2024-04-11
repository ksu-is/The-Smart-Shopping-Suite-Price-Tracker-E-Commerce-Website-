#import the necessary libraries 

import requests
from bs4 import BeautifulSoup
import time
import smtplib
from ipywidgets import interact, widgets

class AmazonPriceTracker:
    def(self, target_price, sender_email, sender_password, receiver_email):
        self.url = url
        self.target_price = target_price
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.receiver_email = receiver_email

#define the URL and create user agent info

URL = 'https://www.amazon.com/dp/B08PZHYWJS/ref=fs_a_mdt2_us3'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = float(price[0:3])

if(converted_price < 545): 
    send_mail()
    
print(converted_price)
print(title.strip())

if(converted_price > 545):
    send_mail()
def send_mail():
    server = smtplib.STMP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('dejaboney1025@gmail.com',' lovecupcakes1')

    subject = 'Price has dropped!'
    body = 'Check the amazon link below to see the price drop!'https://www.amazon.com/dp/B08PZHYWJS/ref=fs_a_mdt2_us3'
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
    'dejaboney1025@gmail.com'
    msg
    )
    print('EMAIL HAS BEEN SENT')
    
    server.quit()

while(True): 
 check_price()
 time.sleep(60 * 60 )

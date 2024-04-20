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
        server.login('shopsmartsuite.com', 'Georgia2024')

        subject = 'Price Has Dropped!'
        body = f'Check the Amazon link below to see your deal: {URL}
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail('shopsmartsuite0@gmail.com', user_email, msg)
        print('MESSAGE HAS BEEN SENT')
        server.quit()
        
    def check_price(URL, Price):
        page = requests.get(URL, headers=headers) 
        soup = BeautifulSoup(page.content, 'htmlparser')
        
            
for i in range(24):
    check_price()
    time.sleep(3600)

        

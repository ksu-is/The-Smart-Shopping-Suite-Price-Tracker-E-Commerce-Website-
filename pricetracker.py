import requests
from bs4 import BeautifulSoup
import smtplib
import time

def check price():
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }
    url = 'https://www.amazon.in/Bose-SoundLink-Wireless-Around_Ear_Headphones/dp/B0117RGG8E/ref=sr_1_11?qid=1562395272&refinements=p_89%3ABose&s=electronics&sr=1-11'

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find(id="productTitle").get_text().strip()
        price = soup.find(id="priceblock_ourprice").get_text().replace(',', '').strip()
        converted price = float(price)
        print("Product:", title)
        print("Price:", converted_price)
        
        if converted price < 20000:
            send_mail(url)
    except Exception as e:
        print("Error:", e)

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
            'receiver@gmail.com,
            msg
        )
        print('Email has been sent')
        server.quit()
            
for i in range(24):
    check_price()
    time.sleep(3600)

        

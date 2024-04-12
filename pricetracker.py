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

    def get_product_info(self):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
        page = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(id="productTitle").get_text().strip
        price = soup.find(id="priceblock_ourprice").get_text()
        converted_price = float(price[1:].replace(',', ''))
        return title, converted_price

    def send_notification(self, title, price):
        subject = f'Price Dropped for {title}'
        body = f'The price has dropped to ${price}!\nCheck it out here: {self.url}'
        message = f'Subject: {subject}\n\n{body}'
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(self.sender_email, self.send_password)
            smtp.sendmail(self.sender_email, self.receiver_email, message)
        
    def track_price(self)
        while True:
            title, price = self.get_product_info()
            print(f"Current Price for '{title}': ${price}")
            if price <= self.target_price:
                print(f"Price dropped below ${self.target_price}! But now!")
                self.send_notification(title, price)
                break
            time.sleep(3600)
            
def start_price_tracker(url, target_price, sender_email, sender_password, receiver_email):
    tracker = AmazonPriceTracker(url, target_price, sender_email, sender_password, receiver email)
    tracker.track_price()

default_url = 'https://www.amazon.com/dp/B07V1SQ966/'

interact(start_price_tracker, 
         url=widgets.Text(value=default-url, placeholder='Enter Amazon Product URL'),
         target_price=widgets.FloatText(placeholder='Enter Target Price'),
         sender_email=widges.Text(placeholder='Enter Sender Email'),
         sender_password=widgets.Password(placeholder='Enter Sender Email Password'),
         receiver_email=widgets.Text(placeholder='Eneter Receiver Email'))

        

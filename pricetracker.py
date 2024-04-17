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

        

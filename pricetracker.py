import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = input("Enter Amazon URL: ")
offer_price = float(input("Enter Wanted Price: "))
user_email = input("Enter your email: ") 

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
        server.login('shopsmartsuite0@gmail.com', 'Georgia2024')

        shopsmartsuite_email = 'shopsmartsuite0@gmail.com'
        gmail_domain = 'gmail.com'
        
        subject = 'Price Has Dropped!'
        body = f'Check the Amazon link below to see your deal: {URL}
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(f'shopsmartsuite0@gmail.com', user_email, msg)
        print('MESSAGE HAS BEEN SENT')
        server.quit()
        
def check_price(URL, Price):
        page = requests.get(URL, headers=headers) 
        soup = BeautifulSoup(page.content, 'htmlparser')

        title_element = soup.find(id="taxInclusiveMessage")
        if title_element:
            title = title_element.get_text().strip()
        else:
            title = "Title Not Found"

        price_element = soup.find('span', class_='a-offscreen')
        if price_element:
            price = float(price_element.get_text().strip().replace('$', ''))
            print(title)
            print(price)

            if price <= Price:
                send_mail()
        
try:
        while True:
            check_price(URL, offer_price)
            time.sleep(60 * 60)
except KeyboardInterrupt:
        pass


  

        

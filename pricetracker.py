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

def send_mail(url, user_email):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('shopsmartsuite0@gmail.com', 'Georgia2024')

        
        subject = 'Price has dropped!'

        body = f'Check the Amazon link below to see your deal: {url}'
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail('shopsmartsuite0@gmail.com', user_email, msg)

        print('MESSAGE HAS BEEN SENT')
        server.quit()
        
def check_price(URL, Price):

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        title_element = soup.find(id="taxInclusiveMessage")
        if title_element:
            title = title_element.get_text().strip()
        else:
            title = "Title Not Found"

        reviews_count_element = soup.find("span", {"id": "acrCustomerReviewText"})
        if reviews_count_element:
              reviews_count_text = reviews_count_element.get_text().strip()
              reviews_count = int(reviews_count_text.split()[0].replace(',', ''))
        else:
              average_rating = 0.0

        rating_element = soup.find("span", {"class": "a-icon-alt"})
        if rating_element:
              rating_text = rating_element.get_text().strip()
              average_rating = float(rating_text.split()[0])
        else:
              average_rating = 0.0

        print(f"Product: {title}")
        print(f"Number of Reviews: {reviews_count}")
        print(f"Average Rating: {average_rating}")

        availability_element = soup.find(id="availability")
        if availability_element:
              availability = availability_element.get_text().strip()
        else:
              availability = "Availabilty Not Found"
        
        if "in stock" in availability.lower():
            price_element = soup.find('span', class_='a-offscreen')
            if price_element:
                price = float(price_element.get_text().strip().replace('$', '').replace(',',''))
                print(title)
                print(price)

                image_element = soup.find("img", {"id": "landingImage"})
                if image_element:
                      image_url = image_element["src"]
                      print(f"Product Image URL: {image_url}")
                
                else: 
                      print("image not found.")

                if price <= Price:
                    send_mail(URL)

            else: 
                print("Element Not Found")
    
        else:
            print("Product is out of stock or unavailable. ")

        if "temporarily out of stock" in availability.lower():
                pass
        elif "unavailable" in availability.lower():
                pass
        

def set_interval():
      try:
            interval = int(input("Enter the time interval in minutes for checking the price: "))
            return interval * 60
      except ValueError:
            print("Please enter a valid integer for the time interval. ")
            return set_interval()


try:
        interval_seconds = set_interval()
        while True:
            check_price(URL, offer_price)
            time.sleep(interval_seconds)
except KeyboardInterrupt:
        pass

  

        

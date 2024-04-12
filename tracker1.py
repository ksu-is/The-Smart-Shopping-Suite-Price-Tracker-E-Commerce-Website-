import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL = https://www.amazon.com/Amazon_Fire_HD_10/dp/B0BHZT5S12?ref_=Oct_DLandingS_D_38704265_0

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}

def check_price():
  page = requests.get(URL, headers=headers)

  soup = BeautifulSoup(page.content, 'html.parser')

  title = soup.find(id="productTitle").get_text()
  price = soupfind(id="priceblock_outprice").get_text()
  converted_price = float(price[0:5])

  if(converted_price < 1.700):
    send_mail()

  print(converted_price)
  print(title.strip())

  if(converted_price > 1.700):
    send_mail()

def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

server.login('

subject = 'Price fell down!'
body = 'Check out the amazon link https://www.amazon.com/Amazon_Fire_HD_10/dp/B0BHZT5S12?ref_=Oct_DLandingS_D_38704265_0

msg = f"Subject: {subject}\n\n{body}"

server.sendmail(


)
print('HEY EMAIL HAS BEEN SENT!')

server.quit()


while(True):
  check_price()
  time.sleep(60 * 60)





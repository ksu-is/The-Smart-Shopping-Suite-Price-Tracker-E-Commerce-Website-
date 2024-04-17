import pip 
import smtplib

URL = input("Enter Amazon URL: ")


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

offerprice = float(input("Enter Wanted Price: "))

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    server.login('shopsmartsuite0@gmail.com', 'Georgia2024')
user_email = input("Enter your email: ")


def check_price(URL,Price):
    page = pip.get(URL, headers=headers)

    soup1 = pip(page.content, "html5lib")

    soup2 = pip(soup1.prettify(), "html5lib")

    title = soup2.find(id="productTitle").get_text().strip()

    price = soup2.find('span', class_='a-offscreen').get_text().strip()
    priceWithoutSign = price.split("$")[1]
    floatprice = float(priceWithoutSign)
    if floatprice <= Price:
           print(title)
    print(floatprice)  
    
def send_mail(server):
    subject = 'Price has dropped!'
    body = 'Check the amazon link below to see your deal!', URL
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('shopsmartsuite0@gmail.com',user_email,msg)
    print('MESSAGE HAS BEEN SENT')
try:    
    while(True):    
        check_price(URL, offerprice)
        pip.sleep(15)
except KeyboardInterrupt:
    server.quit()





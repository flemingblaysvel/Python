from bs4 import BeautifulSoup as bs
import requests
link='https://www.flipkart.com/search?q=watches&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=recency_desc'
page=requests.get(link)
soup=bs(page.content,'html.parser')
names=soup.find_all('a',class_="_2mylT6 _3Ockxk")
products=[]
for i in range(0,len(names)):
    products.append(names[i].get_text())
print(products)
review=soup.find_all('div',class_="VGWI6T")
rate=[]
for i in range(0,len(review)):
    rate.append(review[i].get_text())
print(rate)
price=soup.find_all('div',class_="_1vC4OE")
p=[]
for i in range(0,len(price)):
    p.append(price[i].get_text())
print(p)


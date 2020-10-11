from bs4 import BeautifulSoup as bs
import requests
link='https://www.flipkart.com/search?q=apple+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=apple+mobiles%7CMobiles&requestId=6d28ee8b-a204-416b-88d5-536bddf3799c&as-searchtext=apple'
page=requests.get(link)
soup=bs(page.content,'html.parser')
names=soup.find_all('div',class_="_3wU53n")
products=[]
for i in range(0,len(names)):
    products.append(names[i].get_text())
print(products)
price=soup.find_all('div',class_="_1vC4OE _2rQ-NK")
rate=[]
for i in range(0,len(price)):
    rate.append(price[i].get_text())
print(rate)

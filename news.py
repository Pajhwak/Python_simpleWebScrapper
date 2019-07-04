#Demo Web Scrapping Project
#this script get the news from www.tolonews.com

import requests
from bs4 import BeautifulSoup

try:
    url_list=['https://www.tolonews.com/', 'https://www.voanews.com/','https://www.pajhwok.com/']
    count = 1
    for urls in url_list :
        response = requests.get(urls)
        print(count,'_',urls)
        count = count+1

    respo = response.status_code

    if respo == 200 :
        print('Connection Created! ')
except:

        print('Connection is Field! Check your connection. ')






soup = BeautifulSoup(response.content , 'html.parser')

links  = soup.find_all('a')

new = ' __NEWS__ '

for link in links :
     found = link.get_text()
     print(new,found)

else:
    print('Not Found')

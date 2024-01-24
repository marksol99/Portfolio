
#BROKEN BECAUSE OF TWITTER UPDATE


import re
from bs4 import BeautifulSoup
from selenium import webdriver
import random
from os import path
import time
from urllib.parse import urljoin

url = 'https://twitter.com/search?q=%23Winter'

'''
Jeg har chromedriver på samme nivå som denne filen, i mappehirearkiet.
Om dette ikke er tilfelle hos deg så må pathen til driveren skrives inn
som et argument i parantesene () på linje 20. dette skrives inn som
"executable_path=**PATH/TO/DRIVER**". Det enkleste er å ha den på samme nivå.
'''

driver = webdriver.Chrome()
driver.get(url)  

counter = 7
while counter > 0:
    time.sleep(2)
    temp_links = []
    bs = BeautifulSoup(driver.page_source, 'html.parser')
    links = bs.find_all('a', {'href': re.compile('^(/hashtag/).*$')})


    for link in links:
        temp_links.append(urljoin("https://twitter.com/", link.attrs['href']))

    rand_url = random.choice(temp_links)
    driver.get(rand_url)
    counter -=1

driver.quit()
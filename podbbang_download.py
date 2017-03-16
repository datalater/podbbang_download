
# coding: utf-8

# In[45]:

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from itertools import count
from time import sleep


# In[46]:

def get_list(pid):    
    for page in count(1):
        page_url = "http://www.podbbang.com/podbbangchnew/episode_list"
        params = {'id':pid, 'page':page}
        
        print('page : {}'.format(page))

        r = requests.get(page_url, params=params)
        r.encoding = "utf-8"
        html = r.text

        soup = BeautifulSoup(html, 'lxml')

        for li_tag in soup.select('li'):
            try:
                title = li_tag.find('dt')['title'].replace('"','-')
                link = urljoin(page_url, li_tag.find('a')['href'])
                print(title, link)
            except (TypeError, KeyError):
                print("END")
                return None
            else:
                # 인증요구? Referer헤더, User-Agent헤더
                
                print("download link : {}".format(link))

                '''
                headers = {'Referer': 'http://www.podbbang.com/ch/{pid}'.format(pid=pid)}
                mp3_bin = requests.get(link, headers=headers).content

                filename = '{}.mp3'.format(title)
                with open(filename, 'wb') as f:
                    f.write(mp3_bin)
                '''
            
        sleep(0.5)
        
        break # 1페이지만 하고 종료


# In[47]:

get_list(1749)




import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://meesig.com/items/64',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
lis = soup.select('#comments > ol > li')

#comments > ol > li:nth-child(5) > div > form > div.comment-author.vcard > a
#comments > ol > li:nth-child(5) > div > form > div.comment-content > p
#comments > ol > li:nth-child(5) > div > form > div.comment-author.vcard > a

for li in lis :
    title = li.select_one('div > form > div.comment-content')
    if title is not None:
        ##rank = tr.select_one('td.number').text.split()[0]
        review = tr.select_one('div > form > div.comment-content').text.strip()
        ##artist = tr.select_one('td.info > a.artist.ellipsis').text
        
        print(review)

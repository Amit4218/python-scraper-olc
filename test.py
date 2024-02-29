from bs4 import BeautifulSoup
import requests
import os



url = requests.get("https://overlandingcamping.com/listing/sankri-sanctuary-haven-your-gateway-to-himalayan-overlanding-and-camping-trek-start-point-for-rupin-pass-har-ki-doon-kedarkantha/", headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
})

soup = BeautifulSoup(url.text, "html.parser")


#to get all the description
description = soup.find_all('p')
description = soup.find('div', id= "listing-overview")


for p_tag in description:
    print(p_tag.get_text())


# to get author and link 

author_name = soup.find('div', class_='hosted-by-title').find('a').text.strip()
author_link = soup.find('div', class_='hosted-by-title').find('a')['href']

print("Author Name:", author_name)
print("Href Link:",author_link)
from bs4 import BeautifulSoup
import requests
import os

url = requests.get("https://overlandingcamping.com/listing/sankri-sanctuary-haven-your-gateway-to-himalayan-overlanding-and-camping-trek-start-point-for-rupin-pass-har-ki-doon-kedarkantha/", headers = {
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
})

soup = BeautifulSoup(url.text, "html.parser")

# Listing Title
title = soup.h1.get_text()

# Listing Images 
images = []

for link in soup.find_all('a', {'data-background-image': True}):
    images.append(link["data-background-image"])
        
# Listing Address
address = soup.find('a',class_='listing-address').get_text(strip=True)

# Listing Lat/Long 
latitude = soup.find('div', id='singleListingMap')['data-latitude']
longitude = soup.find('div', id='singleListingMap')['data-longitude']

#To get all description

description = soup.find_all('p')
description = soup.find_all('div', id="listing-overview")

for p_tag in description:
    print(p_tag.get_text())


#listing Author & link

author = soup.find("div", {"id": "widget_listing_owner-2"})

if author:
    author_link =author.find("a", href=True)
    author_name =author.find("a").text.strip() if author.find("a") else None

    if author_link and author_name:
        print(author_link["href"])
        print(author_name)




# Creating a File and saving the data in it

file = open("listing.txt", "w")
file.writelines([f"Address: {address}\n"])
file.writelines([f"Lat: {latitude}\n"])
file.writelines([f"Long: {longitude}\n"])
file.writelines([f"Description : {description}\n"])
file.writelines([f"Authr-name : {author_name}\n"])
file.writelines([f"Authr-link : {author_link}\n"])
file.close()

# storing images in a folder
folder_name = 'images'
os.makedirs(folder_name, exist_ok=True)

#download and save images
for image_url in images:
    image_content = requests.get(image_url).content
    image_name = f'image.jpg'
    with open(os.path.join(folder_name, image_name), 'wb') as f:
        f.write(image_content)
from bs4 import BeautifulSoup
import requests
import os

url = requests.get("https://overlandingcamping.com/listing/sankri-sanctuary-haven-your-gateway-to-himalayan-overlanding-and-camping-trek-start-point-for-rupin-pass-har-ki-doon-kedarkantha/", headers={
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
address = soup.find('a', class_='listing-address').get_text(strip=True)

# Listing Lat/Long
latitude = soup.find('div', id='singleListingMap')['data-latitude']
longitude = soup.find('div', id='singleListingMap')['data-longitude']

# Description
description = soup.find('div', id="listing-overview").get_text(strip=True)

# Author and link
author = soup.find("div", {"id": "widget_listing_owner-2"})
author_link = None
author_name = None
if author:
    author_link = author.find("a", href=True)
    author_name = author.find("a").text.strip() if author.find("a") else None

# Folder creation
folder_name = "overlandng"
txt_folder = os.path.join(folder_name, "Text-folder")
img_folder = os.path.join(folder_name, "images-folder")
os.makedirs(txt_folder, exist_ok=True)
os.makedirs(img_folder, exist_ok=True)

# Save text and image
file_name = "listing.txt"
file_path = os.path.join(txt_folder, file_name)

with open(file_path, "w") as file:
    file.write(f"Title: {title}\n")
    file.write(f"Address: {address}\n")
    file.write(f"Lat: {latitude}\n")
    file.write(f"Long: {longitude}\n")
    file.write(f"Description: {description}\n")
    if author_name and author_link:
        file.write(f"Author Name: {author_name}\n")
        file.write(f"Author Link: {author_link['href']}\n")

for index, image_url in enumerate(images):
    image_content = requests.get(image_url).content
    image_filename = os.path.join(img_folder, f'image_{index}.jpg')
    with open(image_filename, 'wb') as f:
        f.write(image_content)


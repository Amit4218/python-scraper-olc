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

# Get the image content
    image_content = requests.get(images).content
        
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


#creating a folder to save images and data
        
folder_name = "overlandng"
os.makedirs(folder_name , exist_ok=True)

txt_folder = os.path.join(folder_name, "Text-folder")
img_folder = os.path.join(folder_name, "images-folder")
os.makedirs(txt_folder , exist_ok=True)
os.makedirs(img_folder, exist_ok=True)

# Creating a File and saving data in text-folder

file_name = "listing.txt"

file_path = os.path.join(txt_folder, file_name)

# Open the file for writing
with open(file_path, "w") as file:

    file.write(f"Address: {address}\n")
    file.write(f"Lat: {latitude}\n")
    file.write(f"Long: {longitude}\n")
    file.write(f"Description : {description}\n")
    file.write(f"Authr-name : {author_name}\n")
    file.write(f"Authr-link : {author_link}\n")

 # Save the image to the folder
    
image_filename = os.path.join(img_folder, 'image.jpg')
with open(image_filename, 'wb') as f:
    f.write(image_content)
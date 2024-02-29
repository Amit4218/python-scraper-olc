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

#to get all the description
description = soup.find('div', {'id': 'listing-overview'})
description_text ="\n".join([p.get_text(strip=True) for p in description.find_all('p')])


#Author and link
    
author_name = soup.find('div', class_='hosted-by-title').find('a').text.strip()
author_link = soup.find('div', class_='hosted-by-title').find('a')['href']



#making folder

folder_name = "overlandng"
txt_folder = os.path.join(folder_name, "Text-folder")
img_folder = os.path.join(folder_name, "images-folder")
os.makedirs(txt_folder, exist_ok=True)
os.makedirs(img_folder, exist_ok=True)

#Save text and image

file_name = "listing.txt"
file_path = os.path.join(txt_folder, file_name)

with open(file_path, "w") as file:
    file.write(f"Title: {title}\n")
    file.write(f"Address: {address}\n")
    file.write(f"Lat: {latitude}\n")
    file.write(f"Long: {longitude}\n")
    file.write(f"Description: {description_text}\n")
    if author_name and author_link:
        file.write(f"Author Name: {author_name}\n")
        file.write(f"Author Link: {author_link}\n")

# downlopad and save images 

for i, url in enumerate(images):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(img_folder, f"image_{i+1}.jpg"), "wb") as f:
                f.write(response.content)
            print(f"Image {i+1} downloaded successfully")
        else:
            print(f"Failed to download image {i+1}: {response.status_code}")
    except Exception as e:
        print(f"Error downloading image {i+1}: {e}")

print("All images downloaded and saved successfully!")



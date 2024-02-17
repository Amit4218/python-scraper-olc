from bs4 import BeautifulSoup
import requests
import os



url = requests.get ("https://www.lonelyplanet.com/articles/getting-around-south-korea")

soup = BeautifulSoup(url.text, "html.parser")


img_tag = soup.find('img')

# Extract the src attribute
src_link = img_tag['src']


# Remove query parameters related to image compression
src_link = src_link.split('?')[0]

# Create a folder named 'images' if it doesn't exist
folder_name = 'images'
os.makedirs(folder_name, exist_ok=True)

# Get the image content
image_content = requests.get(src_link).content

# Save the image to the folder
with open(os.path.join(folder_name, 'image.jpg'), 'wb') as f:
    f.write(image_content)



from bs4 import BeautifulSoup
import requests

web_link = requests.get ("https://overlandingcamping.com/listing/riverside-bliss-tranquil-camping-20-kms-from-rishikesh/", headers = {
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
})

soup = BeautifulSoup(web_link.text, "html.parser")


# for link in soup.find_all('a'):
#     print(link.get('href'))

# image_links = [img['src'] for img in soup.find_all('img')]


# for link in image_links:
#     print(link)



# print (soup.prettify())

title = soup.h1

images = soup.find_all(class_="mfp-gallery")

print(title)

# print(images)
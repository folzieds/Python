import requests
from PIL import Image
from io import BytesIO


req = requests.get("https://a-static.besthdwallpaper.com/naruto-shippuden-naruto-uzumaki-sasuke-uchiha-wallpaper-8119_L.jpg")
image = Image.open(BytesIO(req.content))

print(f"Status: {req.status_code}")
print(f"Image format: {image.size} {image.mode} {image.format}")

path = f"./images.{image.format}"

try:
    image.save(path,image.format)
except IOError:
    print("Image could not be downloaded!!!")
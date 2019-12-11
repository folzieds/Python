import requests

r = requests.get("https://moneytor.fcmb.com")
print(r.url)
print(r.text)
print(f"Status: {r.status_code}")

with open("./page.html","w+") as text:
    text.write(r.text)

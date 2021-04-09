import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
r = requests.get(url)
res = r.json()
print(res)

bitPrice = res['bpi']['USD']['rate']
threshold = bitPrice[:2]
threshold = int(threshold)
print(threshold)
print(type(threshold))
print("Latest Bitcoin price is :", bitPrice)

time = res['time']['updated']
date = time[:12]
print(date)

emergency_threshold = 10

if threshold <= emergency_threshold:
    print("It's an emergency")
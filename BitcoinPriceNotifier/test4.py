import requests

url = "https://api.nomics.com/v1/currencies/ticker?key=4279dd1d7b991cb52f8dede936c29d61"
r = requests.get(url)
res = r.json()
print(res[0]['price'])
print(res[1]['price'])
print(res[0]['price_date'])
print(res[0]['price_timestamp'])

# 2020-09-17T00:00:00Z
# 2020-09-17T03:59:00Z

date = res[0]['price_date']
date = date[:10]
print(date)
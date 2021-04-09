import requests

url = "https://api.nomics.com/v1/currencies/ticker?key=4279dd1d7b991cb52f8dede936c29d61"
r = requests.get(url)
res = r.json()
print(res[0]['price'])
print(res[0]['price_date'])
print(res[0]['price_timestamp'])

# date = res[0]['price_date']
# time = res[0]['price_timestamp']
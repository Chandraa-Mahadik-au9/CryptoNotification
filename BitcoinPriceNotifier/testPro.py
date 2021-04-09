import requests

url = "https://api.nomics.com/v1/currencies/ticker?key=4279dd1d7b991cb52f8dede936c29d61"

# url = "https://api.coindesk.com/v1/bpi/currentprice.json"
r = requests.get(url)
res = r.json()
print(res[1]['price'])


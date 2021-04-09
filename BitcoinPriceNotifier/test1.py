import requests

url = "https://community-bitcointy.p.rapidapi.com/convert/10/USD"

headers = {
    'x-rapidapi-host': "community-bitcointy.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
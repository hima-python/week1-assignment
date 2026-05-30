import requests

url = "https://catfact.ninja/fact"

response = requests.get(url)

data = response.json()

print("Cat Fact of the Day")
print("-------------------")
print(data["fact"])
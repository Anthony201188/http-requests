import requests

url = "http://www.lingoda.com/en/p/german-b1-intermediate/"

response = requests.get(url, stream=True)

print(response.status_code)
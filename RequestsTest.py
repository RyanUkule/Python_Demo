import requests

def post(url, param):
    headers = { 'Content-Type' : 'application/x-www-form-urlencoded'}
    
    response = requests.post(url, headers = headers, data = param)

    return response.json()

url = 'http://localhost:8080/api/setting/SubmitListing'
param = [
    [{'1. Q':'A'}],
    [{'2.1 Q':'A'}],
    [{'3.1 Q':'A'}]
]

response = post(url, param)

print('Result:', response)

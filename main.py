import requests

# API Specification: http://ip-api.com/docs/api:json
response = requests.get('http://ip-api.com/json')

print("This computer's IP Address is {0}".format(response.json()['query']))
print("The timezone of the request origin location is {0}".format(response.json()['timezone']))
print("The region of the request origin location is {0}".format(response.json()['regionName']))
print("The country of the request origin location is {0}".format(response.json()['country']))
print("The ISP used by the request origin location is {0}".format(response.json()['isp']))

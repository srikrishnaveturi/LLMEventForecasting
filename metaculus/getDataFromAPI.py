import requests

response = requests.get('https://www.metaculus.com/api2/questions/?publish_time__gt=2021-12-31&resolve_time__lt=2023-01-01')

print(response.json()['results'])


import requests

f = open('smarty/input/week02.txt')
lines = [line.rstrip() for line in f.readlines()]

auth = open('smarty/auth.txt')
auth_id, auth_key = [line.rstrip() for line in auth.readlines()]

part1 = []

for line in lines:
  street = line
  response = requests.get(f'https://us-street.api.smartystreets.com/street-address?auth-id={auth_id}&auth-token={auth_key}&street={street}')
  response = response.json()
  part1 += [response[0]['components']['default_city_name']]

part1 = ', '.join(part1)

print(f'part 1: {part1}')

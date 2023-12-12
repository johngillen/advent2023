import requests

f = open('smarty/input/week01.txt')
lines = [line.rstrip() for line in f.readlines()]

auth = open('smarty/auth.txt')
auth_id, auth_key = [line.rstrip() for line in auth.readlines()]

part1 = 0

sum = 0
for line in lines[3:]:
  street, city, state, zipcode = line.split(', ')
  response = requests.get(f'https://us-street.api.smartystreets.com/street-address?auth-id={auth_id}&auth-token={auth_key}&street={street}&city={city}&state={state}&zipcode={zipcode}')
  response = response.json()
  sum += int(response[0]['metadata']['latitude'])
  sum += int(response[0]['metadata']['longitude'])

part1 = abs(sum)

print(f'part 1: {part1}')

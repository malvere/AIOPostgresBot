import requests
from itertools import takewhile as t, repeat as r


# Function to request information based on intagram username via API
def request(username):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = (f'https://www.instagram.com/{username}/channel/?__a=1')
    r = requests.get(url, headers=headers)
    if r.text == '{}':
        # Free
        return False
    elif r.text[:2] == '{"':
        # Taken
        return True
    elif 'Login • Instagram' in r.text:
        # Too many requests, 60s timeout.
        print('Please wait')
        return 'wait'


# Function to count number of available usernames in the .txt file
def rawincount(filename):
    f = open(filename, 'rb')
    bufgen = t(lambda x: x, (f.raw.read(1024*1024) for _ in r(None)))
    return sum(buf.count(b'\n') for buf in bufgen)

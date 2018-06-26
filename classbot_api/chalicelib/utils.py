import requests
from chalicelib import config

def do_get_request(url,header) :
    r = requests.get(url, headers=header)
    return r.json()
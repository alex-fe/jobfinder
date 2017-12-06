
# import json
import getpass
import socket
# import requests

from utils import add_url_params


GLASSDOOR_URL = 'http://api.glassdoor.com/api/api.htm'


def get(query, params):
    params.update({
        'v': 1.1,
        'format': 'json',
        'q': query,
        'action': 'job',
        'userip': socket.gethostbyname(socket.gethostname()),
        'useragent': '51.0.2704.84'
    })
    print add_url_params(GLASSDOOR_URL, params)


def main():
    KEY = getpass.getpass("Please type key")
    PID = getpass.getpass('Please type Partner ID')
    params = {'t.k': KEY, 't.p': PID}
    get(params)


if __name__ == '__main__':
    main()

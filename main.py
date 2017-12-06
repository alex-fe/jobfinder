
# import getpass
import urllib2
import socket

from bs4 import BeautifulSoup

from utils import BadData, add_url_params


GLASSDOOR_URL = 'http://api.glassdoor.com/api/api.htm'


def get(query, params):
    params.update({
        'v': '1',
        'format': 'json',
        'q': query,
        'action': 'employers',
        'userip': '192.168.43.42',
        'useragent': 'Mozilla'
    })
    url = add_url_params(GLASSDOOR_URL, params)
    header = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(req)
    soup = BeautifulSoup(response, "html.parser")
    if not soup:
        raise BadData(params)
    else:
        return soup


def main():
    # query = raw_input('What kind of job are you looking for? ')
    # KEY = getpass.getpass("Please type key")
    # PID = getpass.getpass('Please type Partner ID')
    KEY = 'bBT8AIvltt9'
    PID = '235446'
    params = {'t.k': KEY, 't.p': PID}
    data = get('developer', params)
    
    

if __name__ == '__main__':
    main()

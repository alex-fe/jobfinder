
import json
import urllib2

from bs4 import BeautifulSoup

from job import Job

from utils import BadData, add_url_params


GLASSDOOR_URL = 'http://api.glassdoor.com/api/api.htm'
KEY = 'bBT8AIvltt9'
PID = '235446'


def get(params):
    """Modified GET request.

    Args:
        params(dict): Dictionary of query parameters.

    Returns:
        JSON encoded dictionary.
    """
    params.update({
        'v': '1',
        'format': 'json',
        'action': 'jobs',
        'userip': '192.168.43.42',
        'useragent': 'Mozilla'
    })
    url = add_url_params(GLASSDOOR_URL, params)
    header = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(req)
    soup = BeautifulSoup(response, "html.parser")
    return json.loads(str(soup))


def main():
    """Operation headquarters."""
    # query = raw_input('What kind of job are you looking for? ')
    params = {'t.k': KEY, 't.p': PID, 'q': 'developer'}
    try:
        json = get(params)
    except urllib2.HTTPError, err:
        raise err
    else:
        jobs = [Job(j) for j in json['response']['employers']]
        import pdb; pdb.set_trace()

if __name__ == '__main__':
    main()

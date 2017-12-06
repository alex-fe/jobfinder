from json import dumps

from pprint import pprint
from urllib import unquote, urlencode
from urlparse import ParseResult, parse_qsl, urlparse


class BadData(Exception):
    def __init__(self, params):
        pprint(params)


def add_url_params(url, params):
    """Add query params to URL.

    Args:
        url(str): Base url.
        params(dict): Dictionary of query parameters.
    Returns:
        Url with added parameters.
    """
    url = unquote(url)
    parsed_url = urlparse(url)
    parsed_get_args = dict(parse_qsl(parsed_url.query))
    parsed_get_args.update(params)
    parsed_get_args.update({
        k: dumps(v) for k, v in parsed_get_args.iteritems()
        if isinstance(v, (bool, dict))
    })
    encoded_get_args = urlencode(parsed_get_args, doseq=True)
    return ParseResult(
        parsed_url.scheme,
        parsed_url.netloc,
        parsed_url.path,
        parsed_url.params,
        encoded_get_args,
        parsed_url.fragment
    ).geturl()

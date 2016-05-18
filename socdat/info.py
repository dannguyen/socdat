from request import resource_endpoint, views_endpoint, read_url
from urllib.parse import urlencode, urlparse


def count_rows(url):
    """returns: an Int
    """
    u = resource_endpoint(url)
    xurl = urlparse(u)._replace(query=urlencode({'$select': 'count(*)'})).geturl()
    data = read_url(xurl)
    return int(data[0]['count'])

def count_columns(url):
    return len(get_columns(url))


def get_dims(url):
    return {'columns': count_columns(url), 'rows': count_rows(url)}

def get_columns(url):
    data = read_url(views_endpoint(url))
    return data['columns']

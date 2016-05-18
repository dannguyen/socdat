from collections import namedtuple
from pathlib import Path
from urllib.parse import urlparse, urlunparse
from urllib.request import urlopen
import json

ResourceParts = namedtuple('ResourceParts', ['id', 'domain', 'protocol'])

def metadata_endpoint(url):
    """ Returns a metadata URL
    @url (String):
       "https://data.seattle.gov/dataset/City-of-Seattle-Events/cprz-jsz8"

    returns (String):
        "https://data.seattle.gov/metadata/v1/dataset/kjqu-s8f9.json" """
    p = extract_resource(url)
    path = Path('metadata', 'v1', p.type, p.id + '.json')
    return urlunparse((p.protocol, p.domain, str(path), '', '', ''))

def resource_endpoint(url):
    """ https://dev.socrata.com/docs/endpoints.html

       From: "https://data.seattle.gov/dataset/City-of-Seattle-Events/cprz-jsz8"
       To: 'https://data.seattle.gov/resource/cprz-jsz8.json' """
    p = extract_resource(url)
    path = Path('resource', p.id + '.json')
    return urlunparse((p.protocol, p.domain, str(path), '', '', ''))

def views_endpoint(url):
    p = extract_resource(url)
    path = Path('views', p.id + '.json')
    return urlunparse((p.protocol, p.domain, str(path), '', '', ''))


def extract_resource(url):
    """extracts the bare minimum information from a Socrata URL
       needed to reconstruct the URL for different views"""
    u = urlparse(url)
    r = {}
    r['protocol'] = u.scheme
    r['domain'] = u.netloc
    r['id'] = Path(u.path).stem
#    r['type'], r['seoname'], r['id'] = upath.parts[1:]
    # r['type'] = upath.parts[1]

    return ResourceParts(**r)



# muh???

def read_url(url):
    resp = urlopen(url)
    if resp.status == 200:
        txt = resp.read().decode(resp.headers.get_charsets()[0])
        data = json.loads(txt)
        return data

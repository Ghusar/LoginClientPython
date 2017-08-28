try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse

from urllib2 import Request, urlopen

import urllib

import ssl

import time

url = 'https://10.100.56.55:8090/logout.xml'

post_fields = {
                'mode':'191',
                'username':'*****',
                'password':'*****',
                'a':'1503796951397',
                'producttype':'0'
            }     # Set POST fields here


request = Request(url, urllib.urlencode(post_fields))
json = urlopen(request,context=ssl._create_unverified_context()).read().decode()
print json
time.sleep(3600)

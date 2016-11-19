from __future__ import unicode_literals
import requests

def ping_services(event, context):
    url_list = {
        "payments" : "https://google.ie"
    }
    url_list.update(event)

    for key, value in url_list.iteritems():
        headers = {'content-type': 'text/xml'}
        # We set verify to false to avoid using a cert... Not good, but meh
        response = requests.get(value, headers=headers, verify=False, allow_redirects=False, timeout=5) 
        # log to CloudWatch
        response.raise_for_status()
        print response.status_code



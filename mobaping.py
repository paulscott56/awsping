from __future__ import unicode_literals
import requests

def ping_services(event, context):
    url_list = [
        'https://novaservice?wsdl',
        'https://PaymentWebService?wsdl',
        'https://transfersService?WSDL'
    ]
    url_list.update()
    
    for u in url_list:
        headers = {'content-type': 'text/xml'}
        # We set verify to false to avoid using a cert... Not good, but meh
        response = requests.get(url, headers=headers, verify=False, allow_redirects=False, timeout=5) 
        # log to CloudWatch
        response.raise_for_status()
        #print response.text



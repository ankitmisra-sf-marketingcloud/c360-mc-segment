from auth import *
from var import *
from c360api import *
from datetime import datetime
import json
import time
import requests
import pandas as pd
from pandas import json_normalize

def mc_ingest():
    print('Pushing Segment data into ET...')

mc_header = {'Authorization': 'Bearer ' + mc_access_token, 'content-Type':'application/json'}

DE_ID = 'DC4734C2-960C-4A34-925C-B6E0E9557A0F'
DE_ID2 = '780EF6FD-5399-46D8-AD95-B7D11B23A04C'

mc_de_response = requests.put('https://{}.rest.marketingcloudapis.com/data/v1/async/dataextensions/key:{}/rows'.format(MC_SUBDOMAIN,DE_ID),headers = mc_header, json = c360a_segment)
mc_de_response_2 = requests.put('https://{}.rest.marketingcloudapis.com/data/v1/async/dataextensions/key:{}/rows'.format(MC_SUBDOMAIN,DE_ID2),headers = mc_header, json = c360a_segment)


print(mc_de_response.status_code)
print('ET Data Extension updated...')

from auth import *
from var import *
from datetime import datetime
import json
import jwt
import time
import requests
import pandas as pd
from pandas import json_normalize

def c360_segmentation():
    print('Querying C360 data...')
header = {'Authorization': 'Bearer' +" "+c360_access_token, 'content-Type':'application/json'}

response = requests.post('https://{}/api/v1/query'.format(C360A_INSTANCE_URL), headers=header, json = {
    "sql": "SELECT DataSourceId__c, DataSourceObjectId__c, FirstName__c, Id__c, LastName__c FROM Individual__dlm LIMIT 100"
})

c360a_segment = response.json()

#c360_data = json_normalize(c360a_segment['data'])
print('C360 segment generated...')

print('Normalizing Segment for MC...')

keys_to_remove = ['startTime','endTime','rowCount','queryId','done','metadata']
for key in keys_to_remove:
    c360a_segment.pop(key)


c360a_segment['items'] = c360a_segment.pop('data')

print('Segment ready for MC...')

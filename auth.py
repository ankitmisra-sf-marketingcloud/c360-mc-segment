# pip install jwt cryptography requests

from datetime import datetime
import json
import jwt
import time
import requests
from var import *


def Oauth_Jwt():
    print('Loading private key...')
with open(KEY_FILE) as fd:
    private_key = fd.read()

print('Generating signed JWT assertion...')
claim = {
    'iss': ISSUER,
    'exp': int(time.time()) + 300,
    'aud': 'https://{}.salesforce.com'.format(DOMAIN),
    'sub': SUBJECT,
}
assertion = jwt.encode(claim, private_key, algorithm='RS256', headers={'alg':'RS256'})

print('Making OAuth request...')
initial_req = requests.post('https://{}.salesforce.com/services/oauth2/token'.format(DOMAIN), data = {
    'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
    'assertion': assertion,
})


op_json = initial_req.json()

access_token = op_json['access_token']
instance_url = op_json['instance_url']
C360_DOMAIN = instance_url.split('.')[0]




final_token = requests.post('{}.my.salesforce.com//services/a360/token'.format(C360_DOMAIN), data = {
    'grant_type': 'urn:salesforce:grant-type:external:cdp',
    'subject_token_type':'urn:ietf:params:oauth:token-type:access_token',
    'subject_token':access_token})

c360_json = final_token.json()
c360_access_token = c360_json['access_token']
print('OAuth Sucessful...')
""" print(access_token)
print(instance_url)
print(c360_access_token)
#print('Status:', r.status_code)
print(c360_json)
 """

print('Making OAuth request for MC...')
mc_token = requests.post('https://{}.auth.marketingcloudapis.com/v2/token'.format(MC_SUBDOMAIN),headers={'content-Type':'application/json'},json = {
    'grant_type': 'client_credentials',
    'client_id': MC_CLIENT_ID,
    'client_secret': MC_CLIENT_SECRET,
    'account_id': MID
})

mc_json = mc_token.json()

mc_access_token = mc_json['access_token']
print('All Auth Complete...')

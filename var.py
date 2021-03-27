SALESFORCE_LOGIN_URL = 'login.salesforce.com'
SALESFORCE_INSTANCE_URL = 'ankitmisracdp.my.salesforce.com'
SALESFORCE_AUTH_USER = 'ankitmisra@ankitmisra-20200526.demo'
SALESFORCE_CONSUMER_KEY = '3MVG95jctIhbyCpq7dK9hiIJ7jenbq5i3.GHDACFP8wPnedAFNhch940P38AoAp9wYzLikl3iDXcIujlTI5lg'
SALESFORCE_CONSUMER_SECRET = '8487B7A40D1163FAF845F2C57C5036C0AC91BF210E6D4979CB28620D38EE837D'
C360A_INSTANCE_URL = 'h02dkyzzmnqt1zd0gjsg8nzvg4.c360a.salesforce.com'
MC_CLIENT_ID = 'j1nvrdvw7kk34yt2a3u9dre9'
MC_CLIENT_SECRET = 'dLPgR4IYmjaEkoDsFveEAQqt'
MC_SUBDOMAIN = 'mctb7k9kxpq0mgvhkp-kjs714z-0'
BASE_URI = 'https://mctb7k9kxpq0mgvhkp-kjs714z-0.auth.marketingcloudapis.com/'
REST_URI = 'https://mctb7k9kxpq0mgvhkp-kjs714z-0.rest.marketingcloudapis.com/'
MID = '523001787'
# *** Update these values to match your configuration ***
IS_SANDBOX = False
KEY_FILE = 'salesforce.key'
ISSUER = SALESFORCE_CONSUMER_KEY
SUBJECT = SALESFORCE_AUTH_USER
# *******************************************************

DOMAIN = 'test' if IS_SANDBOX else 'login'



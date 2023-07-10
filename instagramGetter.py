import requests
import json
from decouple import AutoConfig

config = AutoConfig()

#Url para conseguir um código atualizado
#https://api.instagram.com/oauth/authorize?client_id=1310982763154267&redirect_uri=https://alexfoppa.github.io/SocintMH/&scope=user_profile,user_media&response_type=code

authorizationCode = 'AQC6XEO2omsyngzD4towudmSruqzpz6hXtQl1SKoZDSZdH7sGBGvKjS3D6qddtjSDQ3H4iumUnoaOAOt34j71oEeR9Vmgunq8klkM-f2ZbacMosD1OkDCooAGf9Q9vLr4vLenhs5wY2K2OyrELNAyGROM-wpX2LPUhYeYA1RNk_9x4oa7G49GtsAUHN91KDn8KLwlDmfMsea8_M62HwE4JvgWRBDa4bLeMJIcb7R4SOqCQ'
url = 'https://api.instagram.com/oauth/access_token'

params = {
  'client_id': config('API_ID'),
  'client_secret': config('API_SECRET'),
  'grant_type': 'authorization_code',
  'redirect_uri': 'https://alexfoppa.github.io/SocintMH/',
  'code': authorizationCode
}
 
response = requests.post(url, data=params )

if response.status_code == 200:
   apiReturn = json.loads(response.text)
   access_token = apiReturn['access_token']
   user_id = apiReturn['user_id']
else:
    print('Erro na solicitação POST:', response.status_code)
    print('Resposta:', response.text)

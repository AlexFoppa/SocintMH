import requests
import json
from decouple import AutoConfig

def get_insta_id(authorizationCode):
  config = AutoConfig()
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
    return user_id, access_token
  else:
    print('Erro na solicitação POST:', response.text)

def get_insta_profile(user_id, access_token):
  url = 'https://graph.instagram.com/'+str(user_id)
  
  params = {
    'fields': 'id,account_type,media_count,username',
    'access_token': access_token
  }

  response = requests.get(url, params=params)

  if response.status_code == 200:
    data = response.json()
    return data
  else:
    print('Erro na solicitação GET:', response.text)

def get_insta_media(access_token):
  url = 'https://graph.instagram.com/me/media'
  params = {
    'fields': 'id,caption,is_shared_to_feed,media_type,media_url,permalink,thumbnail_url,timestamp,username',
    'access_token': access_token
  }
  
  response = requests.get(url, params=params)

  if response.status_code == 200:
    data = response.json()
    return data
  else:
    print('Erro na solicitação GET:', response.text)
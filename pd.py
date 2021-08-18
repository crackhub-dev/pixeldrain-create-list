import requests
import json

title = input('Enter List Title: ')

try:
  f = open('links.txt')

  
  pd_auth_key = open('auth_key.txt').read()

      #print('Place auth_key.txt next to program and paste your pd_auth_key into it.')
      #print("Don't know where to get it? Get cooki-editor browser extension, go to pixeldrain.com, sign in, click on cooki-editor extension and copy the value of 'pd_auth_key' cookie.")
  l_list = f.readlines()

  id_list = []
  for link in l_list:
       f_id = link.split('/')[-1].strip('\n')
       id_list.append(f_id)
  
  json_dict = {
    "title": str(title),
    "anonymous": False,
    "files": [
    ]
  }


  for f_id in id_list:
      json_dict['files'].append({"id":f_id, "description": "none" },)

  json_obj = json.dumps(json_dict)

  headers = {
      'Content-Type': 'application/json',
  }
  cookies = {
      'pd_auth_key': pd_auth_key,
  }
  response = requests.post('https://pixeldrain.com/api/list', headers=headers, cookies=cookies, data=json_obj)
  print('https://pixeldrain.com/l/' + response.json()['id'])
except FileNotFoundError:
  print('FAILED! Place links.txt next to the program and paste your links inside of it (Seperated by new line).')

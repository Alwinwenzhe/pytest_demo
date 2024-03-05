import requests
import json

header = {'Authorization': 'Bearer 225d3bdc4c90486bac12f18d61808ea4'}
data = ''
upload_files = "{'image': ('suidao1.jpeg', open('suidao1.jpeg', 'rb'), 'image/jpeg')}"
url = 'http://192.168.2.199:48080/admin-api/system/file/procedure/upload'
dict_up= eval(upload_files)
try:
    if upload_files:
        response = requests.post(url=url, files=dict_up, headers=header, verify=False)
    else:
        response = requests.post(url=url, data=json.dumps(data), headers=header, verify=False)
except requests.RequestException as e:
    print(e)
    response = None
res = response
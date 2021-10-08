url="https://api.lyrics.ovh/v1/Ed Sheeran/Shape of you"
import requests
import json
rest=requests.get(url)
if rest.status_code==200:
    response=json.loads(rest.text)
    print(response)
else:
    print('Xatolik')
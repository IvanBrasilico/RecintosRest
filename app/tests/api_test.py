import json

import requests

payload = {
    'recinto': '00001'
}
headers = {'content-type': 'application/json'}
r = requests.post("http://localhost:5000/api/eventos",
                  data=json.dumps(payload),
                  headers=headers)
print(r.status_code)

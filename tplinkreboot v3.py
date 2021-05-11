import requests
r = requests.get('http://192.168.129.1' , auth=('admin', 'admin'))
r.text

import requests
class MyAuth(requests.auth.AuthBase):
     def __call__(self, r):
         # Implement my authentication
         return r

url = 'http://192.168.129.1'
requests.get(url, auth=MyAuth())
print(r)

payload = { 'username': 'admin', 'password': 'admin' }
with requests.Session() as s:
  p = s.post('http://192.168.129.1/', data=payload) 
  p = s.get('http://192.168.129.1/userRpm/SysRebootRpm.htm')
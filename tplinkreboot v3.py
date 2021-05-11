#teste login 1 ok
import requests
r = requests.get('http://192.168.129.1' , auth=('admin', 'admin'))
r.text

#teste login 2 ok

import requests
class MyAuth(requests.auth.AuthBase):
     def __call__(self, r):
         # Implement my authentication
         return r

url = 'http://192.168.129.1'
requests.get(url, auth=MyAuth())
print(r)

#teste login 3 ok

payload = { 'username': 'admin', 'password': 'admin' }
with requests.Session() as s:
  p = s.post('http://192.168.129.1/', data=payload) 
  p = s.get('http://192.168.129.1/userRpm/SysRebootRpm.htm')

  #não sei como pegar a confirmação de rebbot que o scrit gera para executar a solicitação

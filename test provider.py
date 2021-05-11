import requests

payload = { 'username': 'admin', 'password': 'admin' }
with requests.Session() as s:
  p = s.post('http://192.168.129.1/', data=payload) 
  p = s.get('http://192.168.129.1/userRpm/SysRebootRpm.htm')
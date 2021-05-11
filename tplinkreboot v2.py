import base64
import requests

from http.client import HTTPConnection

# Change default router IP if needed.
ip = '192.168.129.1'
# Update username:password if changed.
auth = 'admin:admin'

Conn = HTTPConnection(ip)
auth = base64.b64encode(auth.encode()).decode('ascii')

headers = {
    'referer': 'http://' + ip,
    'cookie': 'Authorization=Basic ' + auth
}

try:
    Conn.request('GET', '/userRpm/SysRebootRpm.htm', headers=headers)
except Exception:
    print('Failed to connect. Check if IP / auth is valid.')
    exit()

body = str(Conn.getresponse().read())

start = body.find('var sessionKey')
end = body.find(';', start)

if start != -1:
    key = body[start + 19: end - 2]

    print('Rebooting...')
    Conn.request('GET', '/userRpm/SysRebootRpm.htm' + key, headers=headers)
else:
    print('Failed to reboot!')

Conn.close()
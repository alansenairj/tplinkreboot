#!/usr/bin/python3
# imports
from requests import get
from base64 import b64encode
from urllib.parse import quote


# constants
tplink = '192.168.129.1'
user = 'admin'
password = 'admin'
url_template = 'http://{}/userRpm/SysRebootRpm.htm?Reboot=Reboot'


if __name__ == '__main__':
    auth_bytes = bytes(user+':'+password, 'utf-8')
    auth_b64_bytes = b64encode(auth_bytes)
    auth_b64_str = str(auth_b64_bytes, 'utf-8')

    auth_str = quote('Basic {}'.format(auth_b64_str))

    auth = {
    'Referer': 'http://'+tplink+'/', 
    'Authorization': auth_str,
    }

    reboot_url = url_template.format(tplink)

    r = get(reboot_url, headers=auth)
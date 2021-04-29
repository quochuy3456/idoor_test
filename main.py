import sys
import re
import json
import requests
from datetime import datetime

# url = "https://verify.idoors.jp/login"
url = 'http://cloud.idoors.jp/domain/'


def test_login():
    _updateurl = url + "api/login"
    payload = {
        "id": "admin",
        "pass": "admin"
    }
    headers = {'Content-Type': 'application/json'}
    r = requests.post(_updateurl, data=json.dumps(payload), headers=headers, verify=False)
    print(r.status_code)
    print(r.json())

def test_confirm_domain():
    _updateurl = url + "api/domain"
    payload = {
        "id": "admin",
        "pass": "admin"
    }
    headers = {'Content-Type': 'application/json'}
    r = requests.get(_updateurl)
    print(r.status_code)
    print(r.json())

test_confirm_domain()
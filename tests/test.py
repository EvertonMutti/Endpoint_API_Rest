# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:58:14 2023

@author: Everton
"""

import requests
import json

link = 'link' #put the ip or link of your API here, I recommend putting the code in the replit and running the API for testing
jsona = {
    "password": "AbcdEfgHiklmnqwerj!1234&",
    "rules": [
        {"rule": "minSize", "value": 8},
        {"rule": "minSpecialChars", "value": 2},
        {"rule": "noRepeted", "value": 0},
        {"rule": "minDigit", "value": 4},
        {"rule": "minUppercase", "value": 3},
        {"rule": "minLowercase", "value": 12}
    ]
}

requisicao = requests.post(link, json.dumps(jsona))
print(requisicao.json())

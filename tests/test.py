# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:58:14 2023

@author: Everton
"""

import requests
import json

link = 'https://APIFLASK.antemoutiranha.repl.co/verify'
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

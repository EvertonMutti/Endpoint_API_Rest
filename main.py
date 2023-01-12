# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 10:38:52 2023

@author: Everton
"""
from flask import Flask, jsonify, request
import re

app = Flask(__name__)

def noRepeted(password):
    set1 = set()
    set1.update(password)
            
    if len(set1) < len(password):
        return False
    else:
        return True


@app.route('/verify', methods=['POST'])
def verifyPassword():

    verify = True
    no_match = []
    data = request.get_json(force=True)
    if 'rules' not in data or 'password' not in data:
        return jsonify(
            status_code=400,
            content={
                "message": "Make sure you are passing the password:str and \
                rules:[rule:str,value:int] arguments"},
        )
                    
    password_json = data.get("password")
    rules = data.get("rules")
    del data
    
    for rul in rules:
        if rul.get('rule') == 'minSize':
            if  len(password_json) < rul.get('value'):
                no_match.append('minSize')
                verify = False
        
        if rul.get('rule') == 'minUppercase':
            varr = re.findall("[A-Z]", password_json)
            if  len(varr) < rul.get('value'):
                no_match.append('minUppercase')
                verify = False
        
        if rul.get('rule') == 'minLowercase':
            varr = re.findall("[a-z]", password_json)
            if  len(varr) < rul.get('value'):
                no_match.append('minLowercase')
                verify = False

        if rul.get('rule') == 'minSpecialChars':
            varr = re.findall("[^A-Za-z0-9]", password_json)
            if len(varr) < rul.get('value'):
                no_match.append('minSpecialChars')
                verify = False

        if rul.get('rule') == 'noRepeted':
            if not noRepeted(password_json):
                no_match.append('noRepeted')
                verify = False

        if rul.get('rule') == 'minDigit':
            varr = re.findall("[0-9]", password_json)
            if len(varr) < rul.get('value'):
                no_match.append('minDigit')
                verify = False
                
    return jsonify({'verify': verify, 'noMatch': no_match})


app.run(host='0.0.0.0')

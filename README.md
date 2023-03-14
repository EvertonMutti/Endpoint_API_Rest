# Endpoint_API_Rest
Endpoint made in python's flask framework
The code was based on a test of studio sol's ability for full developer just to be able to learn and have more projects, the Rest API in question would be receiving this data by the POST method:
Input code below:

<code>
{
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
</code>

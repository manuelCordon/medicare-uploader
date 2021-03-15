from datetime import datetime

import requests


def start_session(authorization_token):
    url = "https://www.sunfirematrix.com/v2/session"

    payload = {
        "zip": "33133",
        "county": "12086",
        "applicants": [
            {
                "type": "primary",
                "birthMonth": 12,
                "birthDay": 7,
                "birthYear": 1950,
                "gender": "male",
                "smoker": False,
                "health": "I don't know"
            }
        ]
    }

    headers = {
        'accept': 'application/json',
        'authorization': authorization_token,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()["customerCode"]


def get_plans(customer_code, authorization_token):
    url = "http://www.sunfirematrix.com/v2/plans/profile/%s/%d" % (customer_code, datetime.now().year)

    headers = {
        'accept': 'application/json',
        'authorization': authorization_token
    }

    response = requests.request("GET", url, headers=headers)

    return response.json()

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

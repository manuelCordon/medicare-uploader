import requests
import datetime


def get_plans(customer_code, authorization_token):
    url = "http://www.sunfirematrix.com/v2/plans/profile/%s/%d" % (customer_code, datetime.datetime.now().year)

    headers = {
        'accept': 'application/json',
        'authorization': authorization_token
    }

    response = requests.request("GET", url, headers=headers)

    return response.json()

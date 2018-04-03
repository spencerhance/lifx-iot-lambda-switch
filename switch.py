import os
from botocore.vendored import requests


token = os.environ['API_KEY']

headers = {
    "Authorization": "Bearer %s" % token,
}

payload = {
    "power": "off",
}


def lambda_handler(event, context):

    # Find current state of lights
    response = requests.get('https://api.lifx.com/v1/lights/all', headers=headers).json()
    status = response[0]['power']

    # If light is off, set power to on
    if status == 'off':
        payload['power'] = 'on'

    # Toggle light
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers).json()

    return response

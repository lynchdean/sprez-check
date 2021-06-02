import json

import requests as requests

webhook_url = ""
data = {
    "content": "Bookings available",
    "username": "Sprezzatura Bot"
}


def get_json():
    r = requests.get(
        'https://app.resmio.com/v1/facility/sprezzatura/availability?num=4&date__gte=2021-6-12&resource_group=&end_of_acceptance_enabled=true&date=2021-06-11T23:00:00.000Z')
    return json.loads(r.text)


if __name__ == '__main__':
    json = get_json()
    for obj in json["objects"]:
        if obj["available"]:
            requests.post(webhook_url, json=data)
            break

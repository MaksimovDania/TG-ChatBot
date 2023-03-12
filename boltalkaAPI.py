import requests


def create_request(message):
    data = {
        "instances": [
            {
                "contexts": [
                    [
                        message
                    ]
                ]
            }
        ]
    }
    return data


def send_request(request):
    url = 'https://api.aicloud.sbercloud.ru/public/v2/boltalka/predict'
    # headers = {"Content-Type": "application/json", "accept": "application/json"}
    answer = requests.post(url, json=request)  # headers=headers
    return answer

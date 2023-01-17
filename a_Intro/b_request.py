import requests
import time


def request():
    requests.post(
        "http://127.0.0.1:3000/classify",
        headers={"content-type": "application/json"},
        data="[[5.9, 3, 5.1, 1.8]]",
    ).text


if __name__ == "__main__":
    send_number = 10
    for _ in range(send_number):
        request()
        time.sleep(1)

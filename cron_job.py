import time
import schedule
import launch
import requests

def print_hello():
    response = requests.get('http://127.0.0.1:5000/ebay')
    print(response.content)

schedule.every(10).seconds.do(print_hello)

while True:
    schedule.run_pending()
    time.sleep(1)
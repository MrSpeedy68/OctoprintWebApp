import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
api_url = "http://192.168.1.16/api"

auth_header = {'X-Api-Key': API_KEY}


def get_nozzle_info():
    nozzle_get = "/printer/bed"
    return requests.get(api_url+nozzle_get, headers=auth_header)

if __name__ == "__main__":
    print(get_nozzle_info().text)





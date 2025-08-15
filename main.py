import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
url = "https://api.football-data.org/v4/competitions/2013/teams"
headers = {"X-Auth-Token":os.getenv("TOKEN_FOOTBALL")}
body = {"season":2025}
teste = requests.get(url=url,headers=headers,params= body).json()
print(teste)
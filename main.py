import requests
import json
url = "https://api.football-data.org/v4/competitions/2013/teams"
headers = {"X-Auth-Token":"52da30433cfc4394b39d8ec14da17145"}
body = {"season":2025}
teste = requests.get(url=url,headers=headers,params= body).json()
print(teste)
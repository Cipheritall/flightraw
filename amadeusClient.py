import json
import amadeus

with open(".env","r") as fenv:
    data = json.load(fenv)
    f_client_id = data["client_id"]
    f_client_secret = data["client_secret"]
    

amaclient = amadeus.Client(
    client_id=f_client_id,
    client_secret=f_client_secret
)
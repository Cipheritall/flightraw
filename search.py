import json
from amadeusClient import amaclient
import pandas as pd

def get_flight_offers_search(o_place,d_place,depart_date,adults):
    try:
        response = amaclient.shopping.flight_offers_search.get(
            originLocationCode=o_place,
            destinationLocationCode=d_place,
            departureDate=depart_date,
            adults=adults)
        print("OK")
        return response 
    except Exception as error:
        print("KO")
        print(f"Error : {error}")
        return -1
    return True

o_place = "NCE"
d_place = "MPL"
depart_date = "2022-10-15"
adults = "1"

res = get_flight_offers_search(o_place,d_place,depart_date,adults)
df = pd.DataFrame(res.data)

print(df)
df.to_csv("response.csv")
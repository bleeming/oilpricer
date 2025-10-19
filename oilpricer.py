import json
import sqlite3

import pandas as pd
import requests

url = "https://www.boilerjuice.com/uk/ajax/price_chart?area=3&oilType=1&days=1460&vat=1&ex=0"
headers = {"x-requested-with": "XMLHttpRequest"}

response = requests.get(url, headers=headers)

response_formatted_text = response.text.replace("=>", ":").replace("nil", "null")

rows = list(json.loads(response_formatted_text)["rows"])

df = pd.DataFrame(
    [
        (pd.to_datetime(rows[i]["c"][0]["v"]), rows[i]["c"][1]["v"])
        for i, ix in enumerate(rows)
    ],
    columns=["date", "price"],
)

df.head()
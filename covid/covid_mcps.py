"""
get list of all headlines
get 3 mcps of each month
"""
import json
import requests

from common import headers, text_url, parse

mcps_url = text_url + "most_common_phrases"

# get the mcps asynchronously
def get_hl_mcps(year, month):
    body = {
        "text": parse(year, month)
    }
    response = requests.post(mcps_url, headers=headers, json=body)
    _dict = json.loads(response.text)
    mcps = _dict["most common phrases"]
    print(mcps)
    with open(f"mcps/{year}_{month}_values.txt", "w") as f:
        f.write("\n".join(mcps))
    return mcps

for year in [2020, 2021]:
    for month in range(12):
        if year == 2020 and month < 3:
            continue
        get_hl_mcps(year, month+1)
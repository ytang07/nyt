import json
import requests

from archive import month_dict
from config import thetextapikey

headers = {
    "Content-Type": "application/json",
    "apikey": thetextapikey
}
base_url = "https://app.thetextapi.com/text/"
polarity_url = base_url+"polarity_by_sentence"

def get_polarity(year, month):
    filename = f"{year}/{month_dict[month]}.json"
    try:
        with open(filename, "r") as f:
            entries = json.load(f)
    except:
        print("No such file")
        return

    headlines = ""
    for entry in entries:
        headline = entry['headline']['main']
        headline = headline.replace('.', '')
        headlines += headline + ". "
    body = {
        "text": headlines
    }
    res = requests.post(polarity_url, headers=headers, json=body)
    _dict = json.loads(res.text)
    with open(f"{year}/{month_dict[month]}_Polarity.json", "w") as f:
        json.dump(_dict["polarity by sentence"], f)

# checks headlines for climate change
def cc_finder(year, month):
    filename = f"{year}/{month_dict[month]}.json"
    try:
        with open(filename, "r") as f:
            entries = json.load(f)
    except:
        print("No such file")
        return
    # get every headline
    # check if it has climate change in it
    total_headlines = len(entries)
    # print(total_headlines)
    cc = 0
    for entry in entries:
        headline = entry['headline']['main']
        if "climate" in headline.lower():
            cc += 1
    # print(cc)
    return (total_headlines, cc)

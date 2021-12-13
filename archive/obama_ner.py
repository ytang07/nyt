# import libraries
import requests
import json
import sys
sys.path.append("../..")
from nyt.config import thetextapikey, _url

# set up request headers and URL
headers = {
    "Content-Type": "application/json",
    "apikey": thetextapikey
}
ner_url = _url + "ner"

# loop through each year
for i in list(range(2008, 2018)):
    with open(f"obama_{i}.txt", "r") as f:
        headlines = f.readlines()
    # combine list of headlines into one text
    text = "".join(headlines)
    
    # set up request bodies
    body = {
        "text": text,
        "labels": "ARTICLE"
    }
    # parse responses
    response = requests.post(url=ner_url, headers=headers, json=body)
    _dict = json.loads(response.text)
    with open(f"obama/{i}_ner.txt", "w") as f:
        for entry in _dict["ner"]:
            ner = entry[0] + ": " + entry[1]
            f.write(ner)
            f.write('\n')
    # save results to a txt
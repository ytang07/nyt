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
summarize_url = _url + "summarize"

# loop through each year
for i in list(range(2008, 2018)):
    with open(f"obama_{i}.txt", "r") as f:
        headlines = f.readlines()
    # combine list of headlines into one text
    text = "".join(headlines)
    
    # set up request bodies
    body = {
        "text": text,
        "proportion": .1
    }
    # parse responses
    response = requests.post(url=summarize_url, headers=headers, json=body)
    _dict = json.loads(response.text)
    # save results to a txt
    with open(f"obama/{i}_summary.txt", "w") as f:
        f.write(_dict["summary"])

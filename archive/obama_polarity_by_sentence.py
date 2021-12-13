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
polarity_by_sentence_url = _url + "polarity_by_sentence"

# loop through each year
for i in list(range(2008, 2018)):
    with open(f"obama_{i}.txt", "r") as f:
        headlines = f.readlines()
    # combine list of headlines into one text
    text = "".join(headlines)
    text.replace('\n', "")
    
    # set up request bodies
    body = {
        "text": text
    }
    # parse responses
    response = requests.post(url=polarity_by_sentence_url, headers=headers, json=body)
    _dict = json.loads(response.text)
    # save to text file
    with open(f"obama/{i}_sentence_polarities.txt", "w") as f:
        for entry in _dict["polarity by sentence"]:
            f.write(f"{entry[1]} : {entry[0]}")
    
# plot each datapoint

# plot each year
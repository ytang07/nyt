import json
import requests
import sys

from archive import month_dict
sys.path.append("../..")
from nyt.config import thetextapikey

headers = {
    "Content-Type": "application/json",
    "apikey": thetextapikey
}
text_url = "https://app.thetextapi.com/text/"
keyword_url = text_url+"sentences_with_keywords"

def get_doc(year, month):
    filename = f"{year}/{month_dict[month]}.json"
    try:
        with open(filename, "r") as f:
            entries = json.load(f)
        return entries
    except:
        raise NameError("No Such File")

def split_headlines(entries):
    # create total list of headlines and index trackers
    # one index tracker for the inner list of headlines
    # one index tracker for the outer list of headlines
    headlines = []
    idx_tracker = 0
    headlines_idx_tracker = 0
    # loop through all the entries
    for entry in entries:
        # get the headline and modify it
        headline = entry['headline']['main']
        headline = headline.replace('.', '')
        # if the headline index tracker index exists in headlines
        # append to it, otherwise, make it
        if len(headlines) == headlines_idx_tracker:
            headlines.append([headline])
        else:
            headlines[headlines_idx_tracker].append(headline)
        # increment the index tracker
        idx_tracker += 1
        # if the index tracker is at 200, reset it and 
        # increment the headlines index tracker
        if idx_tracker == 200:
            headlines_idx_tracker += 1
            idx_tracker = 0
    return headlines

def get_sentences_with_keywords(kws: list, text: str):
    body = {
        "text": text,
        "keywords": kws
    }
    response = requests.post(keyword_url, headers=headers, json=body)
    print(response)
    _dict = json.loads(response.text)
    return _dict

def search(year, month, terms):
    entries = get_doc(year, month)
    headlines_list = split_headlines(entries)
    kws = []
    for headlines in headlines_list:
        text = ". ".join(headlines)
        _dict = get_sentences_with_keywords(terms, text)
        kws.append(_dict)
    with open(f"{year}/{month_dict[month]}.json", "w") as f:
        json.dump(kws, f)

for year in range(2000, 2022):
    for month in range(12):
        search(year, month+1, ["climate change", "global warming", "renewable energy"])
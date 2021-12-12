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

# load a document
def get_doc(year, month):
    filename = f"{year}/{month_dict[month]}.json"
    try:
        with open(filename, "r") as f:
            entries = json.load(f)
        return entries
    except:
        raise NameError("No Such File")

# split headlines because 4000 headlines is way too many to handle at once
# will cause a timeout and the socket connect to close
def split_headlines(entries):
    headlines1 = ""
    headlines2 = ""
    headlines3 = ""
    headlines4 = ""
    for index, entry in enumerate(entries):
        headline = entry['headline']['main']
        headline = headline.replace('.', '')
        if index < 800:
            headlines1 += headline + ". "
        elif index < 1600:
            headlines2 += headline + ". "
        elif index < 2400:
            headlines3 += headline + ". "
        else:
            headlines4 += headline + ". "
    return [headlines1, headlines2, headlines3, headlines4]

# summary
summarizer_url = text_url+"summarize"
def summarize_headlines(year, month):
    entries = get_doc(year, month)
    headlines_list = split_headlines(entries)
    summaries = []
    for headlines in headlines_list:
        body = {
            "text": headlines,
            "proportion": 0.025
        }
        res = requests.post(summarizer_url, headers=headers, json=body)
        _dict = json.loads(res.text)
        summaries.append(_dict["summary"])
    with open(f"{year}/{month_dict[month]}_Summary.json", "w") as f:
        json.dump(summaries, f)

summarize_headlines(2021, 11)
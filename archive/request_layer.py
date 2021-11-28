import json
import requests

from archive import month_dict
from config import thetextapikey

headers = {
    "Content-Type": "application/json",
    "apikey": thetextapikey
}
text_url = "https://app.thetextapi.com/text/"

def get_doc(year, month):
    filename = f"{year}/{month_dict[month]}.json"
    try:
        with open(filename, "r") as f:
            entries = json.load(f)
        return entries
    except:
        raise NameError("No Such File")

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

# get most common phrases
mcp_url = text_url+"most_common_phrases"
def get_mcp(year, month):
    entries = get_doc(year, month)
    headlines_list = split_headlines(entries)
    mcps = []
    for headlines in headlines_list:
        body = {
            "text": headlines,
            "num_phrases": 5
        }
        res = requests.post(mcp_url, headers=headers, json=body)
        _dict = json.loads(res.text)
        mcps.append(_dict["most common phrases"])
    with open(f"{year}/{month_dict[month]}_MCPs.json", "w") as f:
        json.dump(mcps, f)

# get_mcp(2021, 10)

# get least common phrases
lcp_url = text_url+"least_common_phrases"
def get_lcp(year, month):
    entries = get_doc(year, month)
    headlines_list = split_headlines(entries)
    lcps = []
    for headlines in headlines_list:
        body = {
            "text": headlines,
            "num_phrases": 5
        }
        res = requests.post(lcp_url, headers=headers, json=body)
        _dict = json.loads(res.text)
        lcps.append(_dict["least common phrases"])
    with open(f"{year}/{month_dict[month]}_LCPs.json", "w") as f:
        json.dump(lcps, f)

# get_lcp(2021, 10)

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

# summarize_headlines(2021, 10) 

# ner
ner_url = text_url+"ner"
def get_ner(year, month):
    entries = get_doc(year, month)
    headlines_list = split_headlines(entries)
    ners = []
    for headlines in headlines_list:
        body = {
            "text": headlines,
            "labels": "ARTICLE"
        }
        res = requests.post(ner_url, headers=headers, json=body)
        _dict = json.loads(res.text)
        ners.append(_dict["ner"])
    with open(f"{year}/{month_dict[month]}_NER.json", "w") as f:
        json.dump(ners, f)

get_ner(2021, 10)

#polarity
polarity_url = text_url+"polarity_by_sentence"
def get_polarity(year, month):
    entries = get_doc(year, month)
    headlines_list = split_headlines(entries)
    polarity_list = []
    for headlines in headlines_list:
        body = {
            "text": headlines
        }
        res = requests.post(polarity_url, headers=headers, json=body)
        _dict = json.loads(res.text)
        polarity_list.append(_dict["polarity by sentence"])
    with open(f"{year}/{month_dict[month]}_Polarity.json", "w") as f:
        json.dump(polarity_list, f)

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

import requests
import json

from config import thetextapikey

headers = {
    "Content-Type": "application/json",
    "apikey": thetextapikey
}
text_url = "https://app.thetextapi.com/text/"
keyword_url = text_url+"sentences_with_keywords"

month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

# load headlines from a month
# lowercase all of them
# search for covid
def load_headlines(year, month):
    filename = f"C:\\Users\\ytang\\Documents\\workspace\\teaching\\nyt\\archive\\{year}\\{month_dict[month]}.json"
    with open(filename, "r") as f:
        entries = json.load(f)
    hls = ""
    hls_to_send = []
    # organize entries
    for entry in entries:
        # check if there are two headlines
        if entry['headline']["print_headline"]:
            if entry['headline']["print_headline"][-1] == "!" or entry['headline']["print_headline"][-1] == "?" or entry['headline']["print_headline"][-1] == ".":
                hl2 = entry['headline']["print_headline"]
            else:
                hl2 = entry['headline']["print_headline"] + "."
            # append both headlines 
            if entry['headline']["main"][-1] == "!" or entry['headline']["main"][-1] == "?" or entry['headline']["main"][-1] == ".":
                hl = entry['headline']["main"][:-1]
            else:
                hl = entry['headline']["main"]
            hls += hl + ", " + hl2 + " "
        elif entry['headline']['main']:
            if entry['headline']["main"][-1] == "!" or entry['headline']["main"][-1] == "?" or entry['headline']["main"][-1] == ".":
                hl = entry['headline']["main"]
            else:
                hl = entry['headline']["main"] + "."
            hls += hl + " "
        # if hls is over 3000, send for kws
        if len(hls) > 3000:
            hls_to_send.append(hls[:-1].lower())
            hls = ""
    return(hls_to_send)

import time

def execute(year, month):
    hls = load_headlines(year, month)
    covid_headlines = []
    for hlset in hls:
        body = {
            "text": hlset,
            "keywords": ["covid"]
        }
        start = time.time()
        response = requests.post(keyword_url, headers=headers, json=body)
        _dict = json.loads(response.text)
        covid_headlines += _dict["covid"]
        print(time.time()-start)
    with open(f"covid_headlines/{year}_{month}.txt", "w") as f:
        for entry in covid_headlines:
            f.write(entry + '\n')
        
# def execute(year, month):
#     session = FuturesSession(max_workers=100)
#     hls = load_headlines(year, month)
#     covid_headlines = []
#     responses = [session.post(keyword_url, headers=headers, json={
#             "text": hlset,
#             "keywords": ["covid"]
#         }) for hlset in hls]
#     for response in as_completed(responses):
#         print(response.result().text)
#     with open("{year}_{month}.txt", "w") as f:
#         f.writelines(covid_headlines)
for month in [10, 11, 12]:
    execute(2020, month)
for month in range(12):
    execute(2021, month+1)     
    
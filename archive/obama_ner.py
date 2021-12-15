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

def get_ners():
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
        # save results to a txt
        with open(f"obama/{i}_ner.txt", "w") as f:
            for entry in _dict["ner"]:
                ner = entry[0] + ": " + entry[1]
                f.write(ner)
                f.write('\n')

# get_ners()

# find number of mentions of each type of entity
# dictionary of type: dictionary of name: count
def analyze_ner(year):
    with open(f"obama/{year}_ner.txt", "r") as f:
        ners = f.readlines()
    # type to dictionary dict
    outer_dict = {}
    for ner in ners:
        elements = ner.split(":")
        try:
            _type = elements[0]
            _name = elements[1][:-1]
            if "'s" in _name:
                _name = _name.replace("'s", "")
            if _name[0] == " ":
                _name = _name[1:]
        except:
            continue
        # find number of mentions of each entity within types
        if _type in outer_dict:
            if _name in outer_dict[_type]:
                outer_dict[_type][_name] += 1
            else:
                outer_dict[_type][_name] = 1
        else:
            inner_dict = {}
            inner_dict[_name] = 1
            outer_dict[_type] = inner_dict
    with open(f"obama/{year}_analyzed_ner.json", "w") as f:
        json.dump(outer_dict, f)

# for i in range(2008, 2018):
#     analyze_ner(i)

# find most commonly mentioned entity of each type
def most_common(year):
    with open(f"obama/{year}_analyzed_ner.json", "r") as f:
        entries = json.load(f)
    for _type in entries:
        _sorted = sorted(entries[_type].items(), key = lambda item: item[1], reverse=True)
        if _type == 'PERSON':
            print(f"Most common {_type} (other than Obama) in headlines about Obama in {year} was {_sorted[1][0]} mentioned {_sorted[1][1]} times")
        else:
            print(f"Most common {_type} in headlines about Obama in {year} was {_sorted[0][0]} mentioned {_sorted[0][1]} times")
    print('\n')

for i in range(2008, 2018):
    most_common(i)

# word cloud each one
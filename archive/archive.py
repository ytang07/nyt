import requests
import json
import os
import sys
sys.path.append('../..')
from nyt.config import public_key

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

def get_month(year, month):
    try:
        url = f"https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={public_key}"
        res = requests.get(url)
        json_dict = json.loads(res.text)
        docs = json_dict["response"]["docs"]
    except:
        print("Requested month not in archive")
        return
    # print(docs[0].keys())
    try:
        os.mkdir(year)
    except:
        pass
    filename = f"{year}/{month_dict[month]}.json"
    # print(filename)
    # get types_of_material = "News" only
    # get document_type = "article" only
    new_docs = []
    for doc in docs:
        if doc["type_of_material"] == "News" and doc["document_type"] == "article":
            doc.pop("multimedia")
            doc.pop("_id")
            doc.pop("uri")
            new_docs.append(doc)


    with open(filename, "w") as f:
        json.dump(new_docs, f)

def get_year(year):
    # range(12) goes from 0 to 11
    for i in range(12):
        get_month(year, i+1)

def get_years(years):
    for year in years:
        get_year(year)

get_month(2021, 11)
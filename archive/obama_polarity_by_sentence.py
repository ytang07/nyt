# import libraries
import requests
import json
import matplotlib.pyplot as plt
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
def get_polarities():
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

# get_polarities()

# plot each datapoint
def plot_polarities(year):
    with open(f"obama/{year}_sentence_polarities.txt", "r") as f:
        entries = f.readlines()
    ys = []
    titles = []
    for entry in entries:
        try:
            _entry = entry.split(": ")
            ys.append(float(_entry[1]))
            titles.append(_entry[0])
        except:
            continue
    xs = list(range(len(ys)))
    high = titles[ys.index(max(ys))]
    low = titles[ys.index(min(ys))]
    print(high)
    print(low)
    plt.scatter(xs, ys)
    plt.title(f"Obama Sentiments, {year}")
    plt.xlabel("Headline Number")
    plt.ylabel("Average Polarity")
    plt.show()
    
# plot each year
for year in range(2008, 2018):
    plot_polarities(year)

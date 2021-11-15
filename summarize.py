# uncomment the two lines below to call summarizer
# from request_layer import summarize_headlines
# summarize_headlines(2021, 10)
import json

from archive import month_dict

# now let's explore our summarized content
def explore_summarized(year, month):
    filename = f"{year}/{month_dict[month]}_Summary.json"
    try:
        with open(filename, "r") as f:
            entries = json.load(f)
    except:
        raise NameError("No Such File")
    
    for entry in entries:
        new = entry.replace(" .", "")
        print(new)

explore_summarized(2021, 10)
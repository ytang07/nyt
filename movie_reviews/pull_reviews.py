import requests
import json
import sys
sys.path.append('../..')
from nyt.config import public_key

search_url = "https://api.nytimes.com/svc/movies/v2/reviews/search.json"
# define search
def search(term: str):
    params = {
        "query": term,
        "api-key": public_key
    }
    res = requests.get(search_url, params=params)
    json_res = json.loads(res.text)
    print(json_res)
    with open(f"{term}.json", "w") as f:
        json.dump(json_res, f)

search("the godfather")
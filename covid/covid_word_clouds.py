from common import text_url, parse, gather_with_concurrency, post_async
from config import thetextapikey
from word_cloud import word_cloud

def make_word_cloud(year, month):
    text = parse(year, month)
    word_cloud(text, f"wordclouds/{year}_{month}.png")
    
for year in [2020, 2021]:
    for month in range(12):
        if year == 2020 and month < 3:
            continue
        make_word_cloud(year, month+1)

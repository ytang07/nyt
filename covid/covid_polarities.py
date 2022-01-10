"""
get list of all headlines
get polarity values of each headline
get polarity values of each month based on those headlines
get mcps of each month

plot polarity of headlines over time
plot polarity of months over time
"""
import matplotlib.pyplot as plt
import asyncio
import aiohttp

from common import parse, text_url, gather_with_concurrency, post_async
from config import thetextapikey

headers = {
    "Content-Type": "application/json",
    "apikey": thetextapikey
}
polarities_url = text_url + "text_polarity"

# get the polarities asynchronously
async def get_hl_polarities(year, month):
    entries = parse(year, month)
    all_hl = entries.split("\n")
    conn = aiohttp.TCPConnector(limit=None, ttl_dns_cache=300)
    session = aiohttp.ClientSession(connector=conn)
    bodies = [{
        "text": hl
    } for hl in all_hl]
    print(len(bodies))
    # can't run too many requests concurrently, run 10 at a time
    polarities = []
    # break down the bodies into sets of 10
    if len(bodies) > 10:
        bodies_split = []
        count = 0
        split = []
        for body in bodies:
            if len(body["text"]) > 1:
                split.append(body)
                count += 1
            if count > 9:
                bodies_split.append(split)
                count = 0
                split = []
        # make sure that the last few are tacked on
        if len(split) > 0:
            bodies_split.append(split)
            count = 0
            split = []
        for splits in bodies_split:
            polarities_split = await gather_with_concurrency(len(bodies), *[post_async(polarities_url, session, headers, body) for body in splits])
            polarities += [polarity['text polarity'] for polarity in polarities_split]
    else:
        polarities = await gather_with_concurrency(len(bodies), *[post_async(polarities_url, session, headers, body) for body in bodies])
        polarities = [polarity['text polarity'] for polarity in polarities]
    await session.close()
    with open(f"polarity_graphs/{year}_{month}_values.txt", "w") as f:
        f.write(" ".join([str(polarity) for polarity in polarities]))
    return polarities

"""fix yelling at me error"""
from functools import wraps

from asyncio.proactor_events import _ProactorBasePipeTransport

def silence_event_loop_closed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RuntimeError as e:
            if str(e) != 'Event loop is closed':
                raise
    return wrapper

_ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)
"""fix yelling at me error end"""

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

# graph polarities by article 
def polarities_graphs(year, month):
    polarities = asyncio.run(get_hl_polarities(year, month))
    plt.scatter(range(len(polarities)), polarities)
    plt.title(f"Polarity of COVID Article Headlines in {month_dict[month]}, {year}")
    plt.xlabel("Article Number")
    plt.ylabel("Polarity Score")
    plt.savefig(f"polarity_graphs/{year}_{month}_polarity.png")
    plt.clf()
    print(f"{month} {year} done")
    return polarities

# graph polarities by month
def polarities_month_graphs():
    total_polarities_over_time = []
    for year in [2020, 2021]:
        month_polarities = []
        for month in range(12):
            # skip over the first three months
            if year == 2020 and month < 3:
                month_polarities.append(0)
                continue
            polarities = polarities_graphs(year, month+1)
            month_polarities.append(sum(polarities)/len(polarities))
        total_polarities_over_time += month_polarities
        plt.plot(range(len(month_polarities)), month_polarities)
        plt.title(f"Polarity of COVID Article Headlines in {year}")
        plt.xlabel("Month")
        plt.ylabel("Polarity Score")
        plt.savefig(f"polarity_graphs/{year}_polarity.png")
        plt.clf()
    # get total graph for both years
    plt.plot(range(len(total_polarities_over_time)), total_polarities_over_time)
    plt.title(f"Polarity of COVID Article Headlines so far")
    plt.xlabel("Months since January 2020")
    plt.ylabel("Polarity Score")
    plt.savefig(f"polarity_graphs/total_polarity.png")
    plt.clf()

polarities_month_graphs()
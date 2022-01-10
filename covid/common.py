import asyncio
import json
from config import thetextapikey

text_url = "https://app.thetextapi.com/text/"
headers = {
    "Content-Type": "application/json",
    "apikey": thetextapikey
}

def parse(year, month):
    with open(f"covid_headlines/{year}_{month}.txt", "r") as f:
        entries = f.read()
    return entries

# configure async requests
# configure gathering of requests
async def gather_with_concurrency(n, *tasks):
    semaphore = asyncio.Semaphore(n)
    async def sem_task(task):
        async with semaphore:
            return await task
    
    return await asyncio.gather(*(sem_task(task) for task in tasks))

# create async post function
async def post_async(url, session, headers, body):
    async with session.post(url, headers=headers, json=body) as response:
        text = await response.text()
        return json.loads(text)
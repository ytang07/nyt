import matplotlib.pyplot as plt
import json

from archive import month_dict

def get_avg(year, month, month_avgs):
    filename = f"{year}/{month_dict[month]}_Polarity.json"
    with open(filename, "r") as f:
        entries = json.load(f)
    ys = []
    for entry in entries:
        ys.append(entry[0])
    month_avgs.append(sum(ys)/len(ys))

month_avgs = []
for year in [2019, 2020, 2021]:
    for month in range(1, 13):
        if year == 2021 and month > 10:
            continue
        get_avg(year, month, month_avgs)

xs = []
ys = []
for index, month in enumerate(month_avgs):
    xs.append(index)
    ys.append(month)
plt.plot(xs, ys)
plt.xlabel("Months since Jan 2019")
plt.ylabel("Polarity Score")
plt.title(f"NY Times Avg Headline Polarity by Month")
plt.show()
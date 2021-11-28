import matplotlib.pyplot as plt
import json

from archive import month_dict
from request_layer import cc_finder

def get_avg(year, month, month_avgs):
    filename = f"{year}/{month_dict[month]}_Polarity.json"
    with open(filename, "r") as f:
        entries = json.load(f)
    ys = []
    for entry in entries:
        ys.append(entry[0])
    month_avgs.append(sum(ys)/len(ys))

def graph_avgs():
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

def graph_cc():
    years = list(range(2008, 2022))
    xs = []
    ys = []
    ys_total = []
    ys_cc = []
    months_since_2008 = 0
    for year in years:
        for i in range(1,13):
            if year == 2021 and i > 11:
                continue
            total, cc = cc_finder(year, i)
            ratio = cc/total
            xs.append(months_since_2008)
            months_since_2008 += 1
            ys.append(ratio)
            ys_total.append(total)
            ys_cc.append(cc)
        
    ratio = plt.figure(1)
    plt.plot(xs, ys)
    plt.xlabel("Months since January 2008")
    plt.ylabel("Proportion of News Headlines about Climate")
    plt.title("Climate in the News Over Time")
    plt.show()

    total = plt.figure(2)
    plt.plot(xs, ys_total)
    plt.xlabel("Months since January 2008")
    plt.ylabel("Total Number of Articles per Month")
    plt.title("Number of NY Times Articles per Month over Time")
    total.show()

    cc = plt.figure(3)
    plt.plot(xs, ys_cc)
    plt.xlabel("Months since January 2008")
    plt.ylabel("Total Number of Articles Mentioning Climate")
    plt.title("Number of NY Times Articles Mentioning Climate per Month over Time")
    cc.show()



    print(sum(ys)/len(ys))
    print(sum(ys_total)/len(ys_total))
    print(sum(ys_cc)/len(ys_cc))
    input()


graph_cc()
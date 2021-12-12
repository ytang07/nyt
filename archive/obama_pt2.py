import json

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
# get all the headlines and put them into one list
def coalesce(year, month, coalesced: list):
    filename = f"{year}/{month_dict[month]}_Obama.json"
    try:
        with open(filename, "r") as f:
            entries = json.load(f)
    except:
        raise NameError("No Such File")
    
    for entry in entries:
        for headline in entry["Obama"]:
            # take care of the entries I messed up when writing initially
            if "." in headline[:-1]:
                headlines = headline[:-1].split(".")
                for hl in headlines:
                    if "Obama" in hl:
                        coalesced.append(hl)
            else:
                coalesced.append(headline)

# obama_headlines_2017 = []
# coalesce(2017, 1, obama_headlines_2017)
# with open("obama_2017.txt", "w") as f:
#     for headline in obama_headlines_2017:
#         f.write(headline+'\n')

# get all headlines from a year
# obama_headlines_2015 = []
# for i in range(1, 13):
#     coalesce(2015, i, obama_headlines_2015)
# with open("obama_2015.txt", "w") as f:
#     for headline in obama_headlines_2015:
#         f.write(headline+'\n')

# obama_headlines_2014 = []
# for i in range(1, 13):
#     coalesce(2014, i, obama_headlines_2014)
# with open("obama_2014.txt", "w") as f:
#     for headline in obama_headlines_2014:
#         f.write(headline+'\n')

# obama_headlines_2013 = []
# for i in range(1, 13):
#     coalesce(2013, i, obama_headlines_2013)
# with open("obama_2013.txt", "w") as f:
#     for headline in obama_headlines_2013:
#         f.write(headline+'\n')

# obama_headlines_2012 = []
# for i in range(1, 13):
#     coalesce(2012, i, obama_headlines_2012)
# with open("obama_2012.txt", "w") as f:
#     for headline in obama_headlines_2012:
#         f.write(headline+'\n')

# obama_headlines_2011 = []
# for i in range(1, 13):
#     coalesce(2011, i, obama_headlines_2011)
# with open("obama_2011.txt", "w") as f:
#     for headline in obama_headlines_2011:
#         f.write(headline+'\n')

obama_headlines_2010 = []
for i in range(1, 13):
    coalesce(2010, i, obama_headlines_2010)
with open("obama_2010.txt", "w") as f:
    for headline in obama_headlines_2010:
        f.write(headline+'\n')

# obama_headlines_2009 = []
# for i in range(1, 13):
#     coalesce(2009, i, obama_headlines_2009)
# with open("obama_2009.txt", "w") as f:
#     for headline in obama_headlines_2009:
#         f.write(headline+'\n')

# obama_headlines_2008 = []
# for i in range(11, 13):
#     coalesce(2008, i, obama_headlines_2008)
# with open("obama_2008.txt", "w") as f:
#     for headline in obama_headlines_2008:
#         f.write(headline+'\n')
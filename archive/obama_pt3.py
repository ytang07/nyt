headlines = []
for i in range(2008, 2018):
    with open(f"obama_{i}.txt", "r") as f:
        x = f.readlines()
    headlines.append(x)
for hl in headlines:
    print(len(hl))
import matplotlib.pyplot as plt

headlines = []
for i in range(2008, 2018):
    with open(f"obama_{i}.txt", "r") as f:
        x = f.readlines()
    headlines.append(x)

ys = []
for hl in headlines:
    ys.append(len(hl))

xs = list(range(2008, 2018))

plt.plot(xs, ys)
plt.xlabel("Year (2008 and 2017 are only partial)")
plt.ylabel("NY Times Headlines about Obama")
plt.title("Number of Headlines about Obama during his presidency")
plt.show()
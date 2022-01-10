import matplotlib.pyplot as plt

x = list(range(24))
y = [0,0,0,6,9,13,14,32,24,63,41,62,
     57,55,79,84,89,62,91,85,86,94,94,108]

plt.plot(x, y)
plt.title("Number of COVID Headlines Over Time")
plt.ylabel("Number of COVID Headlines")
plt.xlabel("Months since January 2020")
plt.savefig("covid_headlines/count_over_time.png")
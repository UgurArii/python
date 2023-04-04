import matplotlib.pyplot as plt

x1, y1 = [1600, 1700, 1800, 1900, 2000], [0.2, 0.5, 1.1, 2.2, 7.7]
x2, y2 = [1600, 1700, 1800, 1900, 2000], [1, 1, 2, 3, 4]

plt.plot(x1, y1, "rx-", label="Actual")
plt.plot(x2, y2, "bo--", label="Fake")
plt.title("World Population Over Time")
plt.xlabel("Year")
plt.ylabel("Population (billions)")
plt.legend()
plt.show()
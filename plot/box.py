import matplotlib.pyplot as plt

males, females = [72,68,65,77,73,71,69],[60,65,68,61,63,64]

heights = [males,females]
plt.figure(figsize=(15,8))
plt.boxplot(heights)
plt.title("Height by Gender",fontsize=22)
plt.ylabel("Height(inches)", fontsize=14)
plt.xlabel("Gender", fontsize=14)
plt.show()

import matplotlib as mlp
import matplotlib.pyplot as plt
x = [50,70,90,65]
y = [129, 192, 163, 172]

plt.plot(x,y, color = "yellow")
plt.title("TITLE", color = "blue" )
plt.xlabel("Axis X", color = "purple")
plt.ylabel("Axis Y", color = "green")
plt.grid(True)
plt.legend(['Legend1'])

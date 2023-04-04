import matplotlib.pyplot as plt

num_people, categories = [4,8,3,6,2],["Comedy","Action","Thriller","Romance","Horrow"]
plt.bar(categories, num_people)
plt.title("Favorite Movie Category", fontsize=24)
plt.xlabel("Category", fontsize=16)
plt.ylabel("# of People", fontsize=16)
plt.xticks(fontname="Fantasy")
plt.yticks(fontname="Fantasy")
plt.show()
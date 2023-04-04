import matplotlib.pyplot as plt

Students = [2,4,6,8,6,10, 6] 
Courses = [4,5,3,2,4, 3, 4]

plt.scatter(Students, Courses, label='Students/Courses',
            color='green', marker='*', s=75)
plt.xlabel('Student')
plt.ylabel('Courses')
plt.title('Students courses\n Spring 2018')
plt.legend()
plt.show()

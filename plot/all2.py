import matplotlib.pyplot as plt

x =[3,6,8,11,13,14,17,19,21,24,33,37]
y = [7.5,12,13.2,15,17,22,24,37,34,38.5,42,47]
x2 =[3,6,8,11,13,14,17,19,21,24,33]
y2 = [50,45,33,24,21.5,19,14,13,10,6,3]

plt.plot(x,y, label='First Line')
plt.plot(x2,y2, label='Second Line')
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting Graph\n2018')
plt.yticks([0,5,10,15,20,25,30,35,40,45,50],['0B','5B','10B','15B','20B','25B','30B','35B','40B','45B','50B'])
plt.legend()
plt.show()

Students = [2,4,6,8,10]
Courses = [4,5,3,2,1]
stds = [3,5,7,9,11]
Projects = [1,2,4,3,2]
plt.bar(Students, Courses, label="Students/Courses", color='r')
plt.bar(stds, Projects, label="Projects", color='c')
plt.xlabel('Students')
plt.ylabel('Courses')
plt.title('Students-Courses Data\n2018')
plt.legend()
plt.show()


Ages = [ 22.5, 10, 55, 8, 62, 45, 21, 34, 42, 45, 99,
75, 82,
        77, 55, 43, 66, 66, 78, 89, 101, 34, 65, 56,
25, 34,
                52, 25, 63, 37, 32]
binsx = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

plt.hist(Ages, bins=binsx, histtype='bar', rwidth=0.7)

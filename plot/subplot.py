import matplotlib as mlp
import matplotlib.pyplot as plt

plt.plot([1,2,3,4],[1,4,8,15], 'b*')
plt.plot([1,3,5,7],[1,4,8,12], 'g^')
plt.plot([1,2,3,5],[2,5,4,12], 'ro')
plt.legend(['First', 'Second', 'Third'], loc=0)

plt.subplot(2,2,1)
plt.plot([1,2,3,4],[1,4,8,15],'b*')

plt.subplot(2,2,2)
plt.plot([1,2,3,4],[1,4,8,12],'g^')

plt.subplot(2,2,3)
plt.plot([1,2,3,5],[2,5,4,12],'ro')

plt.subplot(2,2,4)
plt.plot([1,2,3,5],[2,5,4,12],'b')


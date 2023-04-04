import numpy as np
import matplotlib.pyplot as plt
data = np.random.randn(2, 3)
print(data)

print(data * 10)
print(data + data)
print(data.shape, '-' , data.dtype)

points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)

print(ys)

z = np.sqrt(xs ** 2 + ys ** 2)
print(z)

plt.imshow(z, cmap = plt.cm.gray)
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

result = [(x if c else y)
          for x,y,c in zip(xarr, yarr, cond)]

print(result)

result = np.where(cond, xarr, yarr)
print(result)

arr = np.random.randn(100)
print((arr>0).sum())
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names))
values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2,4,7]))

from numpy.linalg import inv, qr
X = np.random.randn(5,5)
mat = X.T.dot(X)
print(inv(mat))

print(mat.dot(inv(mat)))

q, r = qr(mat)
print(r)

































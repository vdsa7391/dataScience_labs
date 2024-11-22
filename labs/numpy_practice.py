import numpy as np

x= np.array([[1,2,3],[4,5,6],[7,8,9]])
view=x[:,:2]
view[:,:2]=0
print(x)

y = np.array([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]])
z=np.array([True, False, True])
print(z.shape)
print(y[z])
print(y[1:])
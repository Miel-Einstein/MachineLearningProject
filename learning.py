import  numpy as np

A=np.array([[1,2],[3,4],[5,6]])
print(A.shape)
B=A.T
print(B.shape)
Q=np.ones((3,2))
print(Q)
print(A+Q)
print(A.dot(Q.T))
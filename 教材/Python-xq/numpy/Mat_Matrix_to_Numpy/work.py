
import numpy as np
import pandas
import scipy.io as sio
#imported to save the numpy file
from tempfile import TemporaryFile
outfile = TemporaryFile()
x = np.linspace(0, 2 * np.pi, 100)
y = np.cos(x)
#Try to make a copy of the file SMALL.mat before using it here.
#Converted to a dictionary with x and y key names
sio.savemat('~/Downloads/numpy/RAHULw/SMALL.mat', dict(x=x, y=y))
#Now load it and print it , the value of key x and y is our matrix which we will convert to numpy array
m=sio.loadmat('~/Downloads/numpy/RAHULw/SMALL.mat')
a=np.array([m['y'],m['x']])
#the below line prints our desired array, we can use load and save python method to save the array in a file,in below codes which are 
#commented i have tried to split them and then save them
print(a)
with open(r'~/Downloads/numpy/Mat_Matrix_to_Numpy/final.txt', 'w') as f:
    f.write(" ".join(map(str, a)))
#Now a is our required numpy array data
#The below code saves the array first as a binary file and then as a file you can open in a regular text editor, you can uncomment below lines to see it
'''
nx,ny,nz=np.shape(a)
CXY=np.zeros([ny, nx])
for i in range(ny):
    for j in range(nx):
        CXY[i,j]=np.max(a[j,i,:])

#Binary data
np.save('/home/xq/Downloads/numpy/RAHULw/savedfiles/ab.npy', CXY)

#Human readable data
np.savetxt('/home/xq/Downloads/numpy/RAHULw/savedfiles/ab.txt', CXY)

'''


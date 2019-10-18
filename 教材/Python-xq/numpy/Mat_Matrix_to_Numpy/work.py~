
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
sio.savemat('/home/animesh/Documents/RAHULw/SMALL.mat', dict(x=x, y=y))
#Now load it and print it , the value of key x and y is our matrix which we will convert to numpy array
m=sio.loadmat('/home/animesh/Documents/RAHULw/SMALL.mat')
a=np.array([m['y'],m['x']])
#Now a is our required numpy array data
#The below code saves the array first as a binary file and then as a file you can open in a regular text editor, you can uncomment below lines to see it
'''
nx,ny,nz=np.shape(a)
CXY=np.zeros([ny, nx])
for i in range(ny):
    for j in range(nx):
        CXY[i,j]=np.max(a[j,i,:])

#Binary data
np.save('/home/animesh/Documents/RAHULw/savedfiles/ab.npy', CXY)

#Human readable data
np.savetxt('/home/animesh/Documents/RAHULw/savedfiles/ab.txt', CXY)

'''


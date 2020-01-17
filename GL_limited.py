########################################
#
# GL Limited and Causal
#Dy[x-1]
#
########################################

import numpy as np 
import matplotlib.pyplot as plt 

alpha=1
x=np.arange(100)
y=x
memory=9
dy=np.zeros(len(x))

def shift5(arr, num, fill_value=np.nan):
    result = np.empty_like(arr)
    if num > 0:
        result[:num] = fill_value
        result[num:] = arr[:-num]
    elif num < 0:
        result[num:] = fill_value
        result[:num] = arr[-num:]
    else:
        result[:] = arr
    return result

y_shifted=shift5(y,1,0)
print(y_shifted)
#print("y_shifted:", y_shifted.shape)
#print("y_shifted:", y_shifted[::-1])
#print("y_shifted:", y_shifted[::-1])
#print("***********")
#for i in range(0,memory):
#    print("y_shifted:", y_shifted[i::-1])
#for i in range(memory,len(y_shifted)):
#    print("y_shifted:", y_shifted[i:i-memory:-1])



w=np.zeros(memory)
w[0]=1
h=x[1]-x[0]

for i in range (1,memory):
    c=1-((alpha+1)/i)
    w[i]=np.multiply(c,w[i-1])

print("w",w)
for i in range (len(y_shifted)):
    a=w*h**alpha
    if i<memory:
        #print("y_shifted:", y_shifted[i::-1])
        #print("w:", w[:i+1:1])
        #print("a:", a[:i+1:1])
        #k=a[:i+1:1]
        dy[i]=a[:i+1:1].dot(y_shifted[i::-1])
    else:
        #print("y_shifted:", y_shifted[i:i-memory:-1])
        #print("w:", w)
        dy[i]=a.dot(y_shifted[i:i-memory:-1])

print("dy",dy)
    


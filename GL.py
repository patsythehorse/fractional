import numpy as np 
import matplotlib.pyplot as plt 

order=np.array([0.15,0.3,0.45])
x=np.arange(100)
H=np.zeros((len(order),len(x)))
y=np.sin(x)


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
y_shifted=shift5(y,1)


for alpha in range(len(order)):
    w=np.zeros(len(x))
    w[0]=1
    h=x[1]-x[0]

    for i in range (1,len(x)):
        c=1-((order[alpha]+1)/i)
        w[i]=np.multiply(c,w[i-1])
    

    #print(w)

    for i in range (1,len(x)):
        a=w[0:i]*h**alpha
        #c=y[0:i]
        c=y_shifted[i:0:-1]
        H[alpha,i]=a.dot(c)
        #y[i]=(w[1:i],y[i:0:-1]*h**alpha)


print(H)

H_transpose=H.transpose()
g=np.matmul(np.matmul(np.linalg.inv(np.matmul(H,H_transpose)),H),y.reshape(-1,1))
#print('g')
#print(g.shape)
#print(g)
g_transpose=g.reshape(1,-1)
print("g", g_transpose.shape)
pred_y=np.matmul(g_transpose,H)

print(x)
print(y)
print(pred_y)


plt.plot(x,y)
plt.plot(x,pred_y.reshape(-1,))
plt.plot(x,pred_y.reshape(-1,)-y)
plt.show()
'''
print(y)
print(H)
print('w')
print(w)
print(w.reshape(-1,1))
print(np.outer(w,w))

plt.plot(x,y)
plt.plot(x,H)
#plt.plot(x,np.cos(x))

plt.show()

'''
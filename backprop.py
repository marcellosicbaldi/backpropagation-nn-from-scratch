import numpy as np
import matplotlib.pyplot as plt

#defining the activation function
def sigmoid(x): 
    return 1 / (1 + np.exp(-x))

def sigmoid_der(x):
    return (sigmoid(x) * (1-sigmoid(x)))

# initializing parameters
dim = [1, 12, 1] 
l = len(dim) # number of layers 
lr = 2 # learning rate

w,b = [],[]

for i in range(1,l):
    w.append(np.random.rand(dim[i-1],dim[i]))
    b.append(np.random.rand(dim[i]))

z,a,d=[],[],[] 

for i in range(0,l): 
    a.append(np.zeros(dim[i]))

for i in range(1,l):
    z.append(np.zeros(dim[i]))
    d.append(np.zeros(dim[i]))

#training
def update(x,y): 
    #input                
    a[0] = x 
    #feed forward
    for i in range(0,l-1): 
        z[i] = np.dot(a[i],w[i])+b[i]
        a[i+1] = np.vectorize(sigmoid)(z[i]) 
    # output error
    d[l-2] = (y - a[l-1])*np.vectorize(sigmoid_der)(z[l-2]) 
    # back propagation
    for i in range(l-3,-1,-1): # 
        d[i]=np.dot(w[i+1],d[i+1])*np.vectorize(sigmoid_der)(z[i]) 
    # updating
    for i in range(0,l-1): 
        for k in range (0,dim[i+1]): 
            for j in range (0,dim[i]): 
                w[i][j,k] = w[i][j,k] + lr*a[i][j]*d[i][k]
                b[i][k] = b[i][k] + lr*d[i][k]   
    return np.sum((y-a[l-1])**2)

def epoch(X):
    e = 0
    for i in range(len(X)):
        e = e + update([X[i]],[Y[i]])
    return e

# training data
def f(x):
    return (np.sin(x)**2 + np.cos(x)/3 + 1)/8

X = np.arange(-3,3,0.125)
Y = np.zeros(len(X))
for i in range(0,48):
    Y[i] = f(X[i])

n_iter = 3000
for i in range(1, n_iter+1): # until the error is small
    dist = epoch(X)
    if i == 20:
        print ("Cost after iteration %i: %f" %(i, dist))
    if i % 600 == 0:
        print ("Cost after iteration %i: %f" %(i, dist))

#predict
y_pred = np.zeros(48)

def forward_prop(X, j):
    a[0] = X[j]
    for i in range(0,l-2):
        z[i] = np.dot(a[i],w[i])+b[i]
        a[i+1] = np.vectorize(sigmoid)(z[i])
    z[l-2] = np.dot(a[l-2],w[l-2])+b[l-2]
    a[l-1] = np.vectorize(sigmoid)(z[l-2])
    return a[l-1]
#def predictt(X):
#    for j in range(len(X)):

def predict(X):
    for j in range(len(X)):
        y_pred[j] = forward_prop(X, j)
    return y_pred

plt.plot(X, Y,'r', linewidth = '2.8')

plt.plot(X, predict(X), 'b')




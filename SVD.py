import numpy as np
#import random

def SVD(mat, initial_vec1, initial_vec2, learn_rate, iterations):
    ## reassigning vectors in order to keep code clean
    # the matrix that we want to approximate
    A = mat
    # two vectors from which we will start
    b = initial_vec1
    c = initial_vec2
    # learning rate, or step of learning
    alpha = learn_rate
    # number of iterations
    n = iterations
    # A ~ b * c^t : the first approximation based on given initial vectors
    A_app = np.dot(b, c.T)
    # loop
    for i in range(n):
        # partial derivatives for vectors
        dLdb = np.dot((A_app - A), c)
        dLdc = np.dot((A_app - A).T, b)
        # updating vectors
        c = c - alpha * dLdc
        b = b - alpha * dLdb
        # calculating approximated matrix
        A_app = np.dot(b, c.T)
    # returning two vectors that can be used for A approximation
    return b, c, A_app
### end


## examples of implimentation

alpha = 0.001
n = 100


## with numpy arrays example
A = np.array([[3, 1, 1], [-1, 3, 1], [1, 2, 3]])
b = np.array([[1], [-11], [2]])
c = np.array([[-22], [-22], [-2]])

temp = SVD(mat = A, initial_vec1 = b, initial_vec2 = c, learn_rate = alpha, 
           iterations = n)

## with list example
#A_helper = [[random.random() for x in range(100) ] for y in range(100)]
#a0_helper = [[random.random() for x in range(3) ] for y in range(100)]
#a1_helper = [[random.random() for x in range(3) ] for y in range(100)]
#
#temp = SVD(mat = A_helper, initial_vec1 = np.array(a0_helper), 
#initial_vec2 = np.array(a1_helper), learn_rate = alpha, iterations = n)
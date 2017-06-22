from matplotlib import pyplot as plt
import math



def vector_add(v1, v2):
    # Adds vector 1 and vector 2
    return [v1_i + v2_i
            for v1_i, v2_i in zip(v1,v2)]
def vector_subtract(v,w): 
    # Subtracts corresponding elements
    return [v_i - w_i 
            for v_i, w_i in zip(v,w)]

""" x = [1,2]
y = [2,1]
vectors = zip(x,y) # print(vectors): <zip at 0x18022066388> 
print("vectors: ", list(vectors)) # list(vectors): [(1,2), (2,1)] 
plt.title('Adding Two Vectors') 
plt.xlabel('x')
plt.ylabel('y')
vector1 = plt.quiver(1, 2, color='red')
vector2 = plt.quiver(2,1, color='blue')


plt.show() """

def vector_sum(vectors): 
    """ Sums all corresponding elements """ 
    result = vectors[0] # start at the first vector of the argument
    # I think [1:] = slice from 1 to end
    for vector in vectors[1:]: # Loop over the rest of the array
        result = vector_add(result,vector) # Use vector_add to add to the result
    return result

""" 
With higher order functions
def vector_sum(vectors): 
    return reduce(vector_add, vectors)
"""

def scalar_multiply(c,v): 
    """ c = number; v = vector """
    return [c * v_i for v_i in v] 

def vector_mean(vectors):
    """ compute the vector whose ith element is the mean of the ith element of the input vectors """
    n = len(vectors) # See how many there are
    return scalar_multiply(1/n, vector_sum(vectors))
                          
def dot_product(v,w):
    """ v_1 * w_1 + ... + v_n * w_n """
    return sum(v_i * w_i 
               for v_i, w_i in zip(v,w))
    
    
def sum_of_squares(v):
    """ v_1*v_1 + ... + v_n*v_n """
    return dot_product(v,v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v)) # Use the built in square root function


""" Distance between two vectors: sqrt((v1-w1)^2 + ... + (v_n - w_n)^2) """

def squared_distance(v,w): 
    """ (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2 """
    return sum_of_squares(vector_subtract(v,w))

def distance(v,w):
    return math.sqrt(squared_distance(v,w))

""" 
Equivalent to 
    distance(v,w):
        return magnitude(vector_subtract(v,w)) 
"""
    

    
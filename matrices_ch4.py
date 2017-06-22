A = [[1,2,3],
     [4,5,6]]
# A has 2 rows and 3 columns

B = [[1,2], 
     [3,4], 
     [5,6]]
# B has 3 rows and 2 columns

# Let shape be the len(A) rows and len(A[0]) columns

def shape(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0 # number of elements in the first row
    return num_rows, num_cols


def get_row(matrix, i): 
    return matrix[i]

def get_column(matrix, j):
    return [ matrix_i[j] 
            for matrix_i in matrix]
    
def make_matrix(num_rows, num,cols, entry_fn):
    # returns a num_rows x num_cols matrix
    # whose (i,j) entry is entry_fn(i,j)
    return [[
            entry_fn(i,j) # given i, create a list
            for j in range(num_cols)]
        for i in range(num_rows)]

def is_diagonal(i,j):
    """ 
    the diagonal values are all the same,
    e.g. identity matrix
    1 = true; 0 = false;
    
    """
    return 1 if i==j else 0
    
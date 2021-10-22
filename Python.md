# Introduction to python programming
The focus is not efficiency in terms of timing or space, but rather developing the logic correctly

## Matrix Problems
Zero based indexing
- Check the dimension of matrix
```
def dim_equal(A):
  return len(A) == len(A[0]
```
- Validate dimension for addition or subtraction of two matrices
```
def add_subtract_dim(A,B):
  if len(A) != len(B) or len(A[0]) != len(B[0]):
    return False
  return True
```
- Adding or subtracting two matrices
```
def add_mat(A,B):
  C = []
  if add_subtract_dim(A,B):
    for i in range(len(A)):
      C.append([])
      for j in range(len(B)):
        # To subtract replace the "+" with "-"
        C[i].append(A[i][j] + B[i][j])
   
  return C
```
- Validate dimension of matrices for multiplication
```
def multiply_validate(A,B):
  """The order of arguments is important"""
  if len(A[0]) != len(B)
    return False
  return True
```
- Multiply two matrices (incomplete)
```
def multiply(A,B):
  if multiply_validate(A,B):
    C = []
    for i in range(len(A)):
    C.append([])
      for j in range(len(B[0]):
        for k in range(len(A[0]):
          sum = sum + A[i][j]*B[j][i]
          if k == len(A[0])
            C[i].append(sum)
        sum = 0
    return C
```
- Find the determinant of a matrix with two rows and two columns
```
def determinant_2*2(A):
  if dim_equal(A):
    return(A[0][0]*A[1][1] - A[0][1]*A[1][0])
  return "Incorrect Dimensions"
```
[Minors and Cofactors](https://en.wikipedia.org/wiki/Minor_(linear_algebra))
- Restricting to matrices of three rows and three columns
```
def square_dim_three(A):
  if len(A) != 3 or len(A[0]) != 3:
    return False
  return True
```
- Minors
```
def minors(A,i,j):
  """Takes three arguments matrix A and the corresponding row and column to find the cofactor"""
  if square_dim_three(A):
    C = []
      for k in range(len(A)):
        C.append([])
        for l in range(len(A[0])):
        # Whenever either cofactor index i or j occurs skip appending
          if k == i or l == j:
            continue
          else:
            C[k].append(A[k][l])
  
  #Removing the empty lists
  C.remove([])
  
  return determinant_2*2(C)
```
- Cofactors
```
def cofactors(A):
  """Limited to matrices of 3*3 dimensions"""
  if not equal_dim(A) or len(A) != 3:
    return "A is not a 3*3 matrix or does not have equal dimension"
  C = []
  for i in range(len(A)):
  C.append([])
    for j in range(len(A[0])):
      c = ((-1)**(i+j))*minors(A,i,j)
      C[i].append(C)
  
  return C
  ```
- Find the determinant of a matrix with three rows and three columns (incomplete)
```
def determinant_3*3(A):
  if determinant_validate(A):
  sum = 0
    for i in range(len(A)):
      for j in range(len(A)):
        sum = sum + (-1)**(i+j) * minor(A,i,j)
  
  return sum
```
- Transpose(M):
```
def transpose(M):
  T = []
  for i range(len(M[0])):
    T.append([])
  
  for i in range(len(M)):
    for j in range(len(M[0]):
      T[j].append(M[i][j])
  
  return T
```
Some common types of matrices
- Identity Matrix
```
def identity(A):
  for i in range(len(A)):
    if A[i][i] != 1:
      return False
  return True
```
- Scalar Matrix
```
def scalar(A):
  scal = A[0][0]
  for i in range(len(A)):
    if A[i][i] != scal:
      return False
  return True
```
- Diagonal Matrix
```
def diagonal(A):
  for i in range(len(A)):
    for j in range(len(A[0])):
      if i != j and A[i][j] != 0:
        return False
  return True
```
[Linear Aljebra](https://en.wikipedia.org/wiki/Linear_algebra)
- [Row Echelon](https://en.wikipedia.org/wiki/Row_echelon_form) (incomplete)
```
def row_echelon(A):
  l = []
  for i in range(len(A)):
    for j in range(len(A[0]):
      if A[i][j] == 1:
        l.append([i,j])
        continue
```
- Checking the dimension of two one dimensional array  
Example A = [1, 2, 3, 4] and B = [5, 6, 7, 8] have equal dimension whereas C = [1,2] and A (as defined) do not!
```
def one_dim_vectors(A, B):
  return len(A) == len(B)
```
- Linearly Dependent
```
def lin_depdent(A,B):
  C = []
  if one_dim_vectors(A, B):
    for i in range(len[A]):
      C.append(A[i]/B[i])
    
    for j in range(len(C)-1):
      if C[j] != C[j+1]:
      return False
  return True
```
- Linearly Dependent Set
```
def linearly_dependent_set(A):
  """ A is a list of lists"""
```

## Math Problems

## Collection (Changing from one type to another)

## Miscellaneous
- Given a list of integers create a new sorted list using slicing

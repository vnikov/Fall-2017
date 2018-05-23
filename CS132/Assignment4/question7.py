def matrixMul(A, B):
    '''Returns the multiplication of matrix A and B.
    If the Matrix A and B cannot be multiplied, return back suitable
    error message'''
    if len(A[0]) != len(B):
        return 'The dimension of A and B are not suitable for multiplication.'
    else:
        C = []
        for cb in range(len(B[0])):
            rowB = []
            for rb in range(len(B)):  # Extract the column of B
                rowB += [B[rb][cb]]
            Ctmp = []
            for ra in range(len(A)):
                elem = 0
                for ca in range(len(A[0])):
                    elem += A[ra][ca] * rowB[ca] # Do the multiplication one by one
                Ctmp += [elem]
            C += [Ctmp]
    return matrixT(C)

def matrixT(A):
    '''Returns the Transpose of the Matrix A'''
    if A == [] or (len(A) == 1 and len(A[0]) == 1):
        return A
    else:
        origCol = len(A[0])
        origRow = len(A)
        B = []
        for ca in range(origCol):
            tmpB = []
            for ra in range(origRow):
                tmpB += [A[ra][ca]]
            B += [tmpB]
        return B

def matrixAdd(A, B):
    ''' Returns the addition of Matrix A and B.
    If the Matrix A and B cannot be added, return back
    suitable error message '''
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return 'The dimension of A and B are not matched.'
    else:
        C = []
        for ra in range(len(A)):
            tmpC = []
            for ca in range(len(A[0])):
                elem = A[ra][ca] + B[ra][ca]
                tmpC += [elem]
            C += [tmpC]
        return C

def test():
    A = [[1, 3, 5], [2, 4, 7], [1, 1, 0]]
    B = [[1, 2, 6], [2, 4, 7], [1, 1, 8]]
    print matrixT(A)  #This prints back the transpose of A
    print matrixMul(A,B) #This prints back the multiplication of A and B
    print matrixAdd(A,B) #This prints back the addition of A and B

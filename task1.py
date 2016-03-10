import numpy as np
#Your optional code here
#You can import some modules or create additional functions
ITERATION_LIMIT = 10

def LU_decomp(A):
       n=len(A)
       for k in range(0, n-1):
        for i in range(k+1, n):
            if A[i,k]!= 0.0:
                lam = A[i,k] / A[k,k]
                A[i, k+1:n] = A[i, k+1:n] - lam * A[k, k+1:n]
                A[i, k] = lam
        return A

def lu(A,b):
      A=LU_decomp(A)
      n = len(A)
      for k in range(1,n):
           b[k] = b[k] - np.dot(A[k,0:k], b[0:k])
           b[n-1]=b[n-1]/A[n-1, n-1]
      for k in range(n-2, -1, -1):
           b[k] = (b[k] - np.dot(A[k,k+1:n], b[k+1:n]))/A[k,k]
      return b
      

def sor(A, b):
    sol = []
    # Edit here to implement your code
    #A = D-L-U
    D = [[0 for x in range (0,n)] for x in range (0,n)]
    L = [[0 for x in range (0,n)] for x in range (0,n)]
    U = [[0 for x in range (0,n)] for x in range (0,n)]
    invD = [[0 for x in range (0,n)] for x in range (0,n)]
    T = [[0 for x in range (0,n)] for x in range (0,n)]
   
    #compute diagonal matrix D
    for i in range (0, n):
        D[i][i] = A[i][i]
    
    #compute lower triangular matrix L    
    for i in range (1, n):
        for j in range (0, i):
            L[i][j] = -A[i][j]
    
    #compute upper triangular U        
    for i in range (0, n):
        for j in range(i+1, n):
            U[i][j] = -A[i][j]
    
    #compute inverse matrix of D, named invD
    for i in range (0, n):
        invD[i][i] = 1/D[i][i]
    
    #compute matrix T, where T = invD * (L + U)
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                T[i][j] += invD[i][k]*(L[k][j] + U[k][j])
                
    #compute the spectral radius of matrix T, named pT, where pT = max(all eigenvalues)
    pT = max(abs(np.linalg.eigvals(T)))
    
    #compute optimal omega for SOR method
    omega = 2*(1 - np.sqrt(1 - ((pT)**2)))/((pT)**2)

    x = np.zeros_like(b)
    for itr in range(ITERATION_LIMIT):
        for j in range(len(b)):
            sums = np.dot( A[j,:], x )
            x[j] = x[j] + omega*(b[j]-sums)/A[j,j]

    return list(sol)

def solve(A, b):
    condition = True # State and implement your condition here
    condition = False
    try:       
        np.linalg.cholesky(A)
    except np.linalg.linalg.LinAlgError :
        condition = True    
    if condition:
        print('Solve by lu(A,b)')
        return lu(A,b)
    else:
        print('Solve by sor(A,b)') 
        return sor(A,b)

if __name__ == "__main__":
    ## import checker
    ## checker.test(lu, sor, solve)

    A = np.array([[2,1,6], [8,3,2], [1,5,1]]).astype(float)
    b = np.array([9, 13, 7]).astype(float)
    n = len(A)
    sol = np.linalg.solve(A,b)
    solve(A,b)
    print(sol)
    
    A = np.array([[6566, -5202, -4040, -5224, 1420, 6229],
         [4104, 7449, -2518, -4588,-8841, 4040],
         [5266,-4008,6803, -4702, 1240, 5060],
         [-9306, 7213,5723, 7961, -1981,-8834],
         [-3782, 3840, 2464, -8389, 9781,-3334],
         [-6903, 5610, 4306, 5548, -1380, 3539.]]).astype(float)
    b = np.array([ 17603,  -63286,   56563,  -26523.5, 103396.5, -27906]).astype(float)
    n=len(A)  
    sol = np.linalg.solve(A,b)
    solve(A,b)
    print(sol)
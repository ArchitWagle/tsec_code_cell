import numpy as np

M = ([[0,0,1],[1,0,1],[0,1,1]])
X = M.copy()



def matmul1333(a,b):
    c=[[0,0,0]]
    for i in range(1):
        for j in range(3):
            for k in range(3):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j])#%1000000007
    return c

def matmul3333(a,b):
    c=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j])
    return c

i=0
def matr_pow(n):
    global M
    
    if(n==1 ):
        return;
    #print(M)
    matr_pow(int(n/2))
    M =(matmul3333(M,M))
    if(n%2!=0):
        M =matmul3333(M,X)
    return M
def h(n):
    global i
    print(i)
    i=i+1

    global M
    M =  M = ([[0,0,1],[1,0,1],[0,1,1]])
    
    V = [[1,1,2 ]]
    exp = matr_pow(n-2)#,1000000007)
    r = (matmul1333(V,exp))
    #print([i%1000000007 for i in r[0]])
    return((r)[0][2])
print((h(10)+h(100)+h(1000000)+h(1000000000)+h(12345654321)+h(9999999999999999))%1000000007)

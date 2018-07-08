 import numpy as np
  2 
  3 M = np.mat([[0,0,1],[1,0,1],[0,1,1]])
  4 X = M
  5 def matr_pow(n):
  6     global M
  7     if(n==1 ):
  8         return;
  9     #print(M)
 10     matr_pow(int(n/2))
 11     M =np.mod(np.matmul(M,M),(1000000007))
 12     if(n%2!=0):
 13         M =np.matmul(M,X)
 14     return M
 15 def h(n):
 16     global m
 17     V = np.mat([[1,1,2 ]])
 18     exp = matr_pow(n-2)#,1000000007)
 19     return(np.matmul(V,exp)[0,2])
 20 print((h(10)+h(100)+h(1000000)+h(1000000000)+h(12345654321)+h(9999999999999999))%1000000007)
~                                                                                                                                                                                                                                            
~                                                                                                                                                                                                                                            
~                                                                                                                                                                                                                                            
~                                                                                                                                                                                                                                            
~                                                                                                                                                                                                                                            
~                                                                                                                                                                                                                                            
~                                                                                                                                                                                                                                            
~                                                                                                                                                                                                                                            
~                                                                                            

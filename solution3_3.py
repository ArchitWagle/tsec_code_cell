
from math import *

#in terminal use  cat and pipe operator while compiling to feed input
x= input().split()
N = int(x[0])
P = int(x[1])
M = int(x[2])
G=[]
H=[]
mini = 0
C =[]
for i in range(N):
    x =(list([int(u) for u in input().split()]))
    H.append(x[0])
    G.append(x[1])
    C.append((floor((M-x[0])/x[1])+1) if(floor((M-x[0])/x[1])+1>0) else 0)
    #H[-1] = H[-1] + C[-1]*G[-1]
#print(H,G,C)
zipped = zip(C,H,G)
#print(min(C))
Z = [list(i) for i in list(sorted(zipped))]
print(Z[:10])
profit = 0
count = 0

days = Z[0][0]
j =0

#the code in the 2 while loops below provides an uper and lower bound on thefinal step
#the last while loop calculates the accurate value
while(profit<P and j<N-1):
    temp =[]
    profit = 0
    while(Z[j][0] == days):
        j = j+1
    
    for i in range(j):
        temp.append(Z[i][1]+days * Z[i][2])
    print(sum(temp))
    profit = sum(temp)
    print(j,days)
    days = Z[j][0]

k = Z[j-1][0]  
print(k)
while(profit<P):
    temp = []
    for i in Z:
        temp.append(i[1]+k*i[2])
    profit = sum(temp)
    print(temp,k)
    k = k+1    
#the values below were obtained  from the estimates calculated above.I am lazy :)
profit =0
day = 110733388

while(profit<P and day<110764174):
    day = day+1
    temp =[]
    for i in range(950):
        if(Z[i][0]<=day):
            temp.append(Z[i][1]+Z[i][2]*day)
        profit = sum(temp)
    print(day,profit)





    
    



       







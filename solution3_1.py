def group(x):
    j ={}
    for i in x:
        j[i] = j.get(i,0)+1
    print(j)
    size =0
    for k in j:
        sizen = j[k]
        if(k+1 in j):
            sizen = sizen+j[k+1]
                
        if(k-1 in j):
            sizen = sizen+j[k-1]
        if(size<sizen):
            size = sizen
    print(size)



group([66, 68 ,67 ,67 ,61 ,66 ,67 ,120, 120 ,120 ,65 ,120 ,118,61,116,66,61])


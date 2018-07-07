
def sally(s):
    k=[]
    count = 0
    #k.append(s[0])
    for i in s:
        print (i,k)
        if(len(k)==0):
            k.append(i)
        elif(k[-1]==i):
            count = count+1
            k.pop()
        else:
            k.append(i)
#        print(i,k)
    return (count)     

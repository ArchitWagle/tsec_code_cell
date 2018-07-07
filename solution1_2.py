

def sally(s):
    k=[]
    count = 0
    k.append(s[0])
    for i in s[1:]:
        if(k[-1]==i):
            count = count+1
            k.pop()
        else:
            k.append(i)
    return (count)        
    

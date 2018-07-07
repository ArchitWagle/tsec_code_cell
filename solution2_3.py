def bus(n,s):
    bus = 0
    count = 1
    for i in s:
            
        if(bus+i>n ):
            bus = 0
            
            count =count+1
        
        bus = bus+i
            
    return count
    
print(bus(5,[4])+bus(4,[1,3,2,3,4,1])+bus(8,[6,1,1,1,4,5])+bus(10,[1,10,1,10,1,1,7,8,6,7])+bus(1,[1,1,1,1,1,1,1,1,1,1])+bus(2,[2,2,1,1,1,1,1,2,1,2])+bus(100,[14,67,15,28,21])+bus(100,[14,67,19,2,99,1,99])+bus(1,[1,1,1,1,1]))



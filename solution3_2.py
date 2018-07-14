n =4

x =[0]*(n+1)
count =0
def place(k,i):
	for j in range(1,k):
		if(x[j]== i or i-x[j] == k -j):
			return False
	return True
	

def nqueen(k):
	global count
	global x
	global n
	for i in range(1,n+1):
		
		if(place(k,i)):
			x[k] = i
			
			if(k==n):
				print(x)
				count = count+1
				
			else:
				nqueen(k+1)
				




nqueen(1)

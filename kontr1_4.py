A=[0]*100
i=0
n=int(input())
for i in range(97):
    A[0] = 0
    A[1] = 0
    A[2] = 1
    A[i+3]=A[i]+A[i+1]+A[i+2]
    if A[i] > n:
        print(i)
        break    
    else: 
        i+=1



            





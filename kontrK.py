N = int(input())
A=[0]*2*N
B = [0]*N
top=0
m = 0
i=0
for top in range(len(A)):
    A[top] = int(input())
    top += 1
    i+=1
    if i == 2:
        B[m] = int(input())
        m += 1
        i = 0
M = int(input())
C = [0]*M
i = 0
for i in range (M):
    x = int(input())
    m1= int((len(A)/2)-1)
    for i1 in range(len(A)-1, -1, -2):
        if A[i1] > x > A[i1-1]:
            C[i] = B[m1]
            break
        m1-=1
for i in range (len(C)):
    print(C[i],end = ' ')









            





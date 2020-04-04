N = int(input())
A=[0]*N
M = [0]+[0]*(N-1)
m = 0
for i in range (N):
    A[i] = int(input())
if N==0 or N==1:
    print (0)
else:
    M[1] = abs(A[1] - A[0])
    for i in range (2, N):
        E1 = abs(A[i]-A[i-1])
        E2 = abs(3*(A[i]-A[i-2]))
        if E1+M[i-1] < E2+M[i-2]:
            M[i] = E1+M[i-1]
        else:
            M[i] = E2+M[i-2]
    print(M[N-1])


            





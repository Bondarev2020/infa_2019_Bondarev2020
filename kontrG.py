n = int(input())
A=[0]*n
B=[0]*n
top=0
s=0
x=0
i=0
while top<n:
    x = int(input())
    A[top]=x
    top+=1
for x in range (n):
    for i in range(n):
        if A[x] == A[i]:
            B[x]+=1
    i+=1
x+=1
for i in range(n):
    if B[i]==max(B):
        break
print(A[i])




            





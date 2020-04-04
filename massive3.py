n= int(input())
A=[0]*n
B=[0]*n
top=0
s=0
while  top<=n-1:
    x = int(input())
    A[top]=x
    if A[top]==1:
        s+=1
        B[top]=s
    else:
        s=0
    top+=1

print(max(B))



            





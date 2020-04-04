A=[0]*1000000
top=0
x = int(input())
m=0
while  x!=0:
    A[top]=x
    if m<A[top]:
        m=A[top]
    top+=1
    x = int(input())
print(m)

            





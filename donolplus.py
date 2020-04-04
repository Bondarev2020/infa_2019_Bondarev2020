A=[0]*1000
top=0
x = int(input())
s=0
while  x!=0:
    A[top]=x
    s+=A[top]
    top+=1
    x = int(input())
print(s)

            





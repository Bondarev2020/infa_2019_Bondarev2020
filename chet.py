A = []
top=0
x = int(input())
s=0
while  x!=0:
    A[top]=x
    if A[top]%2==0:
        s+=1
    top+=1
    x = int(input())
print(s)

            





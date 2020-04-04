A=[0]*100000
top=0
x = int(input())
s=0
m=0
while  x!=0:
    A[top] = x
    if A[top]%2 == 0:
        if A[top]>m:
            m=A[top]
    top+=1
    x = int(input())
print(m)



            





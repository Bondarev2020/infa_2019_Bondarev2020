A=[0]*10000
top=0
x = int(input())
m=0
s=0
while  x!=0:
    A[top]=x
    if m<A[top]:
        m=A[top]
    top+=1
    x = int(input())
print(m)
for k in range (top):
    if A[k]==m:
        s+=1
print(s)

            





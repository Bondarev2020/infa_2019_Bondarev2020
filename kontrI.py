A=[0]*6
top=0
x = int(input())
m = 0
while  x!=0:
    for top in range(6):
        A[top]=x
        top+=1
        x = int(input())
    if x == 0:
        m = (A[0])
        break
    m = (A[0])
    while x != 0:
        if m < A[1]:
            m=A[1]
        for i in range(5):
            A[i]=A[i+1]
            i+=1
        x = int(input())
        A[5] = x
print (m)








            





A=[0]*10000000
B=[0]*3
top=0
s=0
m=0
i=0
i1=0
s1=0
s2=0
s3=0
top1=0
x = input()
A1 = x.split()
if len(A1) > 2:
    n=int(A1[0])
    for i1 in range(len(A1)):
        A1[i1]=int(A1[i1])
        if A1[i1]>m:
            m=A1[i1]
        if A1[i1]<n:
            n=A[i1]
        s+=A1[i1]
        if top1<=2:
            B[top1]=A1[i1]
            s1+=B[top1]
        if top1==2:
            s2=s1%B[top1]
            s3+=s2
            top1=-1
            s1=0
        top1+=1    
        i+=1
        i1+=1    
else:
    n=int(x)
    while  x!='#':
        x=int(x)
        A[top]=x
        if A[top]>m:
            m=A[top]
        if A[top]<n:
            n=A[top]
        s+=A[top]
        if top1<=2:
            B[top1]=A[top]
            s1+=B[top1]
        if top1==2:
            s2=s1%B[top1]
            s3+=s2
            top1=-1
            s1=0
        top1+=1    
        top+=1
        i+=1
        x = input()
print(round(s/i, 3), m, n, s3)



            





a = int(input())
b = int(input())
if a < b:
    a,b=b,a
A = [0]*100
n = a%b
A[0] = a % b
if A[0]==0:
    print(b)
else:
    A[1] = b % A[0]
    if A[1]==0:
        print(A[0])
if A[0] !=0 and A[1] != 0:
    for i in range(2, 100, 1):
        A[i] = A[i-2]%A[i-1]
        if A[i] == 0:
            print (A[i-1])
            break
        i += 1


            





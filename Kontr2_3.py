c = input()
A = input().split(' ')
b=0

for i in range(len(A)):
    A[i] = int(A[i])
    if A[i] == 1:
        b+= 1
for i in range(1, len(A)):
    if A[i] == 0 and A[i-1] == 0:
        b+= 1
print(b)





   
    

            





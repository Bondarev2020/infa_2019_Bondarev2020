c = input()
A = input().split(' ')
for i in range (len(A)):
    A[i]= A[i][::-1]
j=0
def insert_sort(A):
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -=1
insert_sort(A)
for i in range (len(A)):
    A[i]= A[i][::-1]
for i in range (len(A)):
    print(A[i], end=' ')





   
    

            





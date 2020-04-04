c = int(input())
A=[]*c
B=[]*2*c
for i in range (c):
    A.append(input().split(' '))
for i in range (c):
    A[i][0] = float(A[i][0])
    A[i][1] = float(A[i][1])
def insert_sort(A):
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1][1] > A[k][1]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1
insert_sort(A)
for i in range (1, c):
    if A[i - 1][1] == A[i][1]:
        if A[i - 1][0] < A[i][0]:
            A[i], A[i - 1] = A[i - 1], A[i]
for i in range (c):
    print("{:.2f}".format(A[i][0]), "{:.3f}".format(A[i][1]), end='\n')











   
    

            





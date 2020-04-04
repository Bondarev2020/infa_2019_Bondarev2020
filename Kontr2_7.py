A = input().split('.')
B = list(A[0])
for i in range (len(B)):
    B[i] = ord(B[i])
def insert_sort(A):
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -=1
insert_sort(B)
for i in range (len(B)):
    B[i] = chr(B[i])
    print(B[i], end='')
print ('.')




   
    

            





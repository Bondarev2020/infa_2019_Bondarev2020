c = int(input())
A = [0]*c
B = [0]*c
D = [0]*c
for i in range (c):
    D[i] = str(input())
    B[i] = D[i][::-1]
B.sort()
for i in range (c):
    A[i] = B[i][::-1]
def insert_sort(B):
    N = len(B)
    for top in range(1, N):
        k = top
        while k > 0 and len(B[k-1]) > len(B[k]):
            A[k], A[k-1] = A[k-1], A[k]
            B[k], B[k - 1] = B[k - 1], B[k]
            k -=1
insert_sort(B)

k = 1
while k <= 15:
    for i in range (len(A)):
        if len(A[i]) == k:
            print(k)
            break
    for i in range(i, len(A)):
        if len(A[i]) == k:
            print(B[i], A[i], end="\n")
    k+=1




   
    

            





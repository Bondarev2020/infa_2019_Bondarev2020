def hoar_sort(A):
    if len(A) <=1:
        return
    barrier = A[0]
    L = []
    R = []
    M = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L+M+R:
        A[k] = x
        k+=1
A = [2, 5, 10, 2, 3, 345, 23, 45]
hoar_sort(A)
print(A)
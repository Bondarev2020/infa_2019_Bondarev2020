x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
A = [2, 2, 1, 1, -1, -1, -2, -2]
B = [1, -1, 2, -2, -2, 2, 1, -1]
k = -1
def kon():
    if y2==y1 and x2==x1:
        k = 0
        print(k)
        return
    if abs(y2-y1) == 1 and abs(x2-x1) == 1:
        k = -1
        print(k)
        return
    for i in range(len(A)):
        if y2 - B[i] == y1 and x2 - A[i] == x1:
            k = 1
            print(k)
            return
        else:
            for j in range(len(A)):
                if y2 - B[i] - B[j] == y1 and x2 - A[i] - A[j] == x1:
                    k = 2
                    print(k)
                    return
    print ('-1')
kon()


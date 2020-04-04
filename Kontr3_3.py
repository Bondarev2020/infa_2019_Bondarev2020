
A = input().split(', ')
b = int(A[0])
C = []
for i in range(1, len(A[1]), 2):
    C.append(int(A[1][i]))
print (C)
d = b//min(C)
print (d)
e = 0
for x in range (d+1):
    for y in range (d+1):
        if b == C[0]*x + C[1]*y:
            e+=1
            print (C[0], '*', x,  '+',  C[1], '*', y)
print (e)









   
    

            





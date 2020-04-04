a = input().split()
for i in range(len(a)):
    a[i] = int(a[i], base=16)
b = list(hex(int (a[0] ^ a[1])))
for i in range (2, len(b)):
    print (b[i], end ='')


   
    

            





a = int(input())
b = bin(a)
c= 0
for i in range (2, len(b)):
    if b[i] == '1':
        c+=1
print (c)

   
    

            





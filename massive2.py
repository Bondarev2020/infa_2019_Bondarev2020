a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
d=0 
while 0<a[0]<=a[2]:
    a[0]+=int(a[0]*a[1])/100 
    d+=1
print(d)
 
   
    

            





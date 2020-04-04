a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
week=1
price = int(a[0])
delta = int(a[1])
i = 0
m = 0
while week <= a[2]:
    for i in range(7):
        m += price
        price = price + delta
    week+=1
print(m)


   
    

            





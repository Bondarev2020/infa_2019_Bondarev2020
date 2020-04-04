a = int(input())   
b = int(input())   
c = int(input()) 
if a > b:
    (a,b)=(b,a)  
if b > c:
    (b,c)=(c,b)
if a > b:
    (a,b)=(b,a)
if a+b>c and a+c>b and b+c>a:
    if c**2==a**2+b**2:
        print ('right')
    if c**2<a**2+b**2:
        print ('acute')
    if c**2>a**2+b**2:
        print ('obtuse')
else:
    print ('impossible')          





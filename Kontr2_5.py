a = input()
def skobka():
    m = 0
    for i in range(len(a)):
        if a[i]  == '(':
            m+=1
        if a[i] == ')':
            m+=-1
        if m < 0:
            print ('NO')
            return
    print ('YES')
skobka()



   
    

            





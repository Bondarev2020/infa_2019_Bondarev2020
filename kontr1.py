
m1 = int(input())   
H1 = int(input())   
m2 = int(input())   
H2 = int(input())   
m3 = int(input())   
H3 = int(input())   
m4 = int(input())   
H4 = int(input())   
vpx = m1+m2+m3
H = H1+max(H2, H3)
if vpx<=m4 and H<=H4:
    print ('YES')
elif vpx>m4:
    if H<=H4 and vpx-m3<=m4:
        print ('YES')
    elif H>H4 and vpx-m3<=m4:
        if H1+H2<=H4 and H1+H3<=H4:
            print ('YES')
        else:
            print ('NO')
    else:     
        print ('NO')
elif vpx<=m4 and H>H4:
    if H1+H3<=H4:
        print ('YES')
    else:
        print ('NO')    
    
    

            





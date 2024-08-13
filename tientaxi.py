# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:58:19 2024

@author: Phạm Hồng Phúc 23706461
"""
S=float(input("Nhập quãng đường(km):"))
if S<=1:
    print (" số tiền là 20k")
elif 1<S<4 :
    print ("số tiền là",(S*13),"k")
elif 4<=S<=8 :
    print("số tiền là",(3*13+(S-3)*12),"k")
elif  (3*13+5*12+(S-8)*10)> 100:
        print(" số tiền là",((3*13+5*12+(S-8)*10)*0.92),"k")
else :
    print(" số tiền là",(3*13+5*12+(S-8)*10),"k")
    

    
    
    

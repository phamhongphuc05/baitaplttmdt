# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:14:23 2024

@author: Phạm Hồng Phúc 23706461 
"""
import math
a=float(input ("Nhập a="))
b=float(input ("Nhập b="))
A=((math.sqrt(a)- math.sqrt(b))/(math.pow(a,0.25)-math.pow(b,0.25)))-((math.sqrt(a)+ math.pow(a*b,0.25 ))/(math.pow(a,0.25)+ math.pow(b,0.25)))
print(f"Kết quả {A}")



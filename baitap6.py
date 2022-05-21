import numpy as np
n=int(input("nhap so luong phan tu n:"))
m=int(input("nhap so luong phan tu m:"))
a=[]
for i in range(0,m):
    a.append([])
    for j in range(0,n):
        x=int(input("nhap phan tu thu a[%d][%d]:"%(i+1,j+1)))
        a[i].append(x)
A=np.array(a)
print(a.transpose())
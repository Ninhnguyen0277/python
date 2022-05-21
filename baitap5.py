n=int(input("nhap so luong phan tu n:"))
a=[]
s=0
for i in range(0,n):
    a.append(float(input("nhap phan tu thu %d:"%(i+1))))
    if (a[i]%2!=0):
        s=(s+a[i])       
print("trung binh cong cua cac so le la",s/i)
        

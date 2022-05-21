n=int(input("nhap so nguyen duong n="));
s=1;
if(n==0):
    print("thuattoan sai")
else:
    for i in range(2,n+1):
        s=s+1/i;
print("tong so la",s)
n=int(input("Nhap so nguyen duong n="));
if(n>24 and n==0):
    print("nhap lenh sai")
else:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end="");
        print()
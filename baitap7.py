a=float(input("so thu nhat:"))
b=float(input("so thu hai:"))
c=float(input("so thu ba:"))
def max(a,b,c):
    max=a
    if max<b:max=b
    if max<c:max=c
    return max
print("so lon nhat la",max(a,b,c))
    
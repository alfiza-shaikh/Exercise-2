from array import *
n=int(input("Enter number of elements : "))
val=array('i',[])
print("Enter elements : ")
for i in range(n):
    x=int(input())
    val.append(x)
print("Array before sorting :")
for i in val:
    print(i,end=" ")
print()
for i in range(n):
    for j in range(n-i-1):
        if val[j]>val[j+1]:
            val[j],val[j+1]=val[j+1],val[j]
print("Array after bubble sort :")
for i in val:
    print(i,end=" ")
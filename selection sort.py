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
    for j in range(n):
        if i!=j and val[i]<val[j]:
            val[i],val[j]=val[j],val[i]

print("Array after selection sort :")
for i in val:
    print(i,end=" ")
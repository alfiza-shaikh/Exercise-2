def divide(a,s,e):
    i=s
    pivot=a[e]
    for j in range(s,e):
        if	a[j]<=pivot:
            a[i],a[j]=a[j],a[i]
            i+=1
    a[i],a[e]=a[e],a[i]
    return i

def sort(a,s,e):
    if(s<e):
        p=divide(a,s,e)
        sort(a,s,p-1)
        sort(a,p+1,e)

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
sort(val,0,n-1)
for i in val:
    print(i,end=" ")

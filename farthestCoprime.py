import math
def update(arr,n):
    for i in range(n):
        d=0
        coPrime=-1
        for j in range(2,251):
            if(math.gcd(arr[i],j)==1 and d<abs(arr[i]-j)):
                d=abs(arr[i]-j)
                coPrime=j
        arr[i]=coPrime
    for i in range(n):
        print(arr[i],end=" ")
arr=input().strip()
arry=list(map(int, arr.split()))
N=len(arry)
update(arry,N)

num=int(input())
sum=0
temp=num
while temp>0:
    n=temp%10
    sum=sum+n**3
    temp=temp//10
if num==sum:
    print("Armstrong Number")
else:
    print("Not A Armstrong Number")

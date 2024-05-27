def accept(i,j,k):
    def isClose(x,y):
        if abs(x-y)<=1:
            return True
    def isFar(x,y,z):
        if abs(x-z)>=2 and abs(y-z)>=2:
            return True
    if (isClose(i,j) and isFar(i,j,k)) or (isClose(i,k) and isFar(i,k,j)) or (isClose(j,k) and isFar(j,k,i)):
        return True
    else:
        return False
input_list=input().split(',')
split_list=list(map(int, input_list))
res=accept(split_list[0],split_list[1],split_list[2])
print(res)

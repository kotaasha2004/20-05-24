def find_duplicates(l):
    duplicate_list=[]
    for i in l:
        if l.count(i)>1 and  i  not in duplicate_list:
            duplicate_list.append(i)
    new_list=' '.join(map(str, duplicate_list))
    if len(new_list)>0:
        print(new_list)
    else:
        print("-1")
li=input().split()
integer_list=list(map(int, li))
find_duplicates(integer_list)

def example(s):
    N=len(s)
    if N<2:
        return "-1"
    elif N==2:
        return s[0]+s[1]+s[0]+s[1]
    else:
        return s[0]+s[1]+s[N-2]+s[-1]
input_string=input()
res=example(input_string)
print(res)

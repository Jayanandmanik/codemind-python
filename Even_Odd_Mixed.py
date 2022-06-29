n=int(input())
temp=n
rem=0
e,o=0,0
while(n>0):
    res=n%10
    if n%2==0:
        e+=1
    else:
        o+=1
    n=n//10
if e>0 and o>0:
    print('Mixed')
elif e>0 and o==0:
    print('Even')
elif e==0 and o>0:
    print('Odd')
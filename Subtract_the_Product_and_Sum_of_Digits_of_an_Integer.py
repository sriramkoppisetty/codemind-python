n=int(input())
s=1
s1=0
while n>0:
    r=n%10
    s*=r
    s1+=r
    n=n//10
print(s-s1)
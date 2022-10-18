def is_prime(n):
    cnt=0
    if(n>1):
        for i in range(1,n+1):
            if(n%i==0):
                cnt=cnt+1
    if(cnt==2):
        print("Prime")
    else:
        print("Not Prime")
n=int(input())
is_prime(n)
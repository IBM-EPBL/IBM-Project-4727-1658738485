def prime(n1):
    num=2
    while(num<=n1):
        cnt=0
        if(num>1):
            for i in range(1,num+1):
                if(num%i==0):
                    cnt=cnt+1
        if(cnt==2):
            print(num)
        num=num+1
n1=int(input())
prime(n1)
a=int(input())
a1, a2 = 0, 1
count = 0
if a <= 0:
   print("Please enter a positive integer")
elif a == 1:
   print("Fibonacci sequence upto",a,":")
   print(a1)
else:
   print("Fibonacci sequence:")
   while count < a:
       print(a1)
       nth = a1 + a2
       a1 = a2
       a2 = nth
       count += 1
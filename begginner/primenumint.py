lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
for n in range(lower,upper +1):
   if n > 1:
       for a in range(2,n):
           if (n % a) == 0:
               break
       else:
           print(n)

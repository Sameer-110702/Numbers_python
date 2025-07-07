n=int(input("Enter a range : "))
primes=[]
for i in range(1,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count==2:
        primes.append(i)
print("Prime numbers in a given range : ",primes)
print("Alternate prime numbers in the given range are : ",primes[0:n+1:2])

    

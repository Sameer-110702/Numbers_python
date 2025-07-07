# Sunny number
'''n=number
m=number+1
if m= a perfect square then the number is sunny else not sunny'''

n=int(input("Enter a number : "))
m=n+1
print("Number + 1 = ",m)
sq=m**(0.5)
print("Squareroot of (number +1) = ",sq)
p=int(sq)**2
print("Square of the squareroot number = ",p)
if p==m:
    print(n," is a sunny number: ")
else:
    print(n,"is not a sunny number")


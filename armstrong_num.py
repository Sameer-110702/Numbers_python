#Armstrong number using string method
'''sum of powers of the every digit in the given number is equal to input number then the number is armstrong number '''
print("USING ___STRING___METHOD")
n=int(input("enter a number is :"))
print("number is :",n)
s=str(n)
l=len(s)
print("length of the number is :",l)
sum=0
for i in s:
    sum=sum+int(i)**l
print("sum of powers of number is :",sum)
if sum==n:
    print("amstrong")
else:
    print("not amstrong")
print("       ")
print("       ")
print("USING___NORMAL___METHOD")
n=int(input("Enter a number : "))
l=len(str(n))
temp=n
sum=0
while(n>0):
    r=n%10
    sum=sum+r**l
    n=n//10
if temp==sum:
    print("armstromg")
else:
    print("not armstrong")

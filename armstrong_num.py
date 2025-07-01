#Armstrong number using string method
'''sum of powers of the every digit in the given number is equal to input number then the number is armstrong number '''
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

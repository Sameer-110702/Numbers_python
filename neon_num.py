# neon number using string method
'''After squaring of the given number, if the sum of the every digit of the given number is equal to the input then the number is neon number'''
n=int(input("enter a number : "))
sq=n**2
print("square of the number :",sq)
s=str(sq)
sum = 0
for i in s:
    sum=sum+int(i)
print("sum of the numbers :",sum)
if sum==n:
    print("given number is neon number")
else:
    print("given number is not a neon number")

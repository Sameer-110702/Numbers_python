# strong or peterson number using string method
''' if the sum of factorial of every digit in the given number is equal to the input number then the number is strong or peterson number'''
n=int(input())
s=str(n)
sum=0
for i in s:
    fact=1
    for j in range(1,int(i)+1):
        fact=fact*j
    print("a",fact)
    sum=sum+fact
print("b",sum)
if n==sum:
    print("peterson")
else:
    print("not a peterson")

# Automarphic number
'''After squaring the given number if the last digits of the result is equal to input number then the number is automorphic number'''
n=int(input("enter a number : "))
power=n**2
print("power of the number is :",power)
if n%100 == n:
    print("number is automorphic")
else:
    print("number is not automarphic")

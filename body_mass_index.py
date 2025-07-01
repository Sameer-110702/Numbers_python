h=float(input("Enter height in meters : "))
w=float(input("Enter weight in kilograms : "))
#bmi calculation

bmi=(w)/(h**2)
print("your bmi is : ",round(bmi,2))
print("Here’s the BMI category reference:\n Less than 18.5 : Underweight.\n 18.5 – 24.9 : Normal weight.\n 25 – 29.9 : Overweight.\n 30 or more : Obese")

#category
if bmi<18.5:
    print(f"you are under weight, your bmi is {round(bmi,2)}")
elif bmi>18.5 and bmi<24.9:
    print(f"you are normal weight, your bmi is{round(bmi,2)}")
elif bmi>25 and bmi<29:
    print(f"you are over weight, your bmi is{round(bmi,2)}")
else:
    print(f"you are bbese, your bmi is {round(bmi,2)}")


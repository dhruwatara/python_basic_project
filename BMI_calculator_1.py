height=float(input("what is your height in m?"))
weight=float(input("what is your weight in kg?"))

bmi=round((weight/height**2),2)
print(bmi)
print(type(bmi))

if bmi<18.5:
    print("you are underweight")
elif bmi<25:
    print("you have normal weight")
elif bmi<30:
    print("you are overweight")
elif bmi<35:
    print("you are obese")
elif bmi>35:
    print("you are clinically obese")

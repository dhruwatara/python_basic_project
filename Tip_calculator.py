print("welcome to tip calculator")
bill=float(input("what is your total bill?\n$"))
people=int(input("in how many people you want to split the bill?\n"))
tip=int(input("what percent do you want to give a tip, 5% or 12% ?\n"))

total_bill=(((tip/100)*bill)+bill)/people

pay=round(total_bill,2)

print(f"your total bill for each person is ${pay}")

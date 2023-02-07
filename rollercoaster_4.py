print("welcome to the rollercoaster!")

height=int(input("what is your height in cm? \n"))
if height >120:
    print("you can ride")
    bill=0
    age=int(input("what is your age?\n"))
    if age<12:
        bill+=5
    elif age<18:
        bill+=7
    else:
        bill+=12

    photo=input("do you want to take picture? Y or N\n")
    if photo=='y':
        bill+=3
        print(f"your total bill is {bill}")
    else:
        print(f"your total bill is ${bill}")     
else:
    print("sorry, you have to grow taller you can't ride")


height=int(input("what is your height in cm?"))
if height <=120:
    print("sorry you have to grow up taller, you cant ride!!")
else:
    age=int(input("what is your age?"))
    if age<12:
        print("you have to pay $5")
    elif age>=12 and age<=18:
        print("you have to pay $7")
    else:
        print("you have to pay $12")

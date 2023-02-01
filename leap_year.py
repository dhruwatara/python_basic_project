year=int(input("type year you want to check!"))

if year%4==0:
    if year%100:
        if year%400:
            print("it is leap year")
        else:
            print("it is not leap year")
    else:
        print("it is leap year")
else:
    print("it is not leap year")

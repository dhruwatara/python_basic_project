print("Welcome to pizza Diliveries!!")
size= input("which size of pizza you want? S, M, L \n")

bill=0
if size=="s":
    bill+=15
elif size=="m":
    bill+=20
elif size=="l":
    bill+=25

peperoni=input("Do you want to add peperoni? Y, N \n")
extra_cheese=input("do want to add extra cheese? Y, N \n")

if size=="s":
    if peperoni=="y":
        bill+=2
if size=="m" or size=="l":
    if peperoni=="y":
        bill+=3
        
if extra_cheese=="y":
    bill+=1

print(f"your total bill is ${bill}")

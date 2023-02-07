print("welcome to love calculator!!")
name1=input("what is your name?\n")
name2=input("what is your partner's name\n")
fullname=name1+name2
print(fullname)
t=fullname.count("t")
print(type(t))
r=fullname.count("r")
u=fullname.count("u")
e=fullname.count("e")
true=t+r+u+e
true1=str(true)
print(type(true1))

l=fullname.count("l")
o=fullname.count("o")
v=fullname.count("v")
e=fullname.count("e")

love=l+o+v+e
love1=str(love)

love_score=true1+love1
score=int(love_score)

if score<=10 or score>=90:
    print("your love score is {love_score} you go together like coak and mentos")

elif score<40 and score>50:
    print(f"your love score is {love_score}, you are alright together")

else:
    print(f"your love score is {love_score}")

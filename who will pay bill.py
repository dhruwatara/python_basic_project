import random

people=input("write the name of person who are ready to pay the bill\n")
people_list=people.split(" ")
numbers= len(people_list)
payone= random.randint(0,numbers-1)
who_is_paying=people_list[payone]
print(f" {who_is_paying} will pay today's total bill !!")

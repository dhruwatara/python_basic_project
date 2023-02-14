height=input("enter the list of height of student").split()

for n in range (0, len(height)):
    height[n]=int(height[n])

total_height=0
total_student=0
for n in height:
    total_student+=1
    total_height+=n
print(total_height)
print(total_student)

average_height=round((total_height/total_student),2)

print(f"average height of student height is {average_height}")

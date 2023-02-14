even=0
for i in range (0,101,2):
    even+=i
print(f"sum of first 100 even number is {even}")

odd=0
for i in range(1,101,2):
    odd+=i
print(f"sum of first 100 odd number is {odd}")
    
total_sum=odd+even
print(f"total sum of 1st 100 even and odd number is {total_sum}")

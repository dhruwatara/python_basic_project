row1=["😃", "😃","😃"]
row2=["😃", "😃","😃"]
row3=["😃", "😃","😃"]
map=[row1, row2, row3]

print(f" {row1}\n {row2}\n {row3}")

import random
room=input("enter the number where you want to keep treasure")

horizontal=room[0]
vertical=room[1]

row=map[int(horizontal)]
row[int(vertical)]="x"

print(f" {row1}\n {row2}\n {row3}")

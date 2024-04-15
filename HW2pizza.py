import math  
fam = 4
slices = 8
eat =input("How many slices does each family member eat ")
meat = int(eat)
totalS = meat * fam
print(totalS)
wpie = math.ceil(totalS/slices)
print("buy",wpie,"pizza")
lmod = totalS%slices
print(lmod)
print(f"You will have {lmod} leftover slices")


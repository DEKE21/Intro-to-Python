import math
mom = int(input("How many slices does the mom eat? "))
dad=int(input("How many slices does the dad eat? "))
son=int(input("How many slices does the son eat "))
dau=int(input("How many slices does the daughter eat "))
slices = 8
eat = mom+dad+son+dau
print(eat)
wpie = math.ceil(eat/slices)
print("buy",wpie,"pizza")
lmod = eat%slices
print(lmod)
print(f"You will have {lmod} leftover slices")


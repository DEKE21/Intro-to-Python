
try: file_object  = open('C:\\Users\\MechTech3959\\New folder (2)\\edu\\python\\numbers.txt','r')
except FileNotFoundError:
    print("could not find file")
else:
    lines = file_object.readlines()
    total =0
    ln = len(lines)
    copy=[]
    for x in range(0,ln):
        copy.append(int(lines[x]))
    for x in range(0,ln):
        total+= copy[x]
    max = max(copy)   
    greater=[]
    avg = total/ln
    for x in range(0,ln):
        if copy[x] >200:
            greater.append(copy[x])
    greater = set(greater)
    unq = set(copy)
    if len(greater)==1:
        print(f'The number greater than 200 is :{greater}')
    elif len(greater) > 1:
        print(f'The numbers greater than 200 is :{greater}')
    print(f"the unique numbers are :{unq}")
    print(f'the total value: {total}')
    print(f"the largest value is :{max}")
    print(f"the average value is :{avg}")


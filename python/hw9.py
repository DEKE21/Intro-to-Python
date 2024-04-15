import calendar
M = [] #main list
lt =[] #max count
Mt = [] #least count

for x in range(0,12):
    x+=1
    print(calendar.month_abbr[x])
    M.append(int(input("monthly rainfall: ")))

Length = len(M)
Total = 0
for z in range(0,Length):
    Total += M[z]
    z +=1
avg = Total/Length

s = M.copy()
Max = max(s)
Min = min(s)
for t in range(0,12):
    s[t]
    if(s.count(Max)>=1):
        pos = s.index(Max) 
        lt.append(pos)
        s[pos] = -1
for n in range(0,12):
    s[n]
    if(s.count(Min)>=1):
        pos = s.index(Min) 
        Mt.append(pos)
        s[pos] = -1    

print(f'The total rainfall this years is {Total} inches')
print(f'The average rainfall for each month is {avg} inches')

leng = len(lt)
if(leng>=1):
    if(leng > 1):
        print('The months with the highest rainfall were',end=" ")
    if(leng == 1):
        print('The month with the highest rainfall was',end=" ")
    for t in range(0,leng):
        if t < leng-1:
            print( calendar.month_name[lt[t]+1],end=", ")
        if t == leng-1:
            print( "and" ,calendar.month_name[lt[t]+1],end=" ")
    print(f'with {Max} inches')

leng2 = len(Mt)
if(leng2>=1):
    if(leng2 > 1):
        print('The months with the lowest rainfall were',end=" ")
    if(leng2 == 1):
        print('The month with the lowest rainfall was',end=" ")
    for n in range(0,leng2):
        if n < leng2-1:
            print( calendar.month_name[Mt[n]+1],end=", ")
        if n == leng2-1:
            print( "and" ,calendar.month_name[Mt[n]+1],end=" ")
    print(f'with {Min} inches')
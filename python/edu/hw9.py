import calendar
M = []
for x in range(0,12):
    x+=1
    print(calendar.month_abbr[x])
    M.append(input(int("monthly rainfall")))
print(M.sort()) 
 
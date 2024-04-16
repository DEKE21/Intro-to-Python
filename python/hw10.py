import calendar
date = input('Type a date in MM/DD/YYYY format: ')
DL = date.split("/")
month = calendar.month_name[int(DL[0])]
day = DL[1]
year = DL[2]
print(f'{month} {day}, {year}')

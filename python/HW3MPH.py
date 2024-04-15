SL = int(input("What was the speed limit? ")) #Speed limit
YS = int(input("What was your speed? ")) #Your speed
M = int(input("How many miles did you drive? "))
SMPH = int(M/SL*60) #How long it would take you if you went the speed limit(comverted to minutes)
YMPH = int(M/YS*60) #How long it took you(converted to minutes)
if(SL==YS): #If the driver went the speed limit
    print(F'You went the speed limit and it took you {SMPH} minutes')
elif(YS>SL):  #If the driver went over the speed limit
    print(f'If you went the speed limit it would\'ve taken you {SMPH} minutes but by speeding you saved {SMPH-YMPH} minutes')
elif(YS<SL): #If the driver went under the speed limit
    print(f'If you went the speed limit it would\'ve taken you {SMPH} minutes but it took you {YMPH} minutes')


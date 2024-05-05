try: file = open('C:\\Users\\logan\\Downloads\\qtrsales.txt','r')
except FileNotFoundError:
    print("there was a error opening this file")
else:
    inpt = file.readlines()
    leng = len(inpt)
    t =0
    cp=[]
    for x in range(0,leng):
        cp.append(int(inpt[x]))
    for x in range(0,leng):
        t+= cp[x]
    mx = max(cp)   
    lw = min(cp)
    great=[]
    avg = t/leng
    for x in range(0,leng):
        if cp[x] >200:
            great.append(cp[x])
    unique = set(cp)
    print(f'The lowest value is :{lw}')  
    print(f"the largest value is :{mx}")
    print(f"the average value is :{avg}")
    print(f'The elements larger than 200 are :{great}')
    print(f'the total value: {t}')
    print(f"all of the unique elements are :{unique}")
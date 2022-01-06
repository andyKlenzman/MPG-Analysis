#Personal Notes:
#Nice! I got the CSV open by putting it in the same folder and pasting the relative path
import numpy as np
import csv

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

# print(len(mpg))
#print(mpg[0].keys())

#find average mpg in city by all dictionaries, and divide by length of the list
res=0
for d in mpg:
    x=float(d['cty'])
    res +=float(d['cty'])

    # print(d)
    # print()
    # print(x)
    # print()
    # print(res)
    # print()

avg= res/len(mpg)
# print(avg)


#know what city mpg is by number of cyclinders the car has
#iworks when I added 'for d in mpg'
cylinders={}
for d in mpg:
    cylinders = set(d['cyl'] for d in mpg)

CtyMpgByCyl = []
for c in cylinders:
    summpg=0
    cyltypecount=0
    for d in mpg:
        if d['cyl'] == c:
            summpg += float(d['cty'])
            cyltypecount += 1
    CtyMpgByCyl.append((c,summpg/cyltypecount))
    CtyMpgByCyl.sort(key=lambda x: x[0])
print(np.array(CtyMpgByCyl))

#average highway mpg for different vehicle classes
VehClass=[]
for d in mpg:
    VehClass = set(d['class'] for d in mpg)

AvgMpgByClass=[]
for c in VehClass:
    summpg=0
    vehcounter=0
    for d in mpg:
        if d['class']==c:
            summpg +=float(d['hwy'])
            vehcounter+=1
    AvgMpgByClass.append((c,summpg/vehcounter))
    AvgMpgByClass.sort(key=lambda x:x[0])

print(np.array(AvgMpgByClass))


        
        

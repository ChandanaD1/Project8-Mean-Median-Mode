from collections import Counter

import csv 
with open("csvfiles/height&weightHW.csv") as file1: 
    reader = csv.reader(file1)
    data = list(reader)
    
data.pop(0)
height = []

for x in data:
    value = float(x[1])
    height.append(value)

n = len(height)

total = 0

for x in height:
    total = total + x

mean = total/n
print("Mean: ")
print(mean)

height.sort()

if n%2 == 0:
    median1 = float(height[n//2])
    median2 = float(height[n//2 - 1])
    median = (median1 + median2)/2
else:
    median = float(height[n//2])

print("Median: ")
print(median)

mode_range = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0
}

range = Counter(height)
for x,y in range.items():
    if 50<=float(x)<60:
        mode_range["50-60"] = mode_range["50-60"] + y
    elif 60<=float(x)<70:
        mode_range["60-70"] = mode_range["60-70"] + y
    elif 70<=float(x)<80:
        mode_range["70-80"] = mode_range["70-80"] + y

mode, mode_value = 0,0
for x,y in mode_range.items():
    if y > mode_value:
        mode,mode_value = x,y
        
print("Mode: ")
print(mode,mode_value)
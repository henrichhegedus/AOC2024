data = open('input.txt','r')
import re

total = 0
do = True
for line in data.readlines():
    muls = re.findall(r"mul\([0-9]*,[0-9]*\)|don't\(\)|do\(\)", line)

    for mul in muls:

        if mul == "don't()":
            do = False
            continue
        if mul == "do()":
            do = True
            continue

        if do:
            a,b = mul[4:-1].split(',')
            total += int(a)*int(b)

print(total)
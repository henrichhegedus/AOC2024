data = open('input.txt','r')
import re

total = 0
for line in data.readlines():
    muls = re.findall(r"mul\([0-9]*,[0-9]*\)", line)

    for mul in muls:
        a,b = mul[4:-1].split(',')
        total += int(a)*int(b)

print(total)
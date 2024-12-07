data = open('input.txt','r')

list_a = []
list_b = []

safe_count = 0

for line in data.readlines():
    level = line.strip().split(" ")

    level = [int(x) for x in level]


    total = 0
    for i in range(1, len(level)):
        diff = level[i-1] - level[i]
        # print(diff)

        if abs(diff) == 0:
            break
        if abs(diff) > 3:
            break

        if diff>0:
            total += 1

        if diff<0:
            total -= 1

    gaps = len(level) - 1
    if total == gaps or total == -gaps:
        safe_count += 1

print(safe_count)


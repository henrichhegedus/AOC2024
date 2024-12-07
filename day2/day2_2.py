data = open('input.txt','r')

list_a = []
list_b = []

safe_count = 0


def is_safe(level):
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
        return True
    return False

for line in data.readlines():
    level = line.strip().split(" ")

    level = [int(x) for x in level]


    if is_safe(level):
        safe_count += 1
    else:
        for i in range(len(level)):
            sub_level = level[:i] + level[i+1:]

            if is_safe(sub_level):
                safe_count += 1
                break
print(safe_count)
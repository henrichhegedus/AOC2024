data = open('input.txt','r')

list_a = []
list_b = []

for line in data.readlines():
    print(line.strip().split(" "))
    a, _, _, b = line.strip().split(" ")

    list_a.append(a)
    list_b.append(b)

sorted_a = sorted(list_a)
sorted_b = sorted(list_b)

counts_b = {}

for b in sorted_b:
    if b in counts_b:
        counts_b[b] += 1
    else:
        counts_b[b] = 1

value = 0

for a in list_a:
    value += int(a) * counts_b.get(a, 0)

print(value)
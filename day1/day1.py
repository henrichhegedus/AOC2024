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


total = 0

for i in range(len(sorted_a)):
    total += abs(int(sorted_a[i]) - int(sorted_b[i]))

print(total)
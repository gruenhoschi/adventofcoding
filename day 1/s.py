f = open("input.txt")
sum = 0
max = 0

for i in f:
    if i.strip() == "":
        print("sum", sum)
        if sum > max: max = sum
        sum = 0
    else:
        sum += int(i.strip())

print("max", max)



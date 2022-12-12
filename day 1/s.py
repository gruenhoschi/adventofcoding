f = open("input.txt")
sum = 0
calories_list = list()
for i in f:
    if i.strip() == "":
        calories_list.append(sum)
        sum = 0
    else:
        sum += int(i.strip())

calories_list.sort(reverse = True)

sum = 0
for i in range(3):
    sum += calories_list[i]

print("sum",sum)

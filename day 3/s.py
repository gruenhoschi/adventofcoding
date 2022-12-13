def contains_char(x, y):
    ret = set()
    for i in x:
        if y.count(i) != 0:
            ret.add(i)
    return ret

f = open("input.txt")

dupl = list()

for i in f:
    string = i.strip()
    part1 = string[:len(string)//2]
    part2 = string[len(string)//2:]
    dupl += contains_char(part1, part2)

tot = 0
red = 0
for i in dupl:
    if ord(i) > 90:
      red = 96
    else:
      red = 38
    tot += (ord(i) - red)

print(tot)

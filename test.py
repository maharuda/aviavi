list = []
dic = {}
count = 0
number = 0
with open("input.txt") as f:
    for s_line in f:
        list.append(s_line)
        count = count + 1
count = count - 1

for i in range(count):
    if int(list[-1]) % int(list[i][0]) == 0:
        number = number + 1
        a = list[i].find(":")
        key = list[i][:a]
        key = int(key)
        value = list[i][a+1:]
        dic[key] = value
sortedDict = sorted(dic.items())

if number == 0:
    print(list[-1])
else:
    for i in range(number-1):
        print(sortedDict[i][1])

# https://adventofcode.com/2020/day/1
fin = open("day1.in", "r")

entries = list(fin.readlines())
entries = [int(x) for x in entries]

for i in range(len(entries)):
    for j in range(i,len(entries)):
        for k in range(j,len(entries)):
            if entries[i]+entries[j]+entries[k]==2020:
                print(entries[i])
                print(entries[j])
                print(entries[k])
                print(entries[i]*entries[j]*entries[k])
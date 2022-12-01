import numpy as np

with open('elves.txt') as f:
    lines = f.readlines()
    #print(lines[0])
    
    elves = [0]
    i = 0
    mostCaloriesElf = 0

    for x in lines:
        if len(x) == 1:
            if i > 0:
                if elves[i] > elves[mostCaloriesElf]:
                    mostCaloriesElf = i
            i += 1
            elves.append(0)
            #if i == 5:
            #    break

        else:
            elves[i] += int(x)

    print('Elf Number ' + str(mostCaloriesElf + 1) + ' has the most Calories with ' + str(elves[mostCaloriesElf]) + '.')


with open('elves.txt') as f:
    lines = f.readlines()
    #print(lines[0])
    
    elves = [0]
    i = 0
    topThreeElves = [0, 0, 0]

    for x in lines:
        if len(x) == 1:
            i += 1
            elves.append(0)

        else:
            elves[i] += int(x)

    for i in range(3):
        topThreeElves[i] = np.max(elves)
        elves.remove(topThreeElves[i])

    topThreeSum = np.sum(topThreeElves)
    print(topThreeSum)
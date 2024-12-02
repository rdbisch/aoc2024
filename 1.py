import numpy as np

list1 = []
list2 = []

with open("1.input") as file:
    lines = file.read().split('\n')
    for L in lines:
        line = L.split('   ')
        try:
            list1.append(int(line[0]))
            list2.append(int(line[1]))

        except:
            print("Error parsing", L)

    list1 = np.array(sorted(list1))
    list2 = np.array(sorted(list2))
    # 1A s = np.sum(np.abs(list2-list1))

    # 1B
    N = set(list1)
    s = 0
    for n in N:
        s += n*np.sum(list1==n)*np.sum(list2 == n)
    print(s)

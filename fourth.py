import random
list1 = []

def findMax(list, n):
    for i in range(1, n):
        list.append(random.randint(1, 200))
    print(list)
    print(max(list))

findMax(list1, 10)    
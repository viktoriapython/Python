list1 = [5, 6, 7, 8, 9, 1, 5, 7]
list2 = [10, 11, 12, 13, 11, 12, 10]

def Repeat(x):
    size = len(x)
    repeated = []
    for i in range(size):
        k = i + 1
        for j in range(k, size):
            if x[i] ==x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

print(Repeat(list1))
print(Repeat(list2))





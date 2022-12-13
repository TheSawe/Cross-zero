a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
result = []
for i in range(len(a)):
    if a[i] < 5:
        result.append(a[i])
print(result)

print(list(filter(lambda elem: elem < 5, a)))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for i in len(a + b):
    if a[i]

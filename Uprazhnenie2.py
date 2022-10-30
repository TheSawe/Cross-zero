a = 0
while a != 10:
    a += 1
    print(a, end='')
    if a == 5:
        break
    print(', ', end='')
print()
print()
age = 12
number = 0
while number <= age:
    number += 2
    print(number, end=' ')
print()
print()
numbers = ['a', 'b', 'c', 'd']
for i in range(len(numbers)):
    print(i + 1, numbers[i])
    # print(f'{i + 1} {numbers[i]}')
print()
print()
kofficent = 16.5 / 100
weight = 20
result = 0
for i in range(15):
    result = int(weight * kofficent)
    print(f'{i + 1} --- {result}')
    weight += 1


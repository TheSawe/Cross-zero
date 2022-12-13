d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = {}
d1['b'] = 'B'
d1['a'] = 'A'
d1['c'] = 'C'

d3 = {}
d1['c'] = 'C'
d1['b'] = 'B'
d1['a'] = 'A'

print(d1 == d2)
print(d1 == d3)

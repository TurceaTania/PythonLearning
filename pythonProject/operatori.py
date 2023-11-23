'''
Operatori:
aritmetici: +,- ,*,/, %
de comparare: <>, ==, !=, >=, <=
logici: and, or, !
'''

a = 3
b = 5

print(a + b)  # 3+5=> 8
print(a - b)  # 3-5 => -2
print(a * b)  # 3*5 => 15
print(a / b)  # 3/5 => 0.6
print(a % b)  # restul impartirii

print(a == b)  # a este egal cu b? => False
print(a != b)  # a este diferit de b? => True
print(a <= b)  # a este mai mic sau egal cu b? => True

print(a < b and a < 4)  # True si True => True
print(a < b or a < 2)  # True sau False => True , cand avem or ajunge una sa fie True

# sedinta: cu mama sau tata sau ( cu bunica si bunicul)
mama = True
tata = False
bunica = False
bunicul = False

print(mama or tata or (bunica and bunicul))





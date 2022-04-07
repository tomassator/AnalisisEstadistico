import math

a= [10,9,7,4,0.1,0.2,0.3]

iteracion = 0

for i in range(len(a)):
    if sum(a[i:len(a)]) > 10:
        print("PASAMO")
    else:
        print(sum(a[i:len(a)]))
        break


#a = -2
#print(abs(a))
'''for i in range(0,5):
    print(i)

a = []
c = []
c.append((1,2))
a[] += 1

print(a)

b = 0.2

li = 0
ls = b
primerapasada = False
ultimapasada = False

for i in range(0,4):

    aux = ls
    li = ls + 0.01
    ls = li + b - 0.01

    print(li, ls)


def prueba():
    return 1,2

d,e = prueba()

print(d, e)

class A:
    a = [(0,1,3),(1,2,4),(2,3,5)]


b = A

print(b.a[0][2])'''


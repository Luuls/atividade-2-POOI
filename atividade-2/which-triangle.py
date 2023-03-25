# https://www.beecrowd.com.br/judge/pt/problems/view/2313

sides = list(map(int, input().split()))

a, b, c = sides

if a + b <= c or a + c <= b or b + c <= a:
    print("Invalido")
    exit()

if a == b and a == c:
    print("Valido-Equilatero")

elif a != b and a != c and b != c:
    print("Valido-Escaleno")

else:
    print("Valido-Isoceles")

biggest_side = max(sides)

smallest_sides = list(sides)
smallest_sides.remove(biggest_side)

if smallest_sides[0] ** 2 + smallest_sides[1] ** 2 == biggest_side ** 2:
    print("Retangulo: S")

else:
    print("Retangulo: N")

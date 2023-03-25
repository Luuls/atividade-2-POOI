# https://www.beecrowd.com.br/judge/pt/problems/view/2409

a, b, c = map(int, input().split())
h, l = map(int, input().split())

if (a <= h and b <= l) or (b <= h and a <= l) or (a <= h and c <= l) or (c <= h and a <= l) or (b <= h and c <= l) or (c <= h and b <= l):
    print('S')

else:
    print('N')

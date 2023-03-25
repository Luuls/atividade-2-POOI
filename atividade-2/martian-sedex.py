# https://www.beecrowd.com.br/judge/pt/problems/view/2382

l, a, p, r = map(int, input().split())

d = 2*r

if d ** 2 >= l ** 2 + a ** 2 + p ** 2:
    print('S')
    
else:
    print('N')
    
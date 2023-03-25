# https://www.beecrowd.com.br/judge/pt/problems/view/2339

c, p, f = map(int, input().split())

if c * f <= p:
    print('S')

else:
    print('N')

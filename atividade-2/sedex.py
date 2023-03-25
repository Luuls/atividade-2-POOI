# https://www.beecrowd.com.br/judge/pt/problems/view/2375

n = int(input())

a, l, p = map(int, input().split())

if n <= a and n <= l and n <= p:
    print('S')

else:
    print('N')

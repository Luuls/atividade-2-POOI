# https://www.beecrowd.com.br/judge/pt/problems/view/1038

code, amount = map(int, input().split())

if code == 1:
    value = amount * 4.00

elif code == 2:
    value = amount * 4.50

elif code == 3:
    value = amount * 5.00

elif code == 4:
    value = amount * 2.00

elif code == 5:
    value = amount * 1.50

print(f'Total: R$ {value:.2f}')
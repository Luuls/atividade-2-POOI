# https://www.beecrowd.com.br/judge/pt/problems/view/2417

cv, ce, cs, fv, fe, fs = map(int, input().split())

score_c = 3 * cv + ce
score_f = 3 * fv + fe

if score_c > score_f:
    print('C')

elif score_f > score_c:
    print('F')

else:
    if cs > fs:
        print('C')

    elif fs > cs:
        print('F')

    else:
        print('=')

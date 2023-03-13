n1, n2, n3, n4 = map(int, input().split())

average = (2 * n1 + 3 * n2 + 4 * n3 + n4) / (2 + 3 + 4 + 1)

print(f'Media: {average:.1f}')

if average >= 7.0:
    print("Aluno aprovado")

elif 5.0 <= average <= 6.9:
    print("Aluno em exame")
    
    n5 = int(input())
    print(f'Nota do exame: {n5:.1f}')

    average = (average + n5) / 2

    if average >= 5.0:
        print("Aluno aprovado")
    
    elif average <= 4.9:
        print("Aluno aprovado")

    print(f'Media final: {average:.1f}')

elif average < 5.0:
    print("Aluno reprovado")

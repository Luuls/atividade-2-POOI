# https://www.beecrowd.com.br/judge/pt/problems/view/1049

vertebra = input()
animal_class = input()
diet = input()

if vertebra == "vertebrado":
    if animal_class == "ave":
        if diet == "carnivoro":
            print("aguia")

        elif diet == "onivoro":
            print("pomba")

    elif animal_class == "mamifero":
        if diet == "onivoro":
            print("homem")

        elif diet == "herbivoro":
            print("vaca")

elif vertebra == "invertebrado":
    if animal_class == "inseto":
        if diet == "hematofago":
            print("pulga")

        elif diet == "herbivoro":
            print("lagarta")

    elif animal_class == "anelideo":
        if diet == "hematofago":
            print("sanguessuga")

        elif diet == "onivoro":
            print("minhoca")

lista_carros = [
    ("Havit" , 120),
    ("Celta" , 80),
    ("Camaro" , 230),
    ("Prisma" , 130)
]
alugados = []

def mostrar_lista(lista_carros):
    for i , car in enumerate(lista_carros):
        print(f"[{i}] - {car[0]} {car[1]}/R$ per day")

    

    

while True:
    print("===================")
    print("Bem vindos a locadora")
    print("===================")
    print("0 - Ver Portfolio |  1 - Alugar Carro | 2 - Devolver Carro")
    aux2 = int(input())
    if aux2 == 0:
        mostrar_lista(lista_carros)
    elif aux2 == 1:
        mostrar_lista(lista_carros)
        print("Qual deseja alugar ?")
        cod_car = int(input())
        print(f"Voce deseja alugar o carro {lista_carros[cod_car][0]} por quantos dias ? ")
        days = int(input())
        print(f"O valor do seu aluguel foi de {lista_carros[cod_car][1] * days} , deseja alugar ? 0 - Sim | 1 - Nao")
        if int(input()) == 1:
            break
        else:
            print(f"Parabéns carroa alugado !")
            alugados.append(lista_carros.pop(cod_car))
    elif aux2 == 2:
        if len(alugados) == 0:
            print("Nao existe carros alugados")
            break
        else:
            mostrar_lista(alugados)
            print("Qual deseja devolver ?")
            cod_car = int(input())
            lista_carros.append(alugados.pop(cod_car))
            print("Carro devolvido !")
    print("Voce deseja continuar ? 0 - Sim | 1 - Nao")
    if int(input()) == 1:
        break



    

    


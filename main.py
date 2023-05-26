qnt = 0
vegetais = []
pesquisa = ''

while qnt < 3:

    vegetal = input("qual o nome do vegetal?\n")
    fertilizante =  input("qual fertilizante usar?\n")
    quantidade = input("quanto colocar por área?\n")

    vegetais.append([vegetal, fertilizante, quantidade])

    qnt += 1

while pesquisa.lower() != "fim":

    pesquisa = input("qual vegetal você quer?\n")

    resposta = ''

    for vegetal in vegetais:
        if vegetal[0] == pesquisa:
             resposta = f"{vegetal[0]} {vegetal[1]} {vegetal[2]}"
             break
        elif pesquisa.lower() == "fim":
            break
        else:
            resposta = "valor não encontrado"

    print(resposta)

print("obrigado tchaus")
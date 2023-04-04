string = input("digite alguma coisa: ")

lista_caracteres = list(string)

indice_primeiro = 0
indice_ultimo = len(lista_caracteres) - 1

while indice_primeiro < indice_ultimo:
    lista_caracteres[indice_primeiro], lista_caracteres[indice_ultimo] = lista_caracteres[indice_ultimo], lista_caracteres[indice_primeiro]
    indice_primeiro += 1
    indice_ultimo -= 1

string_invertida = ''.join(lista_caracteres)

print(string_invertida)
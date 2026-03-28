def selection_sort(lista):
    n = len(lista)

    for i in range(n):
        menor_indice = i

        for j in range(i + 1, n):
            if lista[j] < lista[menor_indice]:
                menor_indice = j

        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]

    return lista

numeros = []

quantidade = int(input("Quantos números você quer inserir? "))

for i in range(quantidade):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

ordenado = selection_sort(numeros)

print("Lista ordenada:", ordenado)
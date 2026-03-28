# Selection Sort em Python

## Descrição
Implementação do algoritmo Selection Sort em Python para o trabalho da disciplina de Estrutura de Dados.

## Como executar
1. Execute o arquivo Algoritmo.py
2. Informe a quantidade de números que deseja compor a lista
3. Digite os valores da lista

## Complexidade
- Melhor caso: O(n²)
- Caso médio: O(n²)
- Pior caso: O(n²)
## - Espaço:
- Melhor Caso: O(1) Constante
- Caso Médio: O(1) Constante
- Pior Caso: O(1) Constante
- Estável: O algoritimo Selection Sort NÃO é estável

## Vantagens
- Simplicidade de implementação: É um dos algoritmos mais fáceis de entender e codificar. Ideal para iniciantes;
- Poucas trocas (swaps): Ao contrário de outros algoritmos, ele faz no máximo n − 1 trocas, o que pode ser útil quando a escrita na memória é custosa;
- Uso de memória eficiente: É um algoritmo in-place, ou seja, não precisa de memória adicional significativa;
- Desempenho previsível:O tempo de execução é sempre o mesmo, independentemente da entrada.

## Desvantagens
- Baixa eficiência (O(n²)): Para listas grandes, ele é muito lento comparado a algoritmos mais avançados;
- Não é estável (na versão padrão): Pode alterar a ordem relativa de elementos iguais;
- Não aproveita listas parcialmente ordenadas: Mesmo que a lista já esteja quase ordenada, ele continua com o mesmo número de comparações;
- Pouco usado na prática: Na maioria dos sistemas reais, algoritmos mais eficientes são preferidos.

 
# Introdução à Ciência da Computação com Python - Parte 1 

[(Coursera)](https://www.coursera.org/learn/ciencia-computacao-python-conceitos/)

Este repositório reúne os scripts que utilizei para resolver os exercícios do curso. 
Abaixo segue algumas notas feitas durante as aulas.


## Notas sobre listas

- coleções de objetos
- array
- vetor

### Manipulação de Listas

- Fatias:

Seleciona os valores da lista baseando-se nos valores assumidos por início e fim:    
    
    lista[início:fim]

O length desse fatiamento será a diferença entre os valores de fim e início.

Se for necessário selecionar os elementos desde o início da lista até um determinado valor:

    lista[:fim]

E também  o contrário, especificando onde iniciar a seleção, indo até o fim da lista:

    lista[início:]

- Clonar

Para clonar uma lista utilize:

    lista_clonada = lista_original[:]

Ao usar lista_clonada = lista, não é feito um clone, mas sim as duas listas apontam para o mesmo vetor. Desse modo, se for modificado um valor em lista_clonada, na lista original ele também será modificado. Experimente as linhas abaixo no Python:

    lista_original = ['python', 'is' 'awesome']

    lista_clonada = lista_original

    lista_clonada[2] = 'life'

    lista_clonada

    lista_original

Agora, tente da seguinte maneira:

    lista_original = ['python', 'is' 'awesome']

    lista_clonada = lista_original[:]

    lista_clonada[2] = 'life'

    lista_clonada

    lista_original




Bibliografia que o curso adota: 

[Aulas Python - IME USP ](https://panda.ime.usp.br/aulasPython/static/aulasPython/index.html)
[Python Tutorial - documentação do Python](https://docs.python.org/3/tutorial/)
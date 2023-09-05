#​Desafio 1: Transforme a frase1 em uma lista de palavras e guarde o resultado em uma variável chamada palavras1

#Desafio 2: Transforme a frase2 em uma lista de palavras e guarde o resultado em uma variável chamada palavras2

#Desafio 3: Pegue o palavras1 e transforme elas no seguinte string: "Desafio,manipulação,de,strings". Imprima o resultado no console.

#Desafio 4: Pegue o palavras2 e transforme elas no seguinte string: frase2 = "jhonatan & rafael & carol & camilla". Imprima o resultado no console.

frase1 = 'Eu me chamo caio '
frase2 = ' jhonatan,rafael,carol,camilla '



palavra1 = frase1.split()
palavra2 = frase2.split(',')
print(','.join(palavra1))
print('&'.join(palavra2))


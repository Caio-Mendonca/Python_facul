
print('ALGORITMO PARA ESCREVER A SEQUÊNCIA DE FIBONACCI')
print('-'*35)
qtde = int(input("Informe quantos números Fibonacci você deseja:"))
valor_1 = 1
valor_2 = 2
sequencia = [1,1]
for count in range (2,qtde):
    valor = sequencia[count -1] + sequencia[count - 2]
    sequencia.append(valor)

print('A sequência é:')
print(sequencia)
print('-'*35)



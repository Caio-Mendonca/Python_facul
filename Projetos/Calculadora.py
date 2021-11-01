print("Calculadora Python")
print("-"*35)

operacao = input('''
Escolha a operação que deseja realizar:
+  para adição
-  para subtração
*  para multiplicação
/  para divisão
''')

numero_1 = int(input('Escreva o primeiro número: '))
numero_2 = int(input('Escreva o segundo número: '))

if operacao == '+':
    print('{} + {} = '.format(numero_1, numero_2))
    print(numero_1 + numero_2)

elif operacao == '-':
    print('{} - {} = '.format(numero_1, numero_2))
    print(numero_1 - numero_2)

elif operacao == '*':
    print('{} * {} = '.format(numero_1, numero_2))
    print(numero_1 * numero_2)

elif operacao == '/':
    print('{} / {} = '.format(numero_1, numero_2))
    print(numero_1 / numero_2)

else:
    print("Você não escolheu uma operção válida, por favor tente novamente.")
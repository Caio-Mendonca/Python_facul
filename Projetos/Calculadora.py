print("Calculadora Python")
print("-"*35)

operacao = input('''
Escolha a operação que deseja realizar:
+  para adição
-  para subtração
*  para multiplicação
/  para divisão
$  para potenciação
#  para radiciação
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

elif operacao == '$':
    print('{} ** {} = '.format(numero_1, numero_2))
    print(numero_1 ** numero_2)

elif operacao == '#':
    resultado= (numero_1) ** (1/numero_2)
    print('{} ** {} = '.format(numero_1, numero_2))
    print(resultado)

else:
    print("Você não escolheu uma operação válida, por favor tente novamente.")
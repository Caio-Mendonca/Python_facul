pilha = []
insercao = True

while insercao == True:
   numero = int(input("Insira um número: "))
   check = numero % 2 #confere se o numero é par
   if check == 0:
       pilha.append(numero) #adiciona o numero a lista
   if check != 0:   #caso  o número seja impar
       if len(pilha) == 0:  #se a lista estiver vazia
           n = len(pilha)
       else:
           pilha.pop() #Quando o numero é impar retiramos o último item inserido
   if numero == 0:
       pilha.pop() #Como o zero  é um numero par ele entra na lista, aqui se remove o zero
       insercao = False    #Para o laço de repetição
       print("Programa encerrado")

itens = len(pilha)
print('-'*35)
print("Sua pilha:")
while itens != 0: #laço para mostrar e retirar os numeros da lista
 print(pilha[itens - 1])
 del(pilha[itens - 1])
 itens = len(pilha)
if itens == 0:
   print(pilha)
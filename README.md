# Python facul
Neste repositório irei colocar todo conteúdo sobre Python que venho estudando no curso Inteligência de mercado e análise de dados 

# Sumário:
* <a href="#">Variáveis</a>
* <a href="#">Tipos de dados</a>
* <a href="#">Operadores</a>
* <a href="#estrutura_de_repeticao">Estrutura de repetição</a>
* <a href="#">Estruturas condicionais</a>
* <a href="#">Funções</a>
* <a href="#estrutura_dados">Estrutura de dados</a>


<div id="estrutura_de_repeticao"> <h1> Estrutura de Repetição</h1>
  <p> Em certos casos precisamos utilizar um conjunto de instruções mais de uma vez... Nestes casos será necessária a utilizaação de loops com o FOR ou WHILE</P>
  
  * <a href="#"> FOR </a>
    
  * <a href="#"> WHILE </a>
</div>

<div id="estrutura_dados"><h1> Estrutura de dados </h1>
  
* <a href="#Built-in"> BUILT-IN </a>
  
* <a href="#definidas_pelo_usuario">DEFINIDA PELO USUÁRIO</a>
</div>
<div id="Built-in">
  <h1> Estrutura de dados Built-in</h1>
  
  - Listas:
   Listas de elementos. Podem receber elementos de tipos distintos como, string, números inteiros, booleanos ou até mesmo outras litas, tuplas e dicinário. Utilizamos "[ ]" para abrir e fechar uma lista.
  
    Ex: v = [ "abacate", "banana", "cenoura"]
  
   Para exibir utilizamos:
   print(v)
  
   Para saber o tipo usamos:
   print(type(v))
  
   Para imprimir somente um elemento utilizamos o índice:
   print(v[0])
  ----> o índice de uma lista sempre começa no 0
  
  - Tuplas:
  Uma tupla pode ser considerada uma lista imutável de elementos. Uma vez criada, não pode ser alterada. Utilizamos "( )" para abrir e fechar uma tupla. Para declarar um tupla não é necessário utilizar "()".
  
     EX: v = (1,2,3)---> FIXO
  
  - Dicionário: 
  Um dicionário pode ser imterpretado como uma lista composta por conjuntos de pares <strong>Chave-valor</strong>. Utilizamos "{ }" para abrir e fechar um dicionário.
  
    <ol>Ex: v = { "A":"adenina",</ol>
    <ol>"C":"citosina",</ol>
    <ol>"T":"timina",</ol>
    <ol>"G":"guanina", }</ol>
  
  - Conjuntos:
  Conjuntos de elementos únicos. Utilizamos "{ }" para abrir e fechar um conjunto.
  
    Ex: v = {1,2,3,4,5,6,7,8,9}
   Manipulando Conjunto:
  
   Adicionando itens: v.add(111)
  
   Removendo itens: v.remove(1)
  
   Impriminto os itens: print(v)
  
  
  </div>
  <div id="definidas_pelo_usuario">
  <h1>Estruturas de dados definidas pelo usuário</h1>
  
  - Listas encadeadas:
  Também conhecidas como listas ligadas, são estruturas que amarzenam dados compostos por valores conectados por ponteiros
  
  - Pilhas:
  São um tipo especial de listas. Sua representação é por uma pilha de dados. Nesse tipo de estrutura de dados o primeiro elemento a ser adicionado é o último a ser removido.
  
  - Filas:
  São outro tipo de listas. Filas são um tipo de estrutura linear em que o primeiro item a ser adicionado é o primeiro item a ser removido. Támbem é conhecido como uma estrutura FIFO.
<div> 
  - Árvores:
   São um tipo de estrutura não linear, em que cada elemento é representado como um nó. A estrutura parte do chamado nó raiz (root).
  <div>
    <li type="square"> Representações:
      <ul type="circle">
          <li>Representação Hierárquica</li>
          <li>Diagrama de inclusão/ diagrama de Venn </li>
          <li>Diagrama com barras (usando recuos "identação")</li>
          <li>Numeração por níveis </li>
      </ul>
    </li>
  </div>
</div>
  
  - Grafos:
  Podem ser compreendidos como um tipo de estrutura em que cada elemento é representado como um vértice, interligado por arestas que podem representar possíveis interações ou relacionamentos.
  
  - Hash-map:
  Vincula uma chave a um determinado valor (figura). Assim, para obter um valor, basta informar a chave. São siimilares aos dicionários Python. 
    
  </div>

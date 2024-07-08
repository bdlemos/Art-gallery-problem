# O Problema da Galeria de Artes

O presente GitHub tem como objetivo explorar um problema clássico de geometria computacional: *O Problema da Galeria de Arte*. Isso será feito resolvendo o problema de forma interativa com o usuário, mostrando o passo a passo da execução do algoritmo e os resultados parciais de cada etapa da solução. 

Outro objetivo deste repositório é apresentar esse problema clássico para alunos e professores da área de computação, de modo que possa ser utilizado didaticamente para compreender a solução do problema, colaborando com conhecimento para a comunidade.

# Explorando o Problema

## Contextualização

O problema da Galeria de Artes tem uma motivação simples: queremos posicionar câmeras em uma galeria (de artes!), de modo que as câmeras não tenham pontos cegos, conseguindo vigiar todo o espaço da nossa galeria. As câmeras funcionam normalmente, tendo uma rotação em 360°, se necessário, para vigiar aquele espaço. Observe que aqui chamamos de 'galeria', mas esse problema tem  aplicação em qualquer tipo de espaço que se deseja instalar câmeras e vigiar, como bancos, bibliotecas, etc.

Considere também que não estamos trabalhando com qualquer espaço: vamos utilizar as plantas dessa construção, e considerar que essa planta é referente à uma área aberta, ou seja, apenas os contornos que delimitam aquele espaço serão as informações que teremos para resolver esse problema de instalar as câmeras. Além disso, queremos instalar as câmeras não em qualquer lugar, mas apenas nas **paredes!**

Observe que, a partir disso, temos a possibilidade de interpretar o espaço em que será instalado as câmeras como um polígono convexo 2-D. A primeira coisa que vem na nossa mente para tentar resolver o problema é: Porque não instalamos uma câmera em cada **vértice** do nosso polígono? Com certeza, essa seria uma solução, mas observe que ela é cara. Se o polígono tem N vértices, e N é um número grande, sairia bem caro utilizar N câmeras de qualidade para vigiar esse espaço.

Então, será que não seria possível vigiar todo o espaço desse polígono utilizando menos de N câmeras? e a resposta é sim!  Exatamente esse é o *Problema da Galeria de Artes!*

Por fim, queremos um limite superior para a instalação de câmeras, em uma área delimitada por um polígono 2D.

## Proposta de Solução do Problema

Para resolver o problema, vamos utilizar algoritmos da área de geometria computacional. Observe, então, que nossa entrada para o algoritmo será um polígono 2D. Cada vértice desse polígono será exatamente um ponto em um espaço de 2 dimensões, definido com as coordenadas (x,y) desse ponto. Formalmente, nossa entrada é uma lista de N pontos, com Pi = (xi, yi). A partir desses pontos, executaremos algoritmos clássicos de geometria computacional.

Para facilitar, o polígono abaixo será utilizado para ilustrar as etapas na solução do problema, guiando o leitor e facilitando a visualização.

<div align="center">
  <img src="https://github.com/bdlemos/Art-gallery-problem/assets/117868879/860ee872-d15e-4e1a-a304-8a9f11525016"/>
</div> 
<p align="center">Figura 1: Polígono Exemplar

O primeiro objetivo é triangular esse polígono, pois, a partir desse polígono triangulado, basta decidir os vértices de cada triângulo em que se deseja colocar uma câmera. Para realizar essa etapa, será utilizado o **Algoritmo da Poda de Orelhas** ou **Ear Clipping Algorithm**.

O segundo objetivo é exatamente encontrar quais vértices desse triângulo serão selecionados, utilizando um algoritmo de **3-Coloração**, com base no grafo dual gerado a partir do polígono triangulado. Dessa forma, estaremos selecionando exatamente a quantidade de câmeras que serão necessárias para vigiar todo o espaço, onde cada câmera vigia um triângulo do polígono. A parte interessante dessa etapa é observar que é possível realizar a 3-Coloração em tempo polinomial para esse caso, que será mostrado posteriormente.

Esses algoritmos serão explicados na sessão seguinte =).

# Metodologia e Solução

Nessa seção, ilustraremos como é desenvolvida a solução do algoritmo que resolve o problema abordado anteriormente. A abordagem está dividida em 2 etapas, uma que envolve a triangulação do polígono e outra que utiliza da busca em largura para realizar uma 3-coloração desse grafo inteligentemente em tempo polinomial, definindo o posicionamento das câmeras na galeria.

## Triangulação através do Algoritmo da Poda de Orelhas

O Algoritmo da Poda de Orelhas é utilizado inicialmente com o objetivo de triangular o polígono em questão. A critério de exemplo, iremos sempre nos referir ao polígono da seção anterior.

### Algoritmo

Esse algoritmo busca, de forma iterativa, triangular o polígono e 'podar' o triângulo gerado, através da remoção do vértice que se liga unicamente aos 2 outros vértices que compõe o triângulo. Para formalizar, seja um triângulo formado pelos pontos Pi, Pi+1, Pi+2, onde os pontos estão ordenados em ordem anti-horária. O primeiro objetivo é verificar se a reta PiPi+1Pi+2 vira a esquerda. Depois, verificar se não tem nenhum ponto Pk qualquer interno ao triângulo em questão. Por último, um dos 3 pontos será removido do polígono, suponha que seja o ponto Pi+1. Por fim, o triângulo Pi-Pi+1-Pi+2 é registrado como um triângulo possível, e as retas que formam esse triângulo são: Pi-Pi+1 (Reta do Polígono), Pi+1-Pi+2 (Reta do Polígono), Pi-Pi+2 (Reta 'imaginária'), fechando o triângulo.

### Implementação

Exemplo de resultado da triangulação executada no polígono de exemplo.
<div align="center">
  <img src="https://github.com/bdlemos/Art-gallery-problem/assets/117868879/3bb1cb19-1b8a-49f4-8e2c-66e71f25f588"/>
</div>
<p align="center">Figura 2: Resultado da execução do Algoritmo da Poda de Orelhas na Figura 1.

## Coloração com uma Busca em Profundidade no Grafo Dual

![animation](https://github.com/bdlemos/Art-gallery-problem/assets/117868879/32b2b186-8f44-4f53-8798-5634f465a49e)

# Requisitos

É necessário instalar a biblioteca Plotly para usufruir da animação implementada pelos alunos.


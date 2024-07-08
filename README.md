# O Problema da Galeria de Artes

O presente GitHub tem como objetivo explorar um problema clássico de geometria computacional: *O Problema da Galeria de Arte*. Isso será feito resolvendo o problema de forma interativa com o usuário, mostrando o passo a passo da execução do algoritmo e os resultados parciais de cada etapa da solução. 

Outro objetivo deste repositório é apresentar esse problema clássico para alunos e professores da área de computação, de modo que possa ser utilizado didaticamente para compreender a solução do problema, colaborando com conhecimento para a comunidade.

# Explorando o Problema

## Contextualização

O problema da Galeria de Artes tem uma motivação simples: queremos posicionar câmeras em uma galeria (de artes!), de modo que as câmeras não tenham pontos cegos, conseguindo vigiar todo o espaço da nossa galeria. As câmeras funcionam normalmente, tendo uma rotação em 360°, se necessário, para vigiar aquele espaço. Observe que aqui chamamos de 'galeria', mas esse problema tem  aplicação em qualquer tipo de espaço que se deseja instalar câmeras e vigiar, como bancos, bibliotecas, etc.

Considere também que não estamos trabalhando com qualquer espaço: vamos utilizar as plantas dessa construção, e considerar que essa planta é referente à uma área aberta, ou seja, apenas os contornos que delimitam aquele espaço serão as informações que teremos para resolver esse problema de instalar as câmeras. Além disso, queremos instalar as câmeras não em qualquer lugar, mas apenas nas **paredes!**

Observe que, a partir disso, temos a possibilidade de interpretar o espaço em que será instalado as câmeras como um polígono 2D. A primeira coisa que vem na nossa mente para tentar resolver o problema é: Porque não instalamos uma câmera em cada **vértice** do nosso polígono 2D? Com certeza, essa seria uma solução, mas observe que ela é cara. Se o polígono tem N vértices, e N é um número grande, sairia bem caro utilizar N câmeras de qualidade para vigiar esse espaço, afinal não podemos economizar na segurança.

Então, será que não seria possível vigiar todo o espaço desse polígono utilizando menos de N câmeras? e a resposta é sim!  Exatamente esse é o *Problema da Galeria de Artes!*

Por fim, queremos um limite superior para a instalação de câmeras, em uma área delimitada por um polígono 2D.

## Proposta de Solução do Problema

Para resolver o problema, vamos utilizar algoritmos da área de geometria computacional. Observe, então, que nossa entrada para o algoritmo será um polígono 2D. Cada vértice desse polígono será exatamente um ponto em um espaço de 2 dimensões, definido com as coordenadas (x,y) desse ponto. Formalmente, nossa entrada é uma lista de N pontos, com Pi = (xi, yi). A partir desses pontos, executaremos algoritmos clássicos de geometria computacional.

Para facilitar, o polígono abaixo será utilizado para ilustrar as etapas na solução do problema, guiando o leitor e facilitando a visualização.

![image](https://github.com/bdlemos/Art-gallery-problem/assets/117868879/860ee872-d15e-4e1a-a304-8a9f11525016)

O primeiro objetivo é triangular esse polígono, pois, a partir desse polígono triangulado, basta decidir os vértices de cada triângulo em que se deseja colocar uma câmera. Para realizar essa etapa, será utilizado o **Algoritmo da Poda de Orelhas** ou **Ear Clipping Algorithm**.

O segundo objetivo é exatamente encontrar quais vértices desse triângulo serão selecionados, utilizando um algoritmo de **3-Coloração**, com base no grafo dual gerado a partir do polígono triangulado. Dessa forma, estaremos selecionando exatamente a quantidade de câmeras que serão necessárias para vigiar todo o espaço, onde cada câmera vigia um triângulo do polígono. A parte interessante dessa etapa é observar que é possível realizar a 3-Coloração em tempo polinomial para esse caso, que será mostrado posteriormente.

Esses algoritmos serão explicados na sessão seguinte =).

# Metodologia e Solução

Nessa seção, ilustraremos como é desenvolvida a solução do algoritmo que resolve o problema abordado anteriormente. A abordagem está dividida em 2 etapas, uma que envolve a triangulação do polígono e outra que envolve a coloração, que define o posicionamento e quantidade de câmeras

## Triangulação através do Algoritmo da Poda de Orelhas

Exemplo de resultado da triangulação executada no polígono de exemplo.
![image](https://github.com/bdlemos/Art-gallery-problem/assets/117868879/3bb1cb19-1b8a-49f4-8e2c-66e71f25f588)

## Coloração com uma Busca em Profundidade no Grafo Dual

![animation](https://github.com/bdlemos/Art-gallery-problem/assets/117868879/32b2b186-8f44-4f53-8798-5634f465a49e)

# Requisitos

É necessário instalar a biblioteca Plotly para usufruir da animação implementada pelos alunos.


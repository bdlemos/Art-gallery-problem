# O Problema da Galeria de Artes

O presente GitHub tem como objetivo explorar um problema clássico de geometria computacional: *O Problema da Galeria de Arte*. Isso será feito resolvendo o problema de forma interativa com o usuário, mostrando o passo a passo da execução do algoritmo e os resultados parciais de cada etapa da solução.Outro objetivo deste repositório é apresentar esse problema clássico para alunos e professores da área de computação, de modo que possa ser utilizado didaticamente para compreender a solução do problema, colaborando com conhecimento para a comunidade.

# Contextualização do Problema

O problema da Galeria de Artes tem uma motivação simples: queremos posicionar câmeras em uma galeria (de artes!), de modo que
as câmeras não tenham pontos cegos, conseguindo vigiar todo o espaço da nossa galeria. As câmeras funcionam normalmente, tendo
uma rotação em 360°, se necessário, para vigiar aquele espaço. Observe que aqui chamamos de 'galeria', mas esse problema tem 
aplicação em qualquer tipo de espaço que se deseja instalar câmeras e vigiar, como bancos, bibliotecas, etc.

Considere também que não estamos trabalhando com qualquer espaço: vamos utilizar as plantas dessa construção, e considerar que
essa planta é referente à uma área aberta, ou seja, apenas os contornos que delimitam aquele espaço serão as informações que
teremos para resolver esse problema de instalar as câmeras. Além disso, queremos instalar as câmeras não em qualquer lugar, mas
apenas nas **paredes!**

Observe que, a partir disso, temos a possibilidade de interpretar o espaço em que será instalado as câmeras como um polígono 2D.
A primeira coisa que vem na nossa mente para tentar resolver o problema é: Porque não instalamos uma câmera em cada **vértice** do
nosso polígono 2D? Com certeza, essa seria uma solução, mas observe que ela é cara. Se o polígono tem N vértices, e N é um número
grande, sairia bem caro utilizar N câmeras de qualidade para vigiar esse espaço, afinal não podemos economizar na segurança.

Então, será que não seria possível vigiar todo o espaço desse polígono utilizando menos de N câmeras? e a resposta é sim! 
Exatamente esse é o *Problema da Galeria de Artes!*

Por fim, queremos um limite superior para a instalação de câmeras, em uma área delimitada por um polígono 2D.

# Proposta de Solução do Problema

Para resolver o problema, vamos utilizar algoritmos da área de geometria computacional. Observe, então, que nossa entrada para o
algoritmo será um polígono 2D. Cada vértice desse polígono será exatamente um ponto em um espaço de 2 dimensões, definido com as
coordenadas (x,y) desse ponto.

Formalmente, nossa entrada é uma lista de N pontos, onde:

![equation](https://latex.codecogs.com/svg.image?&space;Point_{i}=(x_{i},y_{i}))

# Requisitos

É necessário instalar a biblioteca Plotly para usufruir da animação implementada pelos alunos.


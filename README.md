# O Problema da Galeria de Artes

O presente GitHub tem como objetivo explorar um problema clássico de geometria computacional: *O Problema da Galeria de Arte*. Isso será feito resolvendo o problema de forma interativa com o usuário, mostrando o passo a passo da execução do algoritmo e os resultados parciais de cada etapa da solução. 

Outro objetivo deste repositório é apresentar esse problema clássico para alunos e professores da área de computação, de modo que possa ser utilizado didaticamente para compreender a solução do problema, colaborando com conhecimento para a comunidade.

# Explorando o Problema

## Contextualização

O problema da Galeria de Artes tem uma motivação simples: queremos posicionar câmeras em uma galeria (de artes!), de modo que as câmeras não tenham pontos cegos, conseguindo vigiar todo o espaço da nossa galeria. As câmeras funcionam normalmente, tendo uma rotação em 360°, se necessário, para vigiar aquele espaço. Observe que aqui chamamos de 'galeria', mas esse problema tem  aplicação em qualquer tipo de espaço que se deseja instalar câmeras e vigiar, como bancos, bibliotecas, etc.

Considere também que não estamos trabalhando com qualquer espaço: apesar da galeria ser tridimensional, é possível projetá-la no plano, e trabalhar com o polígono simples formado. Além disso, queremos instalar as câmeras preferencialmente nas paredes.

A primeira coisa que vem na nossa mente para tentar resolver o problema é: Porque não instalamos uma câmera em cada **vértice** do nosso polígono? Com certeza, essa seria uma solução, mas observe que ela é cara. Se o polígono tem N vértices, e N é um número grande, sairia bem caro utilizar N câmeras de qualidade para vigiar esse espaço.

Então, será que não seria possível vigiar todo o espaço desse polígono utilizando menos de N câmeras? e a resposta é sim! Exatamente isso que buscamos! Apesar do valor ótimo de câmeras ser um problema difícil, temos como objetivo encontrar um limite superior para a instalação de câmeras, que seja adequada para qualquer problema, mesmo que não seja ótima, já trazendo alguma economia.

## Proposta de Solução do Problema

Para resolver o problema, vamos utilizar algoritmos da área de geometria computacional. Observe, então, que nossa entrada para o algoritmo será um polígono 2D. Cada vértice desse polígono será exatamente um ponto em um espaço de 2 dimensões, definido com as coordenadas (x,y) desse ponto. Formalmente, nossa entrada é uma lista de N pontos, com P<sub>i</sub> = (x<sub>i</sub>, y<sub>i</sub>). A partir desses pontos, executaremos alguns algoritmos clássicos de geometria computacional para resolver o problema.

Para facilitar, o polígono abaixo será utilizado para ilustrar as etapas na solução do problema, guiando o leitor e facilitando a visualização.

<div align="center">
  <img src="https://github.com/bdlemos/Art-gallery-problem/assets/117868879/860ee872-d15e-4e1a-a304-8a9f11525016"/>
</div> 
<p align="center">Figura 1: Polígono Exemplar

Observe que o problema de definir as câmeras é trivialmente resolvido, se nosso polígono de entrada é um triângulo, bastando colocar uma única câmera em qualquer vértice. A partir dessa informação, nosso objetivo principal passa ser dividir nosso polígono principal em triângulos. Formalmente, o problema consiste em decompor esse polígono em triângulos, usando um conjunto máximo de diagonais disjuntas (que não se interceptam). Além disso, vamos definir que uma diagonal é necessariamente um segmento de reta que conecta 2 vértices e se encontra estritamente dentro do polígono. Para realizar essa etapa, será utilizado o **Algoritmo da Poda de Orelhas** ou **Ear Clipping Algorithm**.

O segundo objetivo é exatamente encontrar uma forma de selecionar os vértices do polígono, de modo que cobrimos todos os triângulos, para posicionar as câmeras de forma eficaz. Isso será feito utilizando um algoritmo de **3-Coloração**, executado com base no grafo dual gerado a partir do polígono triangulado. 

> [!IMPORTANT]
> Para definir, um grafo dual do polígono triangulado é um grafo onde todas as **faces** (nesse caso, triângulos), se tornam **vértices** e as **arestas** existem apenas entre 2 vértices caso suas respectivas faces tem um **lado em comum**, sendo esse lado uma **diagonal**, definida nas seções posteriores. 

A parte interessante dessa etapa é observar que é possível realizar a 3-Coloração em tempo polinomial, aproveitando de algumas propriedades particulares do problema.

Esses algoritmos serão explicados na sessão seguinte =).

# Metodologia e Solução

Nessa seção, ilustraremos como é desenvolvida a solução do algoritmo que resolve o problema abordado anteriormente. A abordagem está dividida em 2 etapas, uma que envolve a triangulação do polígono e outra que utiliza da busca em profundidade (DFS) para realizar uma 3-coloração desse grafo inteligentemente em tempo polinomial, definindo o posicionamento e o limiar das câmeras para a galeria.

## Triangulação através do Algoritmo da Poda de Orelhas

O Algoritmo da Poda de Orelhas é utilizado inicialmente com o objetivo de triangular o polígono em questão. A critério de exemplo, iremos sempre nos referir ao polígono da seção anterior. Além disso, compreendemos que é satisfatório clarificar que existe um teorema que afirma que todo polígono simples admite triângulação, bem como tem exatamente n-2 triângulos, sendo n o número de vértices do polígono. A demonstração fica a cargo do leitor. A importância desse teorema para nós? Podemos concluir diretamente, então, que uma galeria de artes pode ser vigiada por n-2 câmeras, basta colocar uma em cada triângulo.

### Algoritmo

Esse algoritmo busca, de forma iterativa, triangular o polígono e 'podar' o triângulo gerado, sendo seu tempo de execução um tempo quadrático em função da entrada O(n²). Então, vamos definir que a orelha de um polígono é um triângulo, formado pelos vértices u, v e w, onde o segmento uw é uma diagonal do polígono. Para esse caso, nosso vértice v é a nossa ponta da orelha.

Portanto, o primeiro passo do algoritmo passa a ser uma busca por pontas de orelha no polígono, isto é, se a reta formada pelos vértices V<sub>i-1</sub>-V<sub>i</sub>-V<sub>i+1</sub> vira a esquerda, definindo V<sub>i</sub> como a ponta da orelha, podendo ser executado em O(1), sem uso de ponto flutuante com alguns truques de geometria computacional. Depois, verificar se não tem nenhum vértice V<sub>k</sub> qualquer interno ao triângulo em questão, também feito em tempo constante com truques de geometria computacional. Essa etapa é feita linearmente em relação ao número de vértices do polígono, visto que buscamos pela ponta de orelha. 

> [!TIP]
> Todos os truques de geometria computacional mencionados podem ser vistos na implementação.

Por fim, o algoritmo repete esse processo, removendo as orelhas (triângulos) que encontra, atualiza seu polígono, apenas removendo o vértice que é a ponta da orelha, e tornando os outros 2 vértices adjacentes, até que o número de vértices seja menor ou igual à 3, sendo esse o último triângulo. Segue abaixo um gif mostrando a execução do algoritmo.

<div align="center">
  <img src="https://github.com/bdlemos/Art-gallery-problem/assets/117868879/b5a56fe2-089f-4155-94c6-3231f1c3c27e">
</div>
<p align="center">Figura 2: Execução do Algoritmo da Poda de Orelhas no polígono exemplar.

### Implementação

A implementação do Algoritmo da Poda de Orelhas pode ser encontrada no presente repositório, definida no arquivo polygon.py, [aqui](https://github.com/bdlemos/Art-gallery-problem/blob/main/polygon.py)!

> [!NOTE]
> OBS: Algumas implementações mais elaboradas do Algoritmo da Poda de Orelhas podem executar em O(N logN)

## Coloração com uma Busca em Profundidade no Grafo Dual

Agora, vamos para a segunda etapa da solução proposta: A coloração no grafo dual. Essa etapa aparenta ser complexa, mas na realidade é extremamente simples, e vamos explorar uma propriedade desse grafo dual. Nesse momento, pare para refletir por um instante no seguinte fato: Escolha uma diagonal, de algum triângulo desse polígono. Observe que qualquer diagonal necessariamente divide nosso polígono em 2 partes! Então, isso faz com que as arestas do nosso grafo dual, caso removidas, resultam em um grafo desconexo1 (por definição, cada diagonal se torna uma aresta no grafo dual). Nesse momento, você deve se lembrar a partir dessa mágica propriedade: *Ora, então nosso grafo dual é uma **árvore**!* Essa é mais uma forma de enxergar que, na realidade, se removermos uma aresta do grafo dual, estaremos desconectando esse grafo.

### Algoritmo

Com o conhecimento que nosso grafo dual tem a propriedade de ser uma árvore, podemos realizar essa 3 coloração de forma muito inteligente: Inicialmente, escolhemos um vértice qualquer do grafo dual. Agora, vamos pegar a face que ele representa, e pintar seus vértices com 3 cores, azul, vermelho e verde. 

A etapa seguinte consiste em ir para o vizinho do nosso vértice no dual. Observe que a face que esse vértice vizinho representa, por definição, compartilha 2 vértices com o triângulo anterior, tendo 2 de seus vértices já pintados. Portanto, basta selecionar a cor faltante para pintar o último vértice. A partir disso, seguimos para o próximo vértice, repetindo esse procedimento.

Assim, o que estamos fazendo na prática, é executar uma Busca em Profundidade no grafo dual, pintando o vértice inicial com as 3 cores, e todos os restantes apenas completamos com a cor faltante, então essa etapa formalmente utiliza tempo O(N), isto é, linear no número de vértices do polígono de entrada. Abaixo, mostramos o grafo dual em preto sendo construído conforme é explorado pela Busca em Profundidade, e a coloração dos vértices do polígono é efetuada, conforme avançamos na busca.

<div align="center">
  <img src="https://github.com/bdlemos/Art-gallery-problem/assets/117868879/32b2b186-8f44-4f53-8798-5634f465a49e">
</div>
<p align="center">Figure 3: Execução da Coloração através da Busca em Profundidade no Grafo Dual.</p>

### Implementação

A implementação da 3-Coloração pode ser encontrada no presente repositório, definida no arquivo Coloring.py, [aqui](https://github.com/bdlemos/Art-gallery-problem/blob/main/Coloring.py)!

# Requisitos

É necessário instalar a biblioteca Plotly para usufruir da animação implementada pelos alunos.


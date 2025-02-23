# O Problema da Galeria de Artes

<div align="justify">

O presente repositório tem como objetivo explorar um problema clássico de geometria computacional: *O Problema da Galeria de Arte*. Isso será feito resolvendo o problema de forma interativa com o usuário, mostrando o passo a passo da execução do algoritmo e os resultados parciais de cada etapa da solução.

Outro objetivo deste repositório é apresentar esse problema clássico para alunos e professores da área de computação, de modo que possa ser utilizado didaticamente para compreender a solução do problema, colaborando com conhecimento para a comunidade.

</div>

# Explorando o Problema

## Contextualização

<div align= "justify">

O problema da Galeria de Artes tem uma motivação simples: queremos posicionar câmeras em uma galeria (de artes!), de modo que as câmeras não tenham pontos cegos, conseguindo vigiar todo o espaço da nossa galeria.   As câmeras funcionam normalmente, tendo uma rotação em 360°, se necessário, para vigiar aquele espaço. Observe que aqui chamamos de 'galeria', mas esse problema tem  aplicação em qualquer tipo de espaço que se      deseja instalar câmeras e vigiar, como bancos, bibliotecas, etc.

Considere também que não estamos trabalhando com qualquer espaço: apesar da galeria ser tridimensional, é possível projetá-la no plano, e trabalhar com o polígono simples formado. Além disso, queremos instalar as câmeras preferencialmente nas paredes.

A primeira coisa que vem na nossa mente para tentar resolver o problema é: Porque não instalamos uma câmera em cada **vértice** do nosso polígono? Com certeza, essa seria uma solução, mas observe que ela é cara. Se o polígono tem N vértices, e N é um número grande, sairia bem caro utilizar N câmeras de qualidade para vigiar esse espaço.

Então, será que não seria possível vigiar todo o espaço desse polígono utilizando menos de N câmeras? e a resposta é sim! Exatamente isso que buscamos! Apesar do valor ótimo de câmeras ser um problema difícil, temos como objetivo encontrar um limite superior para a instalação de câmeras, que seja adequada para qualquer problema, mesmo que não seja ótima, já trazendo alguma economia.

</div>

## Proposta de Solução do Problema

<div align="justify">

Para resolver o problema, vamos utilizar algoritmos da área de geometria computacional. Observe, então, que nossa entrada para o algoritmo será um polígono 2D. Cada vértice desse polígono será exatamente um ponto em um espaço de 2 dimensões, definido com as coordenadas desse ponto. Formalmente, nossa entrada é uma lista de N pontos, com P<sub>i</sub> = (x<sub>i</sub>, y<sub>i</sub>). A partir desses pontos, executaremos alguns algoritmos clássicos de geometria computacional para resolver o problema.

Para facilitar, o polígono abaixo será utilizado para ilustrar as etapas na solução do problema, guiando o leitor e facilitando a visualização.

</div>
<div align="center">
  <img src="https://github.com/bdlemos/Art-gallery-problem/assets/117868879/860ee872-d15e-4e1a-a304-8a9f11525016"/>
</div> 
<p align="center">Figura 1: Polígono Exemplar

<div align="justify">

Observe que o problema de definir as câmeras é trivialmente resolvido, se nosso polígono de entrada é um triângulo, bastando colocar uma única câmera em qualquer vértice. A partir dessa informação, nosso objetivo principal passa ser dividir nosso polígono principal em triângulos. 

Formalmente, o problema consiste em decompor esse polígono em triângulos, usando um conjunto máximo de diagonais disjuntas (que não se interceptam). Além disso, vamos definir que uma diagonal é necessariamente um segmento de reta que conecta 2 vértices e se encontra estritamente dentro do polígono. Para realizar essa etapa, será utilizado o **Algoritmo da Poda de Orelhas** ou **Ear-Clipping Algorithm**.

O segundo objetivo é exatamente encontrar uma forma de selecionar os vértices do polígono, de modo que cobrimos todos os triângulos, para posicionar as câmeras de forma eficaz. Isso será feito utilizando um algoritmo de **3-Coloração**, executado com base no grafo dual gerado a partir do polígono triangulado. Veremos como a 3-Coloração será executada em tempo linear para esse problema nas seções seguintes.

As implementações para os algoritmos apresentados como solução nessa seção serão desenvolvidos nas seções posteriores.

</div>

> [!IMPORTANT]
> <div align="justify"> Um Grafo Dual do polígono triangulado é um grafo onde todas as <b>faces</b> (nesse caso, triângulos), se tornam <b>vértices</b> e as <b>arestas</b> existem apenas entre 2 vértices caso suas respectivas faces tem um <b>lado em comum</b>, sendo esse lado uma <b>diagonal</b>, definida formalmente nas seções posteriores. </div>

# Metodologia e Solução

<div align="justify">
  
Nessa seção, ilustraremos como é desenvolvida a solução do algoritmo que resolve o problema abordado anteriormente. A abordagem está dividida em 2 etapas, uma que envolve a triangulação do polígono e outra que utiliza da busca em profundidade (DFS)[^1] para realizar uma 3-coloração desse grafo em tempo polinomial, definindo o posicionamento e o limiar das câmeras para a galeria.

</div>

## Triangulação através do Algoritmo da Poda de Orelhas

<div align="justify">
  
O Algoritmo da Poda de Orelhas é utilizado inicialmente com o objetivo de triangular o polígono em questão. A critério de exemplo, iremos sempre nos referir ao polígono da seção anterior. 

</div>

> [!IMPORTANT]
> <div align="justify">Existe um teorema que afirma que todo polígono simples admite triângulação, bem como tem exatamente n-2 triângulos, sendo n o número de vértices do polígono. A demonstração fica a cargo do leitor.</div>

<div align="justify">

A importância desse teorema para nós? Podemos concluir diretamente, então, que uma galeria de artes pode ser vigiada por n-2 câmeras, bastando colocar uma em cada triângulo. Apesar disso, esse limite será refinado ainda mais.

</div>

### Algoritmo

<div align="justify">

Esse algoritmo busca, de forma iterativa, triangular o polígono e 'podar' o triângulo gerado, sendo seu tempo de execução um tempo quadrático em função da entrada O(N<sup>2</sup>). Então, vamos definir que a orelha de um polígono é um triângulo, formado pelos vértices u, v e w, onde o segmento uw é uma diagonal do polígono. Para esse caso, nosso vértice v é a nossa ponta da orelha.

Portanto, o primeiro passo do algoritmo passa a ser uma busca por pontas de orelha no polígono, isto é, se a reta formada pelos vértices V<sub>i-1</sub>-V<sub>i</sub>-V<sub>i+1</sub> vira a esquerda, definindo V<sub>i</sub> como a ponta da orelha. Isso pode ser executado em O(1), sem uso de ponto flutuante com alguns truques de geometria computacional. 

Depois, verificar se não tem nenhum vértice V<sub>k</sub> qualquer interno ao triângulo em questão, também feito em tempo constante com truques de geometria computacional. Essa etapa é feita linearmente em relação ao número de vértices do polígono, visto que temos que buscar pela ponta de orelha, utilizando os testes acima sob todo vértice.

</div>

> [!TIP]
> <div align="justify">Todos os truques de geometria computacional mencionados, como a rotação à esquerda e a verificação de pontos internos do triângulo podem ser encontrados na implementação. </div>

<div align="justify">

Por fim, o algoritmo repete esse processo, removendo as orelhas (triângulos) que encontra, atualiza seu polígono, apenas removendo o vértice que é a ponta da orelha e tornando os outros 2 vértices adjacentes, até que o número de vértices seja menor ou igual à 3, restando o último triângulo. Segue abaixo um gif mostrando a execução do algoritmo.

</div>

<div align="center">
  <img src="https://github.com/bdlemos/Art-gallery-problem/assets/117868879/b5a56fe2-089f-4155-94c6-3231f1c3c27e">
</div>
<p align="center">Figura 2: Execução do Algoritmo da Poda de Orelhas no polígono exemplar.

### Implementação

<div align="justify">

A implementação do Algoritmo da Poda de Orelhas pode ser encontrada no presente repositório, definida no arquivo polygon.py, [aqui](https://github.com/bdlemos/Art-gallery-problem/blob/main/polygon.py)!

</div>

> [!NOTE]
> Algumas implementações mais elaboradas para triangulação de polígonos podem executar em O(N logN)

<div align="justify">

A implementação em questão faz uso do paradigma de orientação à objeto, criando um objeto que representa o polígono, chamado de Polygon. Após criado, o objeto conta com métodos que plotam e exibem a animação de triângulação para o polígono em questão de forma interativa com o usuário, podendo este verificar os frames da execução manualmente para acompanhar o passo a passo.

</div>

<div align="justify">

> Lembre-se que o polígono dado como entrada deve ser um [polígono simples](https://pt.wikipedia.org/wiki/Polígono_simples), isto é, os pontos (vértices) que formam o polígono. Além disso, a classe espera que esses pontos estejam ordenados em [ordem anti-horária](https://www.geeksforgeeks.org/orientation-3-ordered-points/).

</div>

## Coloração com uma Busca em Profundidade no Grafo Dual

<div align="justify">

Agora, vamos para a segunda etapa da solução proposta: A coloração no grafo dual. Essa etapa aparenta ser complexa, mas na realidade é extremamente simples, e vamos explorar uma propriedade desse grafo dual. Nesse momento, pare para refletir por um instante no seguinte fato: Escolha uma diagonal, de algum triângulo desse polígono. Observe que qualquer diagonal necessariamente divide nosso polígono em 2 partes! 

Então, isso faz com que as arestas do nosso grafo dual, caso removidas, resultam em um grafo desconexo (por definição, cada diagonal se torna uma aresta no grafo dual). Nesse momento, você deve se lembrar a partir dessa mágica propriedade: *Ora, então nosso grafo dual é uma **árvore**!* Essa é mais uma forma de enxergar que, na realidade, se removermos uma aresta do grafo dual, estaremos desconectando esse grafo.

</div>

### Algoritmo

<div align="justify">

Com o conhecimento que nosso grafo dual tem a propriedade de ser uma árvore, podemos realizar essa 3 coloração de forma inteligente: Inicialmente, escolhemos um vértice qualquer do grafo dual. Agora, vamos pegar a face que ele representa, e pintar seus vértices com 3 cores, azul, vermelho e verde. 

A etapa seguinte consiste em ir para o vizinho do nosso vértice no dual. Observe que a face que esse vértice vizinho representa, por definição, compartilha 2 vértices com o triângulo anterior, tendo 2 de seus vértices já pintados. Portanto, basta selecionar a cor faltante para pintar o último vértice. A partir disso, seguimos para o próximo vértice, repetindo esse procedimento.

Assim, o que estamos fazendo na prática, é executar uma Busca em Profundidade no grafo dual, pintando o vértice inicial com as 3 cores, e todos os restantes apenas completamos com a cor faltante, então essa etapa formalmente utiliza tempo O(N), isto é, linear no número de vértices do polígono de entrada. Abaixo, mostramos o grafo dual em preto sendo construído conforme é explorado pela Busca em Profundidade, e a coloração dos vértices do polígono é efetuada, conforme avançamos na busca.

</div>

<div align="center">
  <img src="https://github.com/bdlemos/Art-gallery-problem/assets/117868879/32b2b186-8f44-4f53-8798-5634f465a49e">
</div>
<p align="center">Figure 3: Execução da Coloração através da Busca em Profundidade no Grafo Dual.</p>

### Implementação

<div align="justify">
  
A implementação da 3-Coloração pode ser encontrada no presente repositório, definida no arquivo Coloring.py, [aqui](https://github.com/bdlemos/Art-gallery-problem/blob/main/Coloring.py)!

Bem como a implementação do algoritmo anterior, essa implementação foi realizada utilizando o paradigma de orientação à objeto, contando com uma classe Coloring. Essa classe espera receber um objeto do tipo Polygon em seu construtor, onde realiza automaticamente a coloração do polígono.

</div>

>[!IMPORTANT]
> A animação da coloração se encontra implementada na [main](https://github.com/bdlemos/Art-gallery-problem/blob/main/main.py) deste repositório.

# Conclusão

<div align="justify">

Por fim, a conclusão é que é possível economizar algumas câmeras que seriam utilizadas, visto que agora nosso limiar para as câmeras utilizando os algoritmos acima é n/3, e o posicionamento das câmeras fica definido com base na coloração de cada vértice obtida na segunda etapa da solução propostas.

</div>

# Requisitos

<div align="justify">

É necessário instalar a biblioteca Plotly para visualizar as animações da implementação deste repositório.

As instruções para uso parcial das classes estão nos tópicos anteriores. Caso queria utilizar o repositório como um todo, baixe os arquivos do repositório em algum diretório da sua escolha, vá até esse diretório e execute o comando a seguir no terminal.

```
python3 main.py <nome_da_instância>
```

Lembre-se que nome_da_instância não é apenas o nome do arquivo, mas seu endereço completo. Preferencialmente, utilize a extensão .txt para posicionar os pontos do polígono.

</div>

# Autores

Bernardo Dutra Lemos e Raphael Aroldo Carreiro Mendes

# Referências

[^1]: Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein. Introduction to Algorithms, 3rd Edition. MIT Press, 2009. ISBN 978-0-262-03384-8.

# aeg-20192

Algoritmos em Grafos - 2019/2, Instituto de Informática, UFG

## Autor

- Erick Vinícius Vieira e Souza / _201515568_

## Instruções

Para rodar este projeto, é necessário ter instalada uma versão igual ou superior do `Python 3.6`. Basta digitar `python3 ./Main.py` numa janela de terminal e o programa de exemplificação iniciará, criando um grafo aleatório. A partir daí, é possível utilizar os demais arquivos para instanciar novos objetos que dão acesso à outras funcionalidades.  
É possível também utilizar softwares como o **Jupyter Notebook** para carregar as classes para o _runtime_ do Python3 e assim, ter uma experiência em tempo real. Para tal, consulte mais informações [aqui](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Running%20Code.html).  

## Artefatos  

1. Main.py: um script responsável por executar um exemplo aleatório de um objeto da classe `Grafo`.  
2. Utils.py: o script resposável pela criação randômica do grafo supracitado.  
3. Grafo_Interface.py: classe abstrata fornecida pelo professor.  
4. Grafo_Lista_Adjacencia.py: classe que implementa as especificações do item anterior.  
5. Grafo_Matriz_Adjacencias.py: classe responsável por implementar a matriz de adjacências.  
6. README.md: este arquivo.

### Principais Métodos e Funções

#### Grafo_Lista_Adjacencia & Grafo_Matriz_Adjacencias

- **__ init__(orientado)**: construtor da classe `Grafo`; caso a flag _orientado_ seja sinalizada com `True`, o grafo passará a se comportar de maneira diferente [para atender a esta especificaçao](http://www.educ.fc.ul.pt/icm/icm2001/icm33/grafosorientados.htm).
- **DefinirN(n)**: inicia o grafo com N vértices, nomeados segundo as letras do Alfabeto Romano Moderno `(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, W, V, X, Y, Z)`.  
- **V()**: retorna uma lista com todos os vértices do grafo.
- **E()**: retorna uma lista com todas as arestas do grafo. Se o grafo em questão for do tipo _orientado_, então a lista resultante contará apenas com **1** aparição da aresta _**(u, v)**_.
- **AdicionarAresta(u, v)**: cria uma aresta entre os vértices _u_ e _v_, desde que estes sejam vértices válidos dentro do grafo em questão. Caso o grafo não seja do tipo _orientado_, tanto _**(u, v)**_ quanto _**(v, u)**_ serão criadas.
- **RemoverAresta(u, v)**: apaga a aresta entre os vértices _u_ e _v_, desde que estes sejam vértices válidos dentro do grafo em questão e estejam ligados. Caso o grafo não seja do tipo _orientado_, tanto _**(u, v)**_ quanto _**(v, u)**_ serão apagadas.
- **SaoViz(u, v)**: retorna `True` quando _u_ é vizinho de _v_ e `False`, caso contrário.
- **Viz(v, Fechada)**: retorna uma lista de todos os vizinhos do grafo atual. Caso a flag __Fechada__ seja marcada, o próprio _v_ também será incluído no retorno.
- **Print()**: produz uma representação gráfica (em caracteres alfanuméricos) do grafo atual.

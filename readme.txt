/**********************************************************************
 *  Hyrule's maze readme.txt template
 **********************************************************************/


Name: Felipe Teles dos Santos
Student ID: 08103842-4


Hours to complete assignment (optional): 12h


/**********************************************************************
 *  Explain briefly how you implemented the datatype for states.
 **********************************************************************/[]
Os estados são representados por nodos. Cada nodo tem as seguintes propriedades:
- Ponto, uma coordenada cartesiana (x,y), que representa uma posição do mapa;
- Custo, o número de movimentos necessários do nodo inicial até nodo corrente;
- Heurística, a distancia otimista desse nodo até o nodo objetivo;
- Parent, uma referencia para o nodo antecessor;
- Key, chave composta pela coordenada, atributo util para acesso hash.



/**********************************************************************
 *  Explain briefly how you represented a search node
 *  (state + number of moves + previous search node).
 **********************************************************************/
O estado inicial ou nodo inicial é adicionado em uma fila ordenada de acordo com a prioridade do nodo. 
A fila começa a ser consumida e para cada nodo consumido é:
- Verificado se o nodo não é o objetivo
- O nodo é adicionado em uma hash de de nodos fechados
- todos os vizinhos desse nodo são avaliados.

Durante a avaliação dos vizinhos são feitos as seguintes ações:
- Criação do nodo, primeiramente inicializando somente o ponto;
- Testa se o nodo não está na lista de fechados e se positivo  inicializa  o parent (antecessor), o custo e a heurística, se negativo vai para a próxima avaliação.
- Se o nodo não estiver na lista de fechados também é testado se ele está na fila, se não estiver na fila é adicionado na fila de prioridades, caso contrário é feito um teste para verificar se o nodo que já está na fila é maior que o que está sendo avaliado e se positivo o nodo que está sendo avaliando entra no lugar do que já estava na fila.




/**********************************************************************
 *  Explain briefly how you detected unsolvable problems.
 **********************************************************************/
Ao executar o algoritmo descrito acima, se a fila ficou vazia e a flag de problema resolvido continua com o valor Falso, o problema não tem solução.




/**********************************************************************
 *  If you wanted to solve random $10^6$ problem, which would you 
 * prefer:  more time (say, 2x as much), more memory (say 2x as much), 
 * a better priority queue (say, 2x as fast), or a better priority 
 * function (say, one on the order of improvement from Hamming to 
 * Manhattan)? Why?
 **********************************************************************/
Gostaria de ter uma função de prioridade melhor, que retornasse a distancia exata do caminho do nodo até o objetivo. Dessa forma o nodo visitado seria sempre o nodo mais próximo do objetivo o que faria alcançar o objetivo mais rápido.





/**********************************************************************
 *  If you did the extra credit, describe your algorithm briefly and
 *  state the order of growth of the running time (in the worst case)
 *  for isSolvable().
 **********************************************************************/
Para o isSolvable(), foi feito um o  Greedy Best-First-Search considerando a lista de fechados. Ao invés de utilizar heurística+custo como prioridade da fila foi utilizado só a heurística. 
Essa mudança representou em torno de 10 segundos na execução de uma mapa de 500x500 sem obstáculos. Como o greedy segue o primeiro caminho até encontrar o objetivo nesse caso ele é perfeito pois ele vai visitar apenas os nodos do primeiro caminho e que nesse caso é o mais curto.
Se o problema não tiver solução todos os nodos vão ser avaliados, assim como no A*. Não tem ganho.
Se o existir obstáculos similares a representação abaixo:
 _____________________ 
|          | Goal     |
|start     |          |
|                     |
|_____________________|
Tanto o A* quanto o Greedy, vão ter custos aproximados. 
A complexidade dos dois algoritmos é O(b^m), logo essa solução só garante ganho para alguns casos.

/**********************************************************************
 *  Known bugs / limitations.
 **********************************************************************/
Na solução final não tem nenhum bug conhecido.


/**********************************************************************
 *  Describe whatever help (if any) that you received.
 *  Don't include readings, lectures, and precepts, but do
 *  include any help from people (including staff, classmates, and 
 *  friends) and attribute them by name.
 **********************************************************************/





/**********************************************************************
 *  Describe any serious problems you encountered.                    
 **********************************************************************/
Na primeira implementação que achei que estava correta ficava variando os testes, as vezes tudo passava e em outras dava problema. Demorei um bom tempo para descobrir que era problema na fila da biblioteca Queue.getPriorityQueue(). 
Para resolver esse problema, fiz a substituição da fila por uma estrutura que desenvolvi com o auxilio da biblioteca heapq.


/**********************************************************************
 *  List any other comments here. Feel free to provide any feedback   
 *  on how much you learned from doing the assignment, and whether    
 *  you enjoyed doing it.                                             
 **********************************************************************/
Achei ótima a estrutura inicial do trabalho. Testes, o framework inicial, tudo isso ajudou a entender melhor o algoritmo.
Melhorias: Deixar um alerta sobre a Queue.getPriorityQueue().
coloquei comentário em todo o codigo para melhor entendimento, mas de forma resumida cada projeto faz:

main.py :
Este código implementa um algoritmo genético para resolver o problema da mochila, onde, dada uma lista de itens com pesos e valores, o objetivo é selecionar itens de forma que o valor total seja maximizado sem ultrapassar o peso máximo permitido.

O algoritmo recebe como entrada os pesos e valores dos itens, o número de cromossomos (indivíduos), o número de gerações, e o peso máximo permitido. Ele então aplica os operadores de seleção, crossover e mutação para evoluir a população, buscando sempre melhorar a solução.

Ao final, o algoritmo retorna a lista de melhor valor obtido em cada geração, junto com a configuração dos itens selecionados.




funcao.py : 
Este código implementa um algoritmo genético para encontrar o valor de x que miniminiza a função f(x)= x elevado a 3 -6x + 14 no intervalo -10,10.
O valor de 𝑥 é representado como um cromossomo binário, que é convertido para um número real.

A população inicial de 10 indivíduos é avaliada com base na função de fitness. O algoritmo aplica operadores de seleção (torneio ou roleta viciada), crossover (1 ou 2 pontos de corte) e mutação (1% de chance por gene) para gerar novas soluções. O processo é repetido por um número máximo de gerações, e elitismo pode ser usado para manter os melhores indivíduos entre as gerações.

O melhor valor de x e o menor valor da função são mostrados ao final. O progresso do algoritmo é monitorado, com a exibição do melhor fitness a cada 10 gerações.

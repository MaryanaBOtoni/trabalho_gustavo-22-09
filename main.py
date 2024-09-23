import random
import numpy as np

# Função de avaliação: Retorna o valor total dos itens, desde que o peso não ultrapasse o limite
def avaliar_individuo(cromossomo, pesos_e_valores, peso_maximo):
    peso_total = sum(pesos_e_valores[i][0] for i in range(len(cromossomo)) if cromossomo[i] == 1)
    valor_total = sum(pesos_e_valores[i][1] for i in range(len(cromossomo)) if cromossomo[i] == 1)
    return valor_total if peso_total <= peso_maximo else 0  # Penaliza soluções que ultrapassam o peso máximo

# Gera a população inicial (binária)
def gerar_populacao(tamanho_populacao, tamanho_cromossomo):
    return [np.random.randint(2, size=tamanho_cromossomo).tolist() for _ in range(tamanho_populacao)]

# Função de crossover de 2 pontos
def crossover(pai1, pai2):
    ponto1 = random.randint(1, len(pai1) - 2)
    ponto2 = random.randint(ponto1 + 1, len(pai1) - 1)
    filho1 = pai1[:ponto1] + pai2[ponto1:ponto2] + pai1[ponto2:]
    filho2 = pai2[:ponto1] + pai1[ponto1:ponto2] + pai2[ponto2:]
    return filho1, filho2

# Função de mutação
def mutacao(cromossomo, taxa_mutacao):
    for i in range(len(cromossomo)):
        if random.random() < taxa_mutacao:
            cromossomo[i] = 1 - cromossomo[i]  # Inverte o gene

# Seleção por roleta
def selecao_roleta_viciada(populacao, fitnesses):
    soma_fitness = sum(fitnesses)
    if soma_fitness == 0:
        return random.choice(populacao)  # Evita divisão por zero
    roleta = [fitness / soma_fitness for fitness in fitnesses]
    selecionado = np.random.choice(len(populacao), p=roleta)
    return populacao[selecionado]

# Algoritmo Genético para o problema da mochila
def algoritmo_genetico_mochila(pesos_e_valores, peso_maximo, numero_de_cromossomos, geracoes, taxa_mutacao=0.3, elitismo=True):
    tamanho_cromossomo = len(pesos_e_valores)
    populacao = gerar_populacao(numero_de_cromossomos, tamanho_cromossomo)
    melhor_individuo_por_geracao = []

    for geracao in range(geracoes):
        fitnesses = [avaliar_individuo(cromossomo, pesos_e_valores, peso_maximo) for cromossomo in populacao]
        nova_populacao = []

        # Elitismo: guarda o melhor indivíduo da geração anterior
        if elitismo:
            melhor_fitness = max(fitnesses)
            melhor_individuo = populacao[fitnesses.index(melhor_fitness)]
            nova_populacao.append(melhor_individuo)

        # Reproduz novos indivíduos
        while len(nova_populacao) < numero_de_cromossomos:
            pai1 = selecao_roleta_viciada(populacao, fitnesses)
            pai2 = selecao_roleta_viciada(populacao, fitnesses)
            filho1, filho2 = crossover(pai1, pai2)
            mutacao(filho1, taxa_mutacao)
            mutacao(filho2, taxa_mutacao)
            nova_populacao.extend([filho1, filho2])

        populacao = nova_populacao[:numero_de_cromossomos]

        # Avalia a nova população e guarda o melhor indivíduo
        fitnesses = [avaliar_individuo(cromossomo, pesos_e_valores, peso_maximo) for cromossomo in populacao]
        melhor_fitness = max(fitnesses)
        melhor_individuo = populacao[fitnesses.index(melhor_fitness)]
        melhor_individuo_por_geracao.append((melhor_fitness, melhor_individuo))

        # Calcula a média de peso dos cromossomos selecionados (com valor 1)
        print(f"Geração {geracao + 1}: Melhor valor = {melhor_fitness:.2f}, Cromossomos = {melhor_individuo}")

    return melhor_individuo_por_geracao

# Função principal que pergunta as entradas do usuário
def main():
    # Solicita os dados de entrada
    pesos_e_valores = [
        [2, 10],
        [4, 30],
        [6, 300],
        [8, 10],
        [8, 30],
        [8, 300],
        [12, 50],
        [25, 75],
        [50, 100],
        [100, 400]
    ]

    print("Dados de entrada:")
    print("Pesos e Valores:", pesos_e_valores)

    peso_maximo = 100
    numero_de_cromossomos = 150
    geracoes = 50

    # Executa o algoritmo genético
    algoritmo_genetico_mochila(pesos_e_valores, peso_maximo, numero_de_cromossomos, geracoes)

# Executa a função principal
if __name__ == "__main__":
    main()

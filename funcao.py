import numpy as np
import random

# Função que calcula o valor da função f(x) = x³ - 6x + 14
def f(x):
    return x**3 - 6*x + 14

# Converte um vetor binário para um número decimal na faixa [-10, +10]
def bin_to_dec(bin_array):
    return -10 + (np.dot(bin_array, 2**np.arange(len(bin_array))) / (2**len(bin_array) - 1)) * 20

# Converte um número decimal na faixa [-10, +10] para um vetor binário de 10 bits
def dec_to_bin(x):
    x = (x + 10) / 20 * (2**10 - 1)  # Normaliza o valor para o intervalo [0, 1023]
    return np.array(list(np.binary_repr(int(x), width=10)), dtype=int)

# Inicializa a população com um número dado de indivíduos, gerando valores aleatórios para x
def initialize_population(size):
    return [dec_to_bin(random.uniform(-10, 10)) for _ in range(size)]

# Seleciona pais da população usando o método especificado (torneio ou roleta)
def selection(population, fitness, method='tournament'):
    if method == 'tournament':
        idx = random.sample(range(len(population)), 2)  # Seleciona dois índices aleatórios
        return population[idx[0]] if fitness[idx[0]] < fitness[idx[1]] else population[idx[1]]
    elif method == 'roulette':
        total_fitness = sum(fitness)  # Soma as fitness
        pick = random.uniform(0, total_fitness)  # Seleciona um valor aleatório
        current = 0
        for i, f in enumerate(fitness):
            current += f
            if current > pick:
                return population[i]  # Retorna o indivíduo correspondente

# Realiza o crossover entre dois pais para gerar dois filhos
def crossover(parent1, parent2, crossover_type='one_point'):
    point = random.randint(1, len(parent1) - 1)  # Ponto de crossover
    if crossover_type == 'one_point':
        child1 = np.concatenate((parent1[:point], parent2[point:]))  # Crossover de um ponto
        child2 = np.concatenate((parent2[:point], parent1[point:]))
    else:  # Crossover de dois pontos
        point2 = random.randint(point + 1, len(parent1) - 1)
        child1 = np.concatenate((parent1[:point], parent2[point:point2], parent1[point2:]))
        child2 = np.concatenate((parent2[:point], parent1[point:point2], parent2[point2:]))
    return child1, child2

# Aplica mutação a um indivíduo com uma taxa de mutação especificada
def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:  # Verifica se a mutação deve ocorrer
            individual[i] = 1 - individual[i]  # Inverte o gene (0 <-> 1)
    return individual

# Executa o algoritmo genético para minimizar a função f
def genetic_algorithm(pop_size=10, mutation_rate=0.01, generations=50, crossover_type='one_point', selection_method='tournament', elitism=False, elite_percentage=0.1):
    population = initialize_population(pop_size)  # Inicializa a população
    
    for generation in range(generations):
        fitness = [f(bin_to_dec(ind)) for ind in population]  # Avalia a fitness de cada indivíduo
        
        # Elitismo: guarda os melhores indivíduos da geração anterior
        if elitism:
            elite_count = int(elite_percentage * pop_size)
            elite_indices = np.argsort(fitness)[:elite_count]  # Índices dos melhores indivíduos
            new_population = [population[i] for i in elite_indices]
        else:
            new_population = []
        
        # Cria novos indivíduos até que a nova população atinja o tamanho desejado
        while len(new_population) < pop_size:
            parent1 = selection(population, fitness, method=selection_method)  # Seleciona o primeiro pai
            parent2 = selection(population, fitness, method=selection_method)  # Seleciona o segundo pai
            child1, child2 = crossover(parent1, parent2, crossover_type=crossover_type)  # Realiza o crossover
            new_population.append(mutate(child1, mutation_rate))  # Aplica mutação ao primeiro filho
            if len(new_population) < pop_size:
                new_population.append(mutate(child2, mutation_rate))  # Aplica mutação ao segundo filho
        
        population = new_population  # Atualiza a população

    # Encontra o melhor indivíduo da população final
    best_idx = np.argmin([f(bin_to_dec(ind)) for ind in population])
    best_individual = population[best_idx]
    best_value = bin_to_dec(best_individual)  # Converte o melhor indivíduo para valor decimal
    min_value = f(best_value)  # Calcula o valor mínimo da função f

    return best_value, min_value  # Retorna o melhor valor de x e seu resultado

# Execução do algoritmo e exibição da saída
if __name__ == "__main__":
    best_x, minimum_f = genetic_algorithm()  # Executa o algoritmo genético
    print(f"O melhor valor de x é: {best_x}, que resulta em f(x) = {minimum_f}")  # Exibe o resultado

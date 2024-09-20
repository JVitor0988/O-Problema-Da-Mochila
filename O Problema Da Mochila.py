import random

def fitness(individual, pesos_e_valores, peso_maximo):
    peso_total = sum(p * w for p, w in zip(individual, pesos_e_valores))
    valor_total = sum(v * i for v, i in zip(individual, pesos_e_valores))
    if peso_total > peso_maximo:
        return 0
    return valor_total

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # Flip the bit
    return individual

def genetic_knapsack(pesos_e_valores, peso_maximo, numero_de_cromossomos, geracoes):
    population = [random.choices([0, 1], k=len(pesos_e_valores)) for _ in range(numero_de_cromossomos)]
    mutation_rate = 0.1

    for _ in range(geracoes):
        population.sort(key=lambda ind: fitness(ind, pesos_e_valores, peso_maximo), reverse=True)
        new_population = population[:numero_de_cromossomos // 2]

        while len(new_population) < numero_de_cromossomos:
            parent1, parent2 = random.choices(population[:10], k=2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population

    best_individual = max(population, key=lambda ind: fitness(ind, pesos_e_valores, peso_maximo))
    best_value = fitness(best_individual, pesos_e_valores, peso_maximo)
    return best_value, best_individual

# Exemplo de uso
pesos_e_valores = [[2, 10], [4, 30], [6, 300], [8, 10], [8, 30], [8, 300], [12, 50], [25, 75], [50, 100], [100, 400]]
peso_maximo = 100
numero_de_cromossomos = 150
geracoes = 50

melhor_valor, melhor_individuo = genetic_knapsack(pesos_e_valores, peso_maximo, numero_de_cromossomos, geracoes)
print("Melhor valor encontrado:", melhor_valor)
print("Melhor indivíduo (0/1 para cada item):", melhor_individuo)

import random

WEIGHTS = {
    "cost": 0.4,
    "cpu": 0.2,
    "memory": 0.2,
    "distance": 0.2
}

POPULATION_SIZE = 10
GENERATIONS = 20
MUTATION_RATE = 0.1


def generate_solution():
    return {
        "cost": random.randint(5, 20),
        "cpu": random.randint(1, 16),
        "memory": random.randint(2, 64),
        "distance": random.randint(10, 100)
    }


def fitness(sol):
    return (
        WEIGHTS["cost"] * sol["cost"] +
        WEIGHTS["cpu"] * sol["cpu"] +
        WEIGHTS["memory"] * sol["memory"] +
        WEIGHTS["distance"] * sol["distance"]
    )


def select(population):
    a = random.choice(population)
    b = random.choice(population)
    return a if fitness(a) < fitness(b) else b


def crossover(p1, p2):
    return {
        key: random.choice([p1[key], p2[key]])
        for key in p1
    }


def mutate(solution):
    if random.random() < MUTATION_RATE:
        solution["cost"] = random.randint(5, 20)
    if random.random() < MUTATION_RATE:
        solution["cpu"] = random.randint(1, 16)
    if random.random() < MUTATION_RATE:
        solution["memory"] = random.randint(2, 64)
    if random.random() < MUTATION_RATE:
        solution["distance"] = random.randint(10, 100)
    return solution


population = [generate_solution() for _ in range(POPULATION_SIZE)]

for gen in range(GENERATIONS):
    new_population = []

    for _ in range(POPULATION_SIZE):
        parent1 = select(population)
        parent2 = select(population)

        child = crossover(parent1, parent2)
        child = mutate(child)

        new_population.append(child)

    population = new_population


best = min(population, key=fitness)

print("🚀 BEST OPTIMIZED DEPLOYMENT:")
print(best)
print("Fitness Score:", fitness(best))

import random

dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(dist)

def fitness(route):
    total = 0
    for i in range(n - 1):
        total += dist[route[i]][route[i+1]]
    total += dist[route[-1]][route[0]]
    return total

population = []
for _ in range(10):
    route = list(range(n))
    random.shuffle(route)
    population.append(route)

for generation in range(100):
    population.sort(key=fitness)
    new_population = population[:2]
    while len(new_population) < 10:
        parent = random.choice(population[:5])
        child = parent[:]
        i, j = random.sample(range(n), 2)
        child[i], child[j] = child[j], child[i]
        new_population.append(child)
    population = new_population

best_route = min(population, key=fitness)

print("Best Route:", best_route)
print("Minimum Distance:", fitness(best_route))
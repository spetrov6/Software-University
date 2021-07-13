population = [int(i) for i in input().split(", ")]
min_wealth = int(input())
equal_wealth = True
for i in range(len(population)):
    needed_wealth = min_wealth - population[i]
    if population[population.index(max(population))] - needed_wealth >= min_wealth:
        while population[i] < min_wealth:
            population[i] += needed_wealth
            population[population.index(max(population))] -= needed_wealth
    else:
        print("No equal distribution possible")
        equal_wealth = False
        break
if equal_wealth:
    print(population)
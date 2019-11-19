from myclass import nkclass
from population import create_population
from population import get_fitnesses
from population import reproduce
from population import mutate
import itertools
import random
import numpy

# random.seed(100)
# numpy.random.seed(100)

genotype_counter = itertools.count(0)
population_size = 10E5
mutation_rate = 10E-6
maxf = 0

pop_map = dict()
fitness_map = dict()

pop = create_population(population_size, genotype_counter, nkclass, pop_map)
for i in range(50000):
  pop = get_fitnesses(pop, fitness_map)
  # if i % 10000 == 0:
  #   print(pop.vs['fitness'])
  #   print(pop.vs['num_mutations'])
    # print(pop.vs['frequency'])
    # average = 0
    # for fit, freq in zip(pop.vs['fitness'], pop.vs['frequency']):
    #   average += fit * freq

    # print(average)
    #print(average, max(pop.vs['fitness']))
    #print(len(pop.vs['frequency']))
  newmax = max(pop.vs['fitness'])
  if (newmax > maxf):
    maxf = newmax
    print(newmax)
    # print(pop.vs.find(fitness=maxf)['num_mutations'])
  pop = reproduce(pop, population_size)
  pop = mutate(pop, population_size, mutation_rate, genotype_counter, pop_map)

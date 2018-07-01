import random
import math
from StoppingCondition import StoppingCondition
from CrossoverOperator import CrossoverOperator
from GeneticProblem import GeneticProblem


class GeneticAlgorithm:

    def __init__(self, population_size, tournament_arity, elitism_rate, mutation_rate, stopping_condition,
                 crossover_operator):

        assert population_size > 0
        assert 0 < tournament_arity <= population_size
        assert 0 <= elitism_rate <= 1
        assert 0 <= mutation_rate <= 1
        assert isinstance(stopping_condition, StoppingCondition)
        assert isinstance(crossover_operator, CrossoverOperator)

        self.population_size = population_size
        self.tournament_arity = tournament_arity
        self.elitism_rate = elitism_rate
        self.mutation_rate = mutation_rate
        self.stopping_condition = stopping_condition
        self.crossover_operator = crossover_operator
        self.genetic_problem = None

    def instantiate_problem(self, genetic_problem):

        assert isinstance(genetic_problem, GeneticProblem)

        self.genetic_problem = genetic_problem

    def __random_population(self):

        return [self.__random_chromosome() for _ in range(self.population_size)]

    def __random_chromosome(self):

        assert self.genetic_problem is not None

        return [random.choice(self.genetic_problem.genes) for _ in range(self.genetic_problem.individual_length)]

    def __elitistic_split(self, population):

        limit = int(math.ceil(len(population) * self.elitism_rate))

        return population[:limit], population[limit:]


    def execute(self):

        sortedPopulation = sorted(self.__random_population(), key=lambda x: self.genetic_problem.fitness(x))

        while not self.stopping_condition.is_satisfied():
            splittedPopulation = self.__elitistic_split(sortedPopulation)
            print(splittedPopulation)





import random

class GeneticAlgorithm:

    def __init__(self, population_size, tournament_arity, elitism_rate, mutation_rate, stopping_condition,
                 crossover_operator):

        assert population_size > 0
        assert 0 < tournament_arity <= population_size
        assert 0 <= elitism_rate <= 1
        assert 0 <= mutation_rate <= 1
        assert isinstance(stopping_condition, GeneticAlgorithm)
        assert isinstance(crossover_operator, GeneticAlgorithm)

        self.population_size = population_size
        self.tournament_arity = tournament_arity
        self.elitism_rate = elitism_rate
        self.mutation_rate = mutation_rate
        self.stopping_condition = stopping_condition
        self.crossover_operator = crossover_operator
        self.genetic_problem = None

    def instantiate_problem(self, genetic_problem):

        assert isinstance(genetic_problem, GeneticAlgorithm)

        self.genetic_problem = genetic_problem

    def __random_population(self):

        return [self.__random_chromosome() for _ in range(self.population_size)]

    def __random_chromosome(self):

        assert self.genetic_problem is not None

        return [random.choice(self.genetic_problem.genes) for _ in range(self.genetic_problem.individual_length)]

    def evolve(self):

        initial_population = self.__random_population()



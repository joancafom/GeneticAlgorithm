from GeneticAlgorithm import GeneticAlgorithm
from StoppingCondition import StoppingCondition
from CrossoverOperator import CrossoverOperator
from GeneticProblem import GeneticProblem
from StoppingCondition import ElapsedTimeStoppingCondition

class SimpleStoppingCondition(StoppingCondition):

    def __init__(self):
        pass

    def is_satisfied(self):
        return True


class SimpleCrossOver(CrossoverOperator):

    def crossover(self, ch1, ch2):
        return True


class SimpleGeneticProblem(GeneticProblem):

    def decode(self, chromosome):
        pass

    def fitness(self, chromosome):
        pass


sc = ElapsedTimeStoppingCondition(0.0008)
co = SimpleCrossOver()
gp = SimpleGeneticProblem(["a", "b", "c"], 2)
ga = GeneticAlgorithm(2, 2, 0.2, 0.9, sc, co)
ga.instantiate_problem(gp)
print(ga.execute())

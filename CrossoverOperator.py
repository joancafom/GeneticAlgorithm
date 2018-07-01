import random
from abc import ABCMeta, abstractmethod


class CrossoverOperator:

    __metaclass__ = ABCMeta

    @abstractmethod
    def crossover(self, ch1, ch2):
        pass


class OnePointCrossover(CrossoverOperator):

    def crossover(self, ch1, ch2):

        assert len(ch1) > 1
        assert len(ch1) == len(ch2)

        point = random.randint(1, len(ch1) - 1)

        chr1 = ch1[:point] + ch2[point:]
        chr2 = ch2[:point] + ch1[point:]

        return chr1, chr2


class TwoPointsCrossover(CrossoverOperator):

    def crossover(self, ch1, ch2):

        assert len(ch1) > 2
        assert len(ch1) == len(ch2)

        point1 = random.randint(1, len(ch1) - 2)
        point2 = random.randint(point1, len(ch1) - 1)

        chr1 = ch1[:point1] + ch2[point1:point2] + ch1[point2:]
        chr2 = ch2[:point1] + ch1[point1:point2] + ch2[point2:]

        return chr1, chr2


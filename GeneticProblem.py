from abc import ABCMeta, abstractmethod


class GeneticProblem:

    __metaclass__ = ABCMeta

    def __init__(self, genes, individual_length):

        self.genes = genes
        self.individual_length = individual_length

    @abstractmethod
    def decode(self, chromosome):
        pass

    @abstractmethod
    def fitness(self, chromosome):
        pass

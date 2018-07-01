from abc import ABCMeta, abstractmethod
import datetime


class StoppingCondition:

    __metaclass__ = ABCMeta

    @abstractmethod
    def is_satisfied(self):
        pass

    @abstractmethod
    def update(self):
        pass


class ElapsedTimeStoppingCondition(StoppingCondition):

    # Time in seconds must be provided
    def __init__(self, time):
        self.initTime = datetime.datetime.now()
        self.time = datetime.timedelta(seconds=time)

    def is_satisfied(self):
        now = datetime.datetime.now()

        return (now - self.initTime) >= self.time

    def update(self):
        pass


class NumGenerationsStoppingCondition(StoppingCondition):

    def __init__(self, max_generations):
        self.maxGenerations = max_generations
        self.currentGen = 0

    def is_satisfied(self):
        return self.currentGen == self.maxGenerations

    def update(self):
        self.currentGen += 1

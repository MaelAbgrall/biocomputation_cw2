# python integrated
import time

# dependencies
import numpy

# local files

class GeneticAlgorithm ():

    def __init__(self, pop_size, lower_bound, upper_bound, selection_percentage, mutation_factor, function_to_optimize, path=None):
        
        self.pop_size = pop_size
        
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

        self.select_percentage = selection_percentage
        self.mutation_factor = mutation_factor

        self.path = path
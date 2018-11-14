# dependencies
import numpy

# local files

class GeneticAlgorithm ():

    def __init__(self, pop_size, child_percentage, tournament_size, mutation_factor, plateau_lengh, max_epoch=None, debug=False):
        """use a genetic algorithm to minimise a function
        
        Arguments:
            pop_size {int} -- population size
            child_percentage {float} -- percentage of child to create (eg. 0.75)
            tournament_size {float} -- percentage of parent to pick up for a tournament (eg. 0.75)
            mutation_factor {float} -- percentage of child to mutate (eg. 0.1)
            plateau_lengh {int} -- stop criterion: how many epoch the algorithm can do without improvement
        
        Keyword Arguments:
            max_epoch {int} -- if not none, the algorithm will stop either if there is no improvement (plateau) or the maximum number of epoch has been reached (default: {None})
            debug {bool} -- show debug prints (default: {False})
        """

        self.pop_size = pop_size

        self.tournament_size = int(tournament_size * pop_size)
        self.child_percentage = child_percentage
        self.mutation_factor = mutation_factor

        self.history = []
        self.plateau_lengh = plateau_lengh
        self.max_epoch = max_epoch

        self.debug = debug

    def optimize(self, lower_bound, upper_bound, function_to_optimize):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.function_to_optimize = function_to_optimize

        # creating the population
        population = self._create_population()

        # first evaluation
        population = self._evaluate(population)

        # loop until self._stop() return true
        iteration = 0
        while(True):
            
            # should we stop ?
            stop_criterion = self._stop(population, iteration)
            if(stop_criterion == True):
                break

            # if not stop, update population
            # select parents
            parent1, parent2 = self._select_parent(population)
            # crossover
            child = self._crossover(parent1, parent2)
            # mutate
            child = self._mutate(child)
            # evaluate childs
            child = self._evaluate(child)

            # merge child and original population and resize to pop_size
            population = self._kill_weakest(population, child)


            # keep track of how many loop were done
            iteration += 1
        # end of while
        
        sorted_population = numpy.sort(population, axis=0)
        best_sample = sorted_population[0]
        
        if(self.debug == True):
            print("stop at iteration", iteration)
            print("best sample:", best_sample)

        return best_sample, iteration
    
    def _create_population(self):
        """create a random population
        
        Returns:
            [stacked array] -- [array_x, array_y] of shape [pop_size, 2]
        """

        array_x = numpy.random.randint(self.lower_bound, self.upper_bound, size=self.pop_size)
        array_y = numpy.random.randint(self.lower_bound, self.upper_bound, size=self.pop_size)
        return numpy.stack([array_x, array_y], axis=1) 

    def _evaluate(self, population):
        """
            solve the function using the population
        """
        result = self.function_to_optimize.solve(population[:, 0], population[:, 1])
        population = numpy.stack([population[:, 0], population[:, 1], result], axis=1)
        return population
    
    def _stop(self, population, iteration):
        # pick up the best sample
        sorted_population = numpy.sort(population, axis=0)
        best_sample = sorted_population[0]

        # add it to history
        self.history.append(best_sample)
        
        # check history evolution, does it converge ?
        if(len(self.history) >= self.plateau_lengh):
            # convert the last samples to a numpy array (more easy to handle)
            array_hist = numpy.array(self.history[-self.plateau_lengh:])
            # if all the elements are identical
            if(numpy.unique(array_hist[:, 2]).shape[0] == 1):
                return True
        
        # at last, if we did too many iteration
        if(self.max_epoch is not None and iteration+1 > self.max_epoch):
            return True

        # else, we continue
        return False
    
    def _select_parent(self, population):
        nb_child = int(self.child_percentage * population.shape[0])
        
        parent1 = []
        parent2 = []
        # for each child
        for _ in range(nb_child):
            # we select two parent
            parent1.append(self._tournament_select(population))
            parent2.append(self._tournament_select(population))
        
        parent1 = numpy.array(parent1)
        parent2 = numpy.array(parent2)

        return (parent1, parent2)
    
    def _tournament_select(self, population):
        # choosing random position in the population
        positions = numpy.random.randint(0, population.shape[0], self.tournament_size)
        # picking those samples
        picked_parents = population[positions]
        # sort and take the best
        sorted_parents = numpy.sort(picked_parents, axis=0)
        return sorted_parents[0]

    def _crossover(self, parent1, parent2):
        child_population = []
        for position in range(len(parent1)):
            x_prime = parent1[position, 0]
            y_prime = parent1[position, 1]

            x_double = parent2[position, 0]
            y_double = parent2[position, 1]

            # P1 = x', y'  P2 = x", y"  C1 = x',y"   C2 = x", y'
            child1 = numpy.array([x_prime, y_double])
            chidl2 = numpy.array([x_double, y_prime])

            child_population.append(child1)
            child_population.append(chidl2)
           
        child_population = numpy.array(child_population)
        return child_population

    def _mutate(self, child_population):
        # random position           size = percentage of child
        positions = numpy.random.randint(0, child_population.shape[0], size=int(self.mutation_factor * child_population.shape[0]))
        # pick
        picked_child = child_population[positions]
        # random mutate
        #    explanation: first random, between 0 and 1 will indicate which values to change. second random will indicate what value to change
        #    0 = don't change
        #    1 = change
        #    eg:    0 0 1 1 * 6 5 8 9 = 0 0 8 9, only x3 and x4 will change
        mutation_x = numpy.random.randint(2, size=picked_child.shape[0]) * numpy.random.randint(self.lower_bound, self.upper_bound, size=picked_child.shape[0])
        mutation_y = numpy.random.randint(2, size=picked_child.shape[0]) * numpy.random.randint(self.lower_bound, self.upper_bound, size=picked_child.shape[0])        
        
        mutation = numpy.stack([mutation_x, mutation_y], axis=1)

        # replace
        # ineficient inelegant solution, but numpy can be a pain sometime
        for pos in range(mutation.shape[0]):
            if(mutation[pos, 0] != 0):
                picked_child[pos, 0] = mutation[pos, 0]
            if(mutation[pos, 1] != 0):
                picked_child[pos, 1] = mutation[pos, 1]
        
        # place back on the array
        child_population[positions] = picked_child
        return child_population

    def _kill_weakest(self, population, child):
        # merge
        population = numpy.concatenate((population, child), axis=0)
        # sort
        population = numpy.sort(population, axis=0)
        # kill the weakest (it can be a child or a parent)
        population = population[:self.pop_size]
        return population
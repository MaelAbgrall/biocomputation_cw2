import numpy

class ParticleSwarmOptimization():
    def __init__(self, pop_size, intertia_weight, cognitive_weight, social_weight, plateau_lengh, max_epoch=None, debug=False):
        
        self.pop_size = pop_size

        self.inertia = intertia_weight
        self.cognitive = cognitive_weight
        self.social = social_weight

        self.plateau_lengh = plateau_lengh
        self.max_epoch = max_epoch
        self.history = []
        self.be = []

        self.debug = debug
    
    def optimize(self, lower_bound, upper_bound, function_to_optimize):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.function_to_optimize = function_to_optimize

        # create population
        population = self._create_population()
        
        # evaluate
        result = self._evaluate(population)
        population = numpy.stack([population[:, 0], population[:, 1], population[:, 2], population[:, 3], result], axis=1)
        
        # select best element locally and globally
        population = self._select_best(population)

        # update velocity
        velocity_x, velocity_y = self._update_velocity(population)
        population[:, 2] = velocity_x
        population[:, 3] = velocity_y

        # update positions
        pos_x, pos_y = self._update_position(population)
        population[:, 0] = pos_x
        population[:, 1] = pos_y

        # re-evaluating 
        result = self._evaluate(population)
        population[:, 4] = result

        # loop until self._stop() return true (stop criterion)
        iteration = 0
        while(True):
            # should we stop ?
            stop_criterion = self._stop(population, iteration)
            if(stop_criterion == True):
                break

            # select best
            population = self._select_best(population)

            # update velocity
            velocity_x, velocity_y = self._update_velocity(population)
            population[:, 2] = velocity_x
            population[:, 3] = velocity_y

            # update positions
            pos_x, pos_y = self._update_position(population)
            population[:, 0] = pos_x
            population[:, 1] = pos_y

            # evaluate
            result = self._evaluate(population)
            population[:, 4] = result

            # keep track of how many loop were done
            iteration += 1
            #TODO
            print("iteration", iteration)
            """sorted_population = numpy.sort(population, axis=0)
            best_sample = sorted_population[0]
            print("best sample:", best_sample)"""

        # end of while

        sorted_population = numpy.sort(population, axis=0)
        best_sample = sorted_population[0]
        
        if(self.debug == True):
            print("stop at iteration", iteration)
            print("best sample:", best_sample)

        return best_sample, iteration


    def _create_population(self):
        x_pos = numpy.random.randint(self.lower_bound, self.upper_bound, size=self.pop_size)
        y_pos = numpy.random.randint(self.lower_bound, self.upper_bound, size=self.pop_size)
        velocity_x = numpy.random.uniform(-10., 10., size=self.pop_size)
        velocity_y = numpy.random.uniform(-10., 10., size=self.pop_size)
        return numpy.stack([x_pos, y_pos, velocity_x, velocity_y], axis=1)

    def _evaluate(self, population):
        """
            solve the function using the population
        """
        result = self.function_to_optimize.solve(population[:, 0], population[:, 1])
        return result

    def _stop(self, population, iteration):
        # pick up the best sample
        sorted_population = numpy.sort(population, axis=0)
        best_sample = sorted_population[0]
        bess = sorted_population[0, 4]
        self.be.append(bess)
        # add it to history
        self.history.append(best_sample)
        
        # check history evolution, does it converge ?
        if(len(self.history) >= self.plateau_lengh):
            # convert the last samples to a numpy array (more easy to handle)
            array_hist = numpy.array(self.history[-self.plateau_lengh:])
            # if all the elements are identical
            print("n", numpy.unique(array_hist[:, 4]).shape[0])
            if(numpy.unique(array_hist[:, 4]).shape[0] == 1):
                return True
        if(iteration >=500):
            import ipdb; ipdb.set_trace()
        # at last, if we did too many iteration
        if(self.max_epoch is not None and iteration+1 > self.max_epoch):
            return True

        # else, we continue
        return False

    def _select_best(self, population):
        # select best overall
        #    sort
        sorted_pop = numpy.sort(population, axis=0)
        #    take the best of all
        self.best_sample = sorted_pop[0]
        
        # select best local
        # since at first call we don't have a local minimum
        if(population.shape[1] <=5):
            population_updated = numpy.stack([
                population[:, 0], 
                population[:, 1], 
                population[:, 2],
                population[:, 3],
                population[:, 4],
                population[:, 0], 
                population[:, 1],
                population[:, 4]], axis=1)

        if(population.shape[1] > 5):
            # unwanted for loop, but lack of time + obscure numpy functions
            population_updated = []
            for position in range(population.shape[0]):
                # if the new position is better, update the local best
                if(population[position, 3] < population[position, 6]):
                    population_updated.append(
                        numpy.array([
                            population[position, 0], 
                            population[position, 1], 
                            population[position, 2],
                            population[position, 3],
                            population[position, 4],
                            population[position, 0], 
                            population[position, 1],
                            population[position, 4]])
                    )
                
                # else, leave it
                if(population[position, 3] >= population[position, 6]):
                    population_updated.append(population[position])
            # end of for element in population
            population_updated = numpy.array(population_updated)
        return population_updated

    def _update_velocity(self, population):
        random_cognitive_x = numpy.random.random_sample(self.pop_size)
        random_cognitive_y = numpy.random.random_sample(self.pop_size)
        random_social_x = numpy.random.random_sample(self.pop_size)
        random_social_y = numpy.random.random_sample(self.pop_size)

        # cognitive = Cweight * random * (Pbest - Pactual)
        try:
            cognitive_x = self.cognitive * random_cognitive_x * (population[:, 5] - population[:, 0])
        except:
            import ipdb; ipdb.set_trace()
        cognitive_y = self.cognitive * random_cognitive_y * (population[:, 6] - population[:, 1])

        # social = SocWeight * random * (Pbest_all - Pactual)
        social_x = self.social * random_social_x * (self.best_sample[0] - population[:, 0])
        social_y = self.social * random_social_y * (self.best_sample[1] - population[:, 1])
        
        # velocity = inertia * velocityX 
        velocity_x = self.inertia * population[:, 2] + cognitive_x + social_x
        velocity_y = self.inertia * population[:, 3] + cognitive_y + social_y

        return velocity_x, velocity_y

    def _update_position(self, population):
        # position + velocity = new pos
        positions_x = population[:, 0] + population[:, 2]
        positions_y = population[:, 1] + population[:, 3]
        # correct out of boundaries values
        positions_x = numpy.clip(positions_x, self.lower_bound, self.upper_bound)
        positions_y = numpy.clip(positions_y, self.lower_bound, self.upper_bound)
        return positions_x, positions_y
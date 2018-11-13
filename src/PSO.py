import numpy

class ParticleSwarmOptimization():
    def __init__(self, pop_size, intertia_weight, cognitive_weight, social_weight, plateau_lengh, max_epoch=None, debug=False):
        
        self.pop_size = pop_size

        self.inertia = intertia_weight
        self.cognitive = cognitive_weight
        self.social = social_weight

        self.plateau_lengh = plateau_lengh
        self.max_epoch = max_epoch

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
        population = self._update_velocity(population)


        return best_sample, iteration


    def _create_population(self):
        x_pos = numpy.random.randint(self.lower_bound, self.upper_bound, size=self.pop_size)
        y_pos = numpy.random.randint(self.lower_bound, self.upper_bound, size=self.pop_size)
        velocity_x = numpy.random.uniform(-1., 1., size=self.pop_size)
        velocity_y = numpy.random.uniform(-1., 1., size=self.pop_size)
        return numpy.stack([x_pos, y_pos, velocity_x, velocity_y], axis=1)

    def _evaluate(self, population):
        """
            solve the function using the population
        """
        result = self.function_to_optimize.solve(population[:, 0], population[:, 1])
        return result

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
                        numpy.stack([
                            population[:, 0], 
                            population[:, 1], 
                            population[:, 2],
                            population[:, 3],
                            population[:, 4],
                            population[:, 0], 
                            population[:, 1],
                            population[:, 4]], axis=1)
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
        cognitive_x = self.cognitive * random_cognitive_x * (population[:, 5] - population[:, 0])
        cognitive_y = self.cognitive * random_cognitive_y * (population[:, 6] - population[:, 1])

        # social = SocWeight * random * (Pbest_all - Pactual)
        social_x = self.social * random_social_x * (self.best_sample[:, 0] - population[:, 0])
        social_y = self.social * random_social_y * (self.best_sample[:, 1] - population[:, 1])
        
        # velocity = inertia * velocityX 
        velocity_x = self.inertia * population[:, 2] + cognitive_x + social_y
        velocity_y = self.inertia * population[:, 3] + cognitive_y + social_y
        
        import ipdb; ipdb.set_trace()
        population_updated = 0
        return population_updated
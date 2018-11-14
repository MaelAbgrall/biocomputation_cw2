# integrated
import sys
import os
import time

# dependencies
import numpy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# local dependencies
from PSO import ParticleSwarmOptimization
from GA import GeneticAlgorithm
import benchmarkFunctions as benchmark

if("-ga" in sys.argv):
    alg_type = "ga"

if("-pso" in sys.argv):
    alg_type = "pso"

if("-ga" not in sys.argv and "-pso" not in sys.argv):
    print("please select an optimizer with -ga or -pso")
    exit()


# debug ?
debug = True

# if debug, create result directory
path = None
if(debug == False):
    path = "result/" + "test_" + alg_type + "_" + str(time.time())
    os.makedirs(path, exist_ok=True)


sizes = [1000, 50, 100, 500, 1000]
benchmark_list = [benchmark.Matyas(), benchmark.Booth(
), benchmark.HolderTable(), benchmark.EggHolder(), benchmark.Himmelblau()]

lower_bound_list = [-10, -10, -10, -512, -5]
upper_bound_list = [10, 10, 10, 512, 5]

# how many benchmark will be done
passage = 1
# how many epoch without improvement before stopping the algorithm
plateau_lengh = 50

#######################################
#    Genetic Algorithm PARAMETERS     #
#######################################
child_percentage=0.25
tournament_size=0.25
mutation_factor=0.1

###################################
#   Particle Swarm PARAMETERS     #
###################################
intertia_weight=.5
cognitive_weight=1
social_weight=2

"""if(debug == True):
    print("Booth")
    funct = benchmark.Booth()
    test = numpy.array([[1, 3]])
    funct.test(test[:, 0], test[:, 1], 0)

    print("Matyas")
    funct = benchmark.Matyas()
    test = numpy.array([[0, 0]])
    funct.test(test[:, 0], test[:, 1], 0)

    print("Hölder table")
    funct = benchmark.HolderTable()
    test = numpy.array([[8.05502, -9.66459]])
    funct.test(test[:, 0], test[:, 1], -19.208502567767606)

    print("Eggholder")
    funct = benchmark.EggHolder()
    test = numpy.array([[512, 404.2319]])
    funct.test(test[:, 0], test[:, 1], -959.6406627106155)

    print("Ackley")
    funct = benchmark.Ackley()
    test = numpy.array([[0, 0]])
    funct.test(test[:, 0], test[:, 1], 0)

    print("Himmelblau")
    funct = benchmark.Himmelblau()
    test = numpy.array([[3.0, 2.0]])
    funct.test(test[:, 0], test[:, 1], 0)
"""

# saving to csv (only if not debug)
time_output = "function, 10 sample, 50 sample, 100 sample, 500 sample, 1000 sample\n"
iteration_output = "function, 10 sample, 50 sample, 100 sample, 500 sample, 1000 sample\n"

# benchmarking
#   each function
for position in range(len(benchmark_list)):

    print("\nBenchmarking", benchmark_list[position].get_name())
    time_output += benchmark_list[position].get_name()
    iteration_output += benchmark_list[position].get_name()

    # benchmarking different population size
    for pop_size in sizes:

        time_output += ", "
        iteration_output += ", "

        print(pop_size, "elements")

        # repeat multiple time (passage)
        time_history = []
        iteration_history = []
        for _ in range(passage):

            if(alg_type == "ga"):
                optimizer_algorithm = GeneticAlgorithm(
                    pop_size,
                    child_percentage,
                    tournament_size,
                    mutation_factor,
                    plateau_lengh)
            if(alg_type == "pso"):
                optimizer_algorithm = ParticleSwarmOptimization(
                    pop_size,
                    intertia_weight,
                    cognitive_weight,
                    social_weight,
                    plateau_lengh)

            start_benchmark = time.time()

            best_sample, iteration = optimizer_algorithm.optimize(
                lower_bound=lower_bound_list[position],
                upper_bound=upper_bound_list[position],
                function_to_optimize=benchmark_list[position])

            end_benchmark = time.time()

            time_history.append(end_benchmark - start_benchmark)
            iteration_history.append(iteration - (plateau_lengh - 1))
        # end of for passages

        time_history = numpy.array(time_history)
        average_time = numpy.mean(time_history)
        print("mean time:", average_time)
        time_output += str(average_time)

        iteration_history = numpy.array(iteration_history)
        average_iteration = numpy.mean(iteration_history)
        print("mean iteration:", average_iteration)
        iteration_output += str(average_iteration)

    # end of for pop_size
    time_output += "\n"
    iteration_output += "\n"
# end of for benchmarks

if(debug == False):
    with open(path + "/algorithm_time_output.csv", "w+") as text_file:
        text_file.write(time_output)

    with open(path + "/algorithm_iteration_output.csv", "w+") as text_file:
        text_file.write(iteration_output)
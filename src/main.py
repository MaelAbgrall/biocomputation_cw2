# python integrated
import sys
import os
import time

# dependencies
import numpy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# local
import benchmarkFunctions as benchmark
from GA import GeneticAlgorithm

# debug ?
debug = True

# if debug, create result directory
path = None
if(debug == False):
    path = "result/" + "test_" + str(time.time())
    os.makedirs(path, exist_ok=True)

# init GA & PSO
pop_size = 1000         # 1000 elements

sizes = [10, 50, 100, 500, 1000]
benchmark_list = [benchmark.Matyas(), benchmark.Booth(
), benchmark.HolderTable(), benchmark.EggHolder(), benchmark.Himmelblau()]

passage = 100

if(debug == True):
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


# benchmarking
#   each function
result_list = []
for bench_fn in benchmark_list:

    print("\nBenchmarking", bench_fn.get_name())

    function_result = []
    # benchmarking different population size
    for pop_size in sizes:

        print(pop_size, "elements")

        ga = GeneticAlgorithm(pop_size=pop_size, child_percentage=0.25,
                              tournament_size=0.25, mutation_factor=0.1,
                              plateau_lengh=50)

        time_history = []
        for _ in range(passage):
            start_benchmark = time.time()
            ga.optimize(lower_bound=-10, upper_bound=10,
                        function_to_optimize=bench_fn)
            end_benchmark = time.time()
            time_history.append(end_benchmark - start_benchmark)
        time_history = numpy.array(time_history)
        average_time = numpy.mean(time_history)
        print("mean time:", average_time)
        function_result.append(numpy.array([pop_size, average_time]))

    # end of for pop_size
    function_result = numpy.array(function_result)
    result_list.append(function_result)

# end of for benchmarks

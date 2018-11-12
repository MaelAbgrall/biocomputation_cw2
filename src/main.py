#python integrated
import sys
import os
import time

# dependencies
import numpy

# local
import benchmarkFunctions as benchmark

# debug ?
debug = True

# if debug, create result directory
path = None
if(debug == False):
    path = "result/" + "test_" + str(time.time())
    os.makedirs(path, exist_ok=True)

# init GA & PSO
pop_size = 1000         # 1000 elements

# GA only
selection_percentage = 0.5  # kill 50% of the population per epoch
mutation_factor = 0.1   # mutate 10% of the elements after breeding

# PSO only


# TODO debug
#population = numpy.array([[1, 7], [3, 8], [2, 9]])
# numpy.sort(population, axis=1)

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



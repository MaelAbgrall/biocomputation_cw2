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
trash_percentage = 0.5  # kill 50% of the population per epoch
mutation_factor = 0.1   # mutate 10% of the elements after breeding

# PSO only


# TODO debug
#population = numpy.array([[1, 7], [3, 8], [2, 9]])
# numpy.sort(population, axis=1)

population = numpy.array([[1, 3], [1, 7]])
res_bo = benchmark.booth(population[:, 0], population[:, 1])
if(res_bo[0, 2] == 0):
    print("booth pass")
if(res_bo[0, 2] != 0):
    print("booth fail, result=", res_bo[0, 2], " expected=", 0)

population = numpy.array([[0, 0], [1, 7]])
res_mat = benchmark.matyas(population[:, 0], population[:, 1])
if(res_mat[0, 2] == 0):
    print("matyas pass")
if(res_mat[0, 2] != 0):
    print("matyas fail, result=", res_mat[0, 2], " expected=", 0)

population = numpy.array([[8.05502, -9.66459], [1, 7]])
res_ho = benchmark.holder_table(population[:, 0], population[:, 1])
if(res_ho[0, 2] == -19.208502567767606):
    print("holder pass")
if(res_ho[0, 2] != -19.208502567767606):
    print("holder fail, result=", res_ho[0, 2], " expected=", -19.208502567767606)

population = numpy.array([[512, 404.2319], [1, 7]])
res_egg = benchmark.eggholder(population[:, 0], population[:, 1])
if(res_egg[0, 2] == -959.6406627106155):
    print("eggholder pass")
if(res_egg[0, 2] != -959.6406627106155):
    print("eggholder fail, result=", res_egg[0, 2], " expected=", -959.6406627106155)

population = numpy.array([[0, 0], [1, 7]])
res_ac = benchmark.ackley(population[:, 0], population[:, 1])
if(res_ac[0, 2] == 0):
    print("ackley pass")
if(res_ac[0, 2] != 0):
    print("ackley fail, result=", res_ac[0, 2], " expected=", 0)

population = numpy.array([[3.0, 2.0], [1, 7]])
res_hi = benchmark.himmelblau(population[:, 0], population[:, 1])
if(res_hi[0, 2] == 0.0):
    print("himmelbleau pass")
if(res_hi[0, 2] != 0.0):
    print("himmelbleau fail, result=", res_hi[0, 2], " expected=", 0)
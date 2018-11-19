# Biologically inspired computation, coursework 2
Goal: implement a genetic algorithm (GA) and Particle Swarm Optimization (PSO), and benchmark them on a sample of functions

## how to use:
(unix)
```batch
source env/bin/activate

python main.py -ga

# or

python main.py -pso
```


(windows)
```batch
call env\Script\activate.bat

python main.py -pso

; or

python main.py -ga
```

## code
the code is commented a lot so it shouldn't be hard to understand it. It is mostly vectorized.

To add new benchmark function, there is an abstract class in BenchmarkFunction.py that you shoud use. You only need to implement get_name and solve(x, y). the latest should only return the result.


## results:

### GA:
#### Mean processing time in seconds (>=100 iterations)
function | 10 sample | 50 sample | 100 sample | 500 sample | 1000 sample |
| ---- | ---- | ----- | ---- | ---- | ---- |
| Matyas | 0.018352 | 0.053137 | 0.10877 | 0.834028 | 2.487554 |
| Booth | 0.017725 | 0.059882 | 0.110857 | 0.804131 | 2.388776 |
| Holder Table | 0.014722 | 0.049492 | 0.095943 | 0.769484 | 2.388653 |
| Eggholder | 0.032726 | 0.121665 | 0.2579 | 1.623453 | 4.061912 |
| Himmelblau | 0.016577 | 0.050138 | 0.098948 | 0.776121 | 2.395099 |

#### Mean iteration (- 100 iterations)
| function | 10 sample | 50 sample | 100 sample | 500 sample | 1000 sample |
| ---- | ---- | ----- | ---- | ---- | ---- |
| Matyas | 28.721 | 10.455 | 3.378 | 0.127 | 0.01 |
| Booth | 27.45 | 16.234 | 11.367 | 0.72 | 0.144 |
| Holder Table | 14.209 | 1.602 | 0.755 | 0.09 | 0.005 |
| Eggholder | 122.258 | 135.386 | 160.898 | 107.663 | 63.468 |
| Himmelblau | 22.6 | 7.971 | 2.93 | 0.024 | 0 |

#### Global minimum found (% on 1000 tests)
| function | 10 sample | 50 sample | 100 sample | 500 sample | 1000 sample |
| ---- | ---- | ----- | ---- | ---- | ---- |
| Matyas | 0.041 | 0.23 | 0.351 | 0.829 | 0.92 |
| Booth | 0.567 | 0.828 | 0.967 | 1 | 1 |
| Holder Table | 0 | 0 | 0 | 0 | 0 |
| Eggholder | 0 | 0 | 0 | 0 | 0 |
| Himmelblau | 0.829 | 0.997 | 1 | 1 | 1 |

### PSO
#### Mean processing time (s)
| function	| 10 sample	| 50 sample	| 100 sample	| 500 sample	| 1000 sample |
| ---- | ---- | ----- | ---- | ---- | ---- |
| Matyas	| 0.030928	| 0.053708	| 0.083029	| 0.311138	| 0.602298 |
| Booth	| 0.025702	| 0.049388	| 0.080727	| 0.325262	| 0.624594 |
| Holder Table	| 0.016746	| 0.031529	| 0.049911	| 0.200045	| 0.380206 |
| Eggholder	| 0.017949	| 0.031566	| 0.051696	| 0.229794	| 0.439115 |
| Himmelblau	| 0.020245	| 0.038009	| 0.059572	| 0.231943	| 0.443113 |

#### Mean iteration
| function	| 10 sample	| 50 sample	| 100 sample	| 500 sample	| 1000 sample |
| ---- | ---- | ----- | ---- | ---- | ---- |
| Matyas	| 275.942	| 312.558	| 319.297	| 351.393	| 371 |
| Booth	| 169.152	| 143.534	| 137.54	| 126.925	| 123.551 |
| Holder Table	| 106.724	| 98.463	| 96.615	| 94.122	| 92.164 |
| Eggholder	| 113.68	| 88.671	| 82.528	| 60.782	| 55.465 |
| Himmelblau	| 133.839	| 127.074	| 122.365	| 117.918	| 116.301 |

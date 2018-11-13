# python integrated
import math
from abc import ABC, abstractmethod

# dependencies
import numpy

class BenchMark(ABC):
    """abstract class, allow to do something.solve(x, y)
    """

    @abstractmethod
    def get_name(self):
        raise NotImplementedError

    @abstractmethod
    def solve(self, array_x, array_y):
        raise NotImplementedError
    
    def test(self, array_x, array_y, result):
        """test if a function is working as expected
        
        Arguments:
            array_x {numpy array} -- known input
            array_y {numpy array} -- known input
            result {float / int} -- known output
        """

        output = self.solve(array_x, array_y)

        if(output[0, 2] == result):
            print("pass")
        if(output[0, 2] != result):
            print("fail... \t Expected:", result, " Got:", output[0, 2])
            


class Booth(BenchMark):
    """execute booth function:

        (x+2y-7)² + (2x+y-5)²
    """
    def solve(self, array_x, array_y):
        """solve booth function:
        
        Arguments:
            array_x {numpy.array} -- value(s) of x
            array_y {numpy.array} -- value(s) of y
        
        Returns:
            full_array -- numpy.array [x1, y1, result1]
                                    [x2, y2, result2]

        """
        result = (array_x + 2 *array_y - 7) * (array_x + 2 *array_y - 7) + (2 * array_x + array_y - 5) * (2 * array_x + array_y - 5)
        
        full_array = numpy.stack([array_x, array_y, result], axis=1) 
        return full_array
    
    def get_name(self):
        return "Booth"
    
class Matyas(BenchMark):
    """execute Matyas function:

        0.26(x²+y²) - 0.48xy
    """
    def get_name(self):
        return "Matyas"

    def solve(self, array_x, array_y):
        """solve Matyas function:

        Arguments:
            array_x {numpy.array} -- value(s) of x
            array_y {numpy.array} -- value(s) of y
        
        Returns:
            full_array -- numpy.array [x1, y1, result1]
                                    [x2, y2, result2]

        """
        result = 0.26 *( array_x*array_x + array_y*array_y ) - 0.48 * array_x * array_y
        
        full_array = numpy.stack([array_x, array_y, result], axis=1) 
        return full_array
    
class HolderTable(BenchMark):
    """execute Hölder table function:

        - abs( sinx * cosy exp( abs( 1- (sqrt(x*x + y*y)/Pi))))
    """
    def get_name(self):
        return "Holder Table"

    def solve(self, array_x, array_y):
        """solve Hölder table function:

        Arguments:
            array_x {numpy.array} -- value(s) of x
            array_y {numpy.array} -- value(s) of y
        
        Returns:
            full_array -- numpy.array [x1, y1, result1]
                                    [x2, y2, result2]

        """
        result = - (numpy.absolute( numpy.sin(array_x) * numpy.cos(array_y) * numpy.exp( numpy.absolute( 1-(numpy.sqrt(array_x*array_x + array_y*array_y) / math.pi)) ) ))
        
        full_array = numpy.stack([array_x, array_y, result], axis=1) 
        return full_array

class EggHolder(BenchMark):
    """execute eggholder function:

        - (y+47) sin( sqrt( abs( x/2 + (y+47)))) - x sin( sqrt( abs( x - (y+47))))
    """
    def get_name(self):
        return "Eggholder"

    def solve(self, array_x, array_y):
        """solve eggholder function:

        Arguments:
            array_x {numpy.array} -- value(s) of x
            array_y {numpy.array} -- value(s) of y
        
        Returns:
            full_array -- numpy.array [x1, y1, result1]
                                    [x2, y2, result2]

        """
        result = - (array_y + 47) * numpy.sin( numpy.sqrt( numpy.abs( array_x/2 + (array_y +47) ) ) ) - array_x * numpy.sin( numpy.sqrt( numpy.abs( array_x - (array_y+47) ) ) )
        
        full_array = numpy.stack([array_x, array_y, result], axis=1) 
        return full_array

class Ackley(BenchMark):
    """execute ackley function:

        -20 exp(-0.2 sqrt(0.5(x² + y²))) - exp(0.5 * (cos(2xPi) + cos(2yPi))) + 20 + exp(1)
    """
    def get_name(self):
        return "Ackley"

    def solve(self, array_x, array_y):
        """solve ackley function:
        
        Arguments:
            array_x {numpy.array} -- value(s) of x
            array_y {numpy.array} -- value(s) of y
        
        Returns:
            full_array -- numpy.array [x1, y1, result1]
                                    [x2, y2, result2]

        """
        result = -20 * numpy.exp( -0.2 * numpy.sqrt( 0.5 * ( array_x*array_x + array_y*array_y) ) ) - numpy.exp( 0.5 * ( numpy.cos( 2*array_x*math.pi ) + numpy.cos( 2*array_y*math.pi ) ) ) + 20 + math.exp(1)
        
        full_array = numpy.stack([array_x, array_y, result], axis=1) 
        return full_array

class Himmelblau(BenchMark):
    """execute Himmelblau function:

        (x²+y-11)² + (x+y²-7)²
    """
    def get_name(self):
        return "Himmelblau"

    def solve(self, array_x, array_y):
        """solve Himmelblau function:
        
        Arguments:
            array_x {numpy.array} -- value(s) of x
            array_y {numpy.array} -- value(s) of y
        
        Returns:
            full_array -- numpy.array [x1, y1, result1]
                                    [x2, y2, result2]

        """
        result = (array_x*array_x + array_y - 11) * (array_x*array_x + array_y - 11) + (array_x + array_y*array_y -7) * (array_x + array_y*array_y -7)
        
        full_array = numpy.stack([array_x, array_y, result], axis=1) 
        return full_array
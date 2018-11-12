# python integrated
import math

# dependencies
import numpy

def booth(array_x, array_y):
    """execute booth function:

    (x+2y-7)² + (2x+y-5)²
    
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

def matyas(array_x, array_y):
    """execute Matyas function:

    0.26(x²+y²) - 0.48xy
    
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

def holder_table(array_x, array_y):
    """execute Hölder table function:

    - abs( sinx * cosy exp( abs( 1- (sqrt(x*x + y*y)/Pi))))

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

def eggholder(array_x, array_y):
    """execute eggholder function:

    - (y+47) sin( sqrt( abs( x/2 + (y+47)))) - x sin( sqrt( abs( x - (y+47))))

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

def ackley(array_x, array_y):
    """execute ackley function:

    -20 exp(-0.2 sqrt(0.5(x² + y²))) - exp(0.5 * (cos(2xPi) + cos(2yPi))) + 20 + exp(1)
    
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

def himmelblau(array_x, array_y):
    """execute Himmelblau function:

    (x²+y-11)² + (x+y²-7)²
    
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
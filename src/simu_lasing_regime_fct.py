

# external libraries 
from numpy import array, amin, diff, where, log





#---------------------------------------------------#
#---------------------------------------------------#

# write lasing regime on output file for each value 
# of the adjustable parameter


def write_cw(ofile,var) : 
    ofile.write('%.3e\t%i\n' % (var, 3e4))
    return 0

def write_pulse(ofile,var, pulse_duration) : 
    ofile.write('%.3e\t%.3e\n' % (var, pulse_duration))
    return 0

def write_no_lasing(ofile,var) : 
    ofile.write('%.3e\t%i\n' % (var, 0))
    return 0

def write_error(ofile,var) : 
    ofile.write('%.3e\t%i\n' % (var, 1e4))
    return 0

def write_undefined(ofile,var) : 
    ofile.write('%.3e\t%i\n' % (var, 2e4))
    return 0




def find_pulse_duration(time, intensity) :

    # conversion list -> numpy array
    time = array(time)
    intensity = array(intensity)
    
    # avoid log(0) errors
    intensity[intensity == 0] = 1e-20

    # intensity derivative
    dint = diff(log(intensity))
    
    # find the minimum
    idx = where(dint == amin(dint))

    return time[idx]


#---------------------------------------------------#
#---------------------------------------------------#





def write_guidelines_three_pop(ofile) :

    ofile.write(
'''
----------- guidelines -----------

column 1: value of the variable parameter
column 2: lasing regime 
    - no lasing    : 0
    - cw lasing    : 3e4
    - pulse lasing : pulse duration (s)
    - integration time too small to decide : 2e4

----------------------------------
'''
    )
    return 0

def write_guidelines_two_pop(ofile) :

    ofile.write(
'''
----------- guidelines -----------

column 1: value of the variable parameter
column 2: lasing regime 
    - no lasing    : 0
    - cw lasing    : 3e4

----------------------------------
'''
    )
    return 0

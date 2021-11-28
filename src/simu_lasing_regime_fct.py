'''
-------------------------------------------------------------------
This file is part of the OSS source code 
Copyright (C) 2021 Anthony Dall'agnol 

This program is free software: you can redistribute it and/or modify 
it under the terms of the GNU General Public License as published 
by the Free Software Foundation, either version 3 of the License, or 
any later version. 
This program is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
GNU General Public License for more details. 
You should have received a copy of the GNU General Public License 
along with this program. If not, see <https://www.gnu.org/licenses/>
-------------------------------------------------------------------

@author    : Anthony Dall'agnol
@copyright : Copyright (C) 2021 Anthony Dall'agnol
@license   : GNU General Public License

-------------------------------------------------------------------
@write_cw        : write on file that CW is reached + value of parameter
@write_pulse     : write on file the pulse duration + value of parameter
@write_no_lasing : write on file no lasing + value of parameter
@write_error     : write on file that an error occured
@write_undefined : write on file that regime is undefined

@find_pulse_duration : find the duration of the lasing pulse
@write_guidelines    : write on file tutorial to read the data

Called in: simu_lasing_regime.py, simu_lasing_regime_solver.py
-------------------------------------------------------------------
'''


# external libraries 
from numpy import array, amin, diff, where, log





#---------------------------------------------------#
#---------------------------------------------------#


'''
write lasing regime on output file for each value of 
the adjustable parameter (chosen by user)

To ease the process of data, regimes are written
in integer. 
CW        = 3e4
no lasing = 0 
error     = 1e4
undefined = 2e4

'''


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

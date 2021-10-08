# external libraries 
import numpy as np 
import os


# external files 
import system         as sys 
import imp_param      as imp 
import solver         as vs
import user_interface as ui



ui.welcome()


# photophysical parameters importation
const_molecule = imp.param_molecule()
const_sample   = imp.param_sample(const_molecule[0])
const_rates    = imp.param_rates(const_sample[2])






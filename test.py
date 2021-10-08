



# external libraries 
import numpy as np 
from scipy.integrate import odeint
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


# pump parameters importation
const_pump = imp.param_pump()


# time vector importation 
t = imp.param_time(const_pump[0])


# initial value for the populations S0,S1,T1
init_pop = [1,0,0]


# output file to write the data on 
output_file_path = 'test.out'
if os.path.exists(output_file_path) : os.remove(output_file_path)



# ode system integration 
sol = odeint(sys.sys_equations,init_pop,t,
        args=(const_sample[0],const_pump[1],const_sample,const_molecule,const_rates)
        )

ofile = open(output_file_path,'a+')
for ii in range(len(sol)) :
    ofile.write('%.3e\t%.3e\t%.3e\n'
    % (sol[ii,0],sol[ii,1],sol[ii,2])
    )
ofile.close()

import matplotlib.pyplot as plt 
plt.plot(t,sol[:,1])
plt.yscale('log')
plt.show()





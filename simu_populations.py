



# external libraries 
from scipy.integrate import odeint
import os


# external files 
import system     as sys 
import imp_param  as imp 
import simu_populations_solver as sv 
import user_interface as ui



def simu() : 

    ui.simulation_start()

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
    ui.output_file_choice()
    output_file_path = input('File path : ')
    if os.path.exists(output_file_path) : os.remove(output_file_path)



    sv.solver(odeint,sys.sys_equations,init_pop,t,const_sample[0],
            const_pump[1],
            const_sample,
            const_molecule,
            const_rates,
            output_file_path
        )






    ui.simulation_finished()    
    return 0











# external libraries 
from scipy.integrate import odeint
import os


# external files 
import system     as sys 
import imp_param  as imp 
import simu_populations_solver as sv 
import output_file_config as of
import user_interface as ui



def simu(user_sys_choice) : 


    # photophysical parameters importation
    const_molecule = imp.param_molecule()
    const_sample   = imp.param_sample(const_molecule[0])
    const_rates    = imp.param_rates(const_sample[2])

    # pump parameters importation
    const_pump = imp.param_pump()

    # time vector importation 
    dt,t = imp.param_time()

    # initial value for the populations S0,S1,T1
    # init_pop = [1,0,0]

    # output file to write the data on 
    ui.create_if_not_exists(['output'])
    output_file_path = ui.output_file_choice()
    config_file_path = ui.config_file_choice()

    ui.delete_file_if_exists([output_file_path,config_file_path])

    # output config files where input parameters are stored
    of.output_file_init_simu_pop(
        const_molecule,
        const_sample,
        const_rates,
        const_pump,
        t,
        config_file_path
        )





    # main section : integration of the system of equations
    ui.simulation_start()

    if user_sys_choice == 1 : 
        init_pop = [1,0]
        sv.solver(odeint,sys.sys_equations_two_pop,init_pop,t,const_sample[0],
                const_pump[0],
                const_sample,
                const_molecule,
                const_rates,
                output_file_path,
                user_sys_choice
            )

    elif user_sys_choice == 2 : 
        init_pop = [1,0,0]
        sv.solver(odeint,sys.sys_equations_three_pop,init_pop,t,const_sample[0],
                const_pump[0],
                const_sample,
                const_molecule,
                const_rates,
                output_file_path,
                user_sys_choice
            )

    ui.simulation_finished()   



    return 0







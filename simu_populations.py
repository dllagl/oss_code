



# external libraries 
from scipy.integrate import odeint


# external files 
import system     as sys 
import imp_param  as imp 
import simu_populations_solver as sv 
import output_file_config as of
import user_interface as ui


# simulations for one set of parameters
def simu_fixed_params(user_sys_choice) : 


    # photophysics/pump/time parameters importation
    const_molecule = imp.param_molecule()
    const_sample   = imp.param_sample(const_molecule[0])
    const_rates    = imp.param_rates(const_sample[2])

    # concatenate arrays for solver 
    const_params   = const_sample + const_molecule + const_rates

    const_pump     = imp.param_pump()
    tmin,tmax      = imp.param_time()

    # output file to write the data on 
    ui.create_if_not_exists(['output'])
    output_file_path = ui.output_file_choice()
    config_file_path = ui.config_file_choice()

    ui.delete_file_if_exists([output_file_path,config_file_path])

    # output config files where input parameters are stored
    of.output_file_init_simu_pop(
        const_sample,
        const_molecule,
        const_rates,
        const_pump,
        tmin,tmax,
        config_file_path
        )


    '''
    Simulations are done step-by-step by 1 microsecond in
    order not to full crash the program when output vectors
    become too heavy.
    This way, you can simulate any time, you are only limited
    by the physical memory of your computer.
    '''
    time_step_unit    = 1e-6  # time block of 1 us
    nbr_pts_per_step  = 2e3   # 2000 pts per us
    time_step_counter = int(tmax/time_step_unit)




    #---------------------------------------------------#
    #---------------------------------------------------#
    ui.simulation_start()

    # two level system (S0,S1)
    if user_sys_choice == 1 : 
        init_pop  = [1,0]
        ode_sys   = sys.sys_equations_two_pop

    # three level system (S0,S1,T1)
    elif user_sys_choice == 2 : 
        init_pop = [1,0,0]
        ode_sys = sys.sys_equations_three_pop

    # solve the ODE
    sv.solver(odeint,ode_sys,init_pop,tmin,tmax,const_sample[0],
                const_pump[0],
                const_params,
                output_file_path,
                user_sys_choice,
                time_step_counter,
                time_step_unit,
                nbr_pts_per_step
            )
    
    ui.simulation_finished()  
    #---------------------------------------------------#
    #---------------------------------------------------# 

    return 0






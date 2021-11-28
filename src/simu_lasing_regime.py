'''
@author    : Anthony Dall'agnol
@copyright : Copyright (C) 2021 Anthony Dall'agnol
@license   : GNU General Public License

-------
Integrate ODE systems for a large range of values of one 
parameter (chosen by user) to study the evolution of the 
lasing regime 

@simu_lasing_regime_three_pop : integrate ODE systems S0/S1/T1
@simu_lasing_regime_two_pop   : integrate ODE systems S0/S1

Called in: main.py
-------
'''

# external librairies 
from scipy.integrate import odeint


# external files 
import imp_param as imp
import system_laser as sys 
import user_interface as ui 
import user_choice as uc 
import phys_constants as cs 
import simu_lasing_regime_solver as sv 
import output_file_config as of 
import simu_lasing_regime_fct as fct  


# three level (S0/S1/T1 + intensity)
def simu_lasing_regime_three_pop(var_idx, var_arr) : 

    '''
    var_idx         : <int> chosen parameter to iterate on
    var_arr         : <array> different values for var_idx
    '''

    # lasing is considered in this config
    _is_laser = True
    
    # photophysics/pump/time parameters importation
    const_molecule = imp.param_molecule()
    const_sample   = imp.param_sample(const_molecule[0])
    const_rates    = imp.param_rates(const_sample[3])
    const_pump     = imp.param_pump()
    const_struct   = imp.param_resonator(const_molecule[2])
    tmin,tmax      = imp.param_time()




    # output file to write the data on 
    output_folder = uc.output_folder_choice()
    output_file_path = uc.output_file_choice(output_folder)
    config_file_path = uc.config_file(output_file_path)

    ui.create_if_not_exists([output_folder])
    ui.delete_file_if_exists([output_file_path,config_file_path])




    '''
    Simulations are done step-by-step by 1 microsecond in
    order not to crash the program when output arrays
    become too heavy.
    '''
    time_step_unit    = 5e-6  # time block of 5 us
    nbr_pts_per_step  = 5e3   # 5000 pts per us

    # Exception handling : integration time smaller that time step  
    if tmax < time_step_unit : time_step_unit = tmax

    time_step_counter = int(tmax/time_step_unit)



    

    #---------------------------------------------------#
    #---------------------------------------------------#
    ui.simulation_start()

    ofile = open(output_file_path, 'a+')
    cfile = open(config_file_path, 'a+')

    of.write_user_infos(cfile)

    ofile.write('\n\n')
    ofile.write('@config file : %s\n\n' % config_file_path)
    
    ofile.write('\n\n')
    fct.write_guidelines_three_pop(ofile)
    ofile.write('\n\n')

    
    ode_sys = sys.sys_equations_three_pop



    for ii in range(len(var_arr)) : 

        init_pop = [1,0,0,0]

        # Exception handling : variable Q-factor
        if var_idx == 21 : 
            const_struct = imp.param_resonator(const_molecule[2], var_arr[ii])
        else : 
            const_struct = imp.param_resonator(const_molecule[2])

        # concatenate arrays for solver 
        const_params   = const_sample + const_molecule + const_rates + const_pump + const_struct

        # replacing the value ii in const_params based on user choice 
        if (var_idx>15) and (var_idx<19) : 
            # exception handling : 
            # ksta,kssa,ktta are in m3.s-1 as 
            # input for the user, but must be multiplied by N since
            # the populations are normalized
            const_params[var_idx] = var_arr[ii] * const_sample[3]
            
        else : 
            const_params[var_idx] = var_arr[ii]



        # compute the saturation intensity of the S0/S1 transition to 
        # normalize the intra-cavity intensity I
        pump_saturation  = cs.C_HC / (const_molecule[1]*const_sample[1]*const_molecule[3])
        tau_eff          = const_molecule[3] / (1+(const_pump[0]/pump_saturation))
        laser_saturation = cs.C_HC / (const_molecule[2]*const_molecule[5]*tau_eff)




        # solve the ODE
        sv.solver_three_pop(odeint,ode_sys,init_pop,tmin,tmax,const_sample[0],
            const_params,
            laser_saturation,
            ofile,
            time_step_counter,
            time_step_unit,
            nbr_pts_per_step,
            var_arr[ii]
            )



    ofile.close()
    ui.simulation_finished()
    #---------------------------------------------------#
    #---------------------------------------------------#


    return 0 


















# three level (S0/S1 + intensity)
def simu_lasing_regime_two_pop(var_idx, var_arr) : 

    '''
    var_idx         : <int> chosen parameter to iterate on
    var_arr         : <array> different values for var_idx
    '''
    
    # lasing is considered in this config
    _is_laser = True
    
    # photophysics/pump parameters importation
    const_molecule = imp.param_molecule()
    const_sample   = imp.param_sample(const_molecule[0])
    const_rates    = imp.param_rates(const_sample[3])
    const_pump     = imp.param_pump()
    const_struct   = imp.param_resonator(const_molecule[2])
    
    # time parameters
    '''
    Since this configuration is a perfect two level, the S1 population
    (and hence the lasing intensity) will be clamped after the relaxation
    oscillation whether there is lasing or not
    -> Therefore, there is no need to integrate over more than 1 us to see 
    if there is lasing or not 
    '''
    tmin = 0.0
    tmax = 1e-6





    # output file to write the data on 
    output_folder = uc.output_folder_choice()
    output_file_path = uc.output_file_choice(output_folder)
    config_file_path = uc.config_file(output_file_path)

    ui.create_if_not_exists([output_folder])
    ui.delete_file_if_exists([output_file_path,config_file_path])




    '''
    Simulations are done step-by-step by 1 microsecond in
    order not to crash the program when output arrays
    become too heavy.
    '''
    time_step_unit    = 5e-6  # time block of 5 us
    nbr_pts_per_step  = 5e3   # 5000 pts per us

    # Exception handling : integration time smaller that time step  
    if tmax < time_step_unit : time_step_unit = tmax

    time_step_counter = int(tmax/time_step_unit)



    

    #---------------------------------------------------#
    #---------------------------------------------------#
    ui.simulation_start()

    ofile = open(output_file_path, 'a+')
    
    ofile.write('\n\n')
    fct.write_guidelines_two_pop(ofile)
    ofile.write('\n\n')

    
    ode_sys = sys.sys_equations_two_pop



    for ii in range(len(var_arr)) : 

        init_pop = [1,0,0]

        # Exception handling : variable Q-factor
        if var_idx == 21 : 
            const_struct = imp.param_resonator(const_molecule[2], var_arr[ii])
        else : 
            const_struct = imp.param_resonator(const_molecule[2])

        # concatenate arrays for solver 
        const_params   = const_sample + const_molecule + const_rates + const_pump + const_struct

        # replacing the value ii in const_params based on user choice 
        const_params[var_idx] = var_arr[ii]



        # compute the saturation intensity of the S0/S1 transition to 
        # normalize the intra-cavity intensity I
        pump_saturation  = cs.C_HC / (const_molecule[1]*const_sample[1]*const_molecule[3])
        tau_eff          = const_molecule[3] / (1+(const_pump[0]/pump_saturation))
        laser_saturation = cs.C_HC / (const_molecule[2]*const_molecule[5]*tau_eff)




        # solve the ODE
        sv.solver_two_pop(odeint,ode_sys,init_pop,tmin,tmax,const_sample[0],
            const_params,
            laser_saturation,
            ofile,
            time_step_counter,
            time_step_unit,
            nbr_pts_per_step,
            var_arr[ii]
            )



    ofile.close()
    ui.simulation_finished()
    #---------------------------------------------------#
    #---------------------------------------------------#


    return 0 



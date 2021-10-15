

import os 


def welcome() : 

    print(
    '''
    ----------------------------------------------
    ----------------------------------------------

    Welcome in this interface, this Hello message
    is pretty boring but it will get better afterwards
    Enjoy ! 

    List of available simulations : 

    One simulation at fixed parameters
    ----------------------------------------------
    |  1) Two level system (S0,S1)  
    |  2) Three level system (S0,S1,T1)
    |
    |  The ODE system is integrated once from
    |  tmin to tmax. Populations and inputs are 
    |  stored in one file in the output folder
    |  To change parameters : imp_param.py
    ----------------------------------------------

    Simulations for several values of one parameter
    ----------------------------------------------
    |  3) Two level system (S0,S1)
    |  4) Three level system (S0,S1,T1)
    |
    |  The ODE system is integrated once for each
    |  value of a given parameter.
    |  Ex: if you want to execute the program for 
    |  n value of kisc or the doping, choose this
    |  one. You will choose the parameter you want
    |  on the next frame.
    ----------------------------------------------

    ----------------------------------------------
    ----------------------------------------------
    ''')

    return 0






def print_something(str) : 
    print(f'''
    {str}
    '''
    )

def simulation_start() : 
    print_something('Computation has started ..')
    return 0

def simulation_finished() : 
    print_something('Computation has finished.')
    return 0













def delete_file_if_exists(arr_file) : 

    for ii in range(len(arr_file)) : 

        if os.path.exists(arr_file[ii]) : 
            os.remove(arr_file[ii])
            print(f'File {arr_file[ii]} has been removed.')

    return 0

def create_if_not_exists(arr_folder) : 

    for ii in range(len(arr_folder)) : 

        if os.path.exists(arr_folder[ii]) == False : 
            os.makedirs(arr_folder[ii])
            print(f'Folder {arr_folder[ii]} has been created.')

    return 0

    




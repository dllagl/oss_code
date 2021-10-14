

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
    |   
    |  2) Three level system (S0,S1,T1)
    |
    |  The ODE system is integrated once from
    |  tmin to tmax. Populations and inputs are 
    |  stored in one file in the output folder
    |  To change parameters : imp_param.py
    ----------------------------------------------

    Simulations for several values of one parameter
    ----------------------------------------------
    |  3) Working on that
    |
    |  The ODE system is integrated once for each
    |  value of the chosen parameter.
    |  Ex: if kisc = [1e6,1e7,1e8]
    |  > three integration : populations and inputs
    |    will be stored in three differents files
    |  
    |  The concerned parameters will have to be 
    |  chosen after this choice
    |  !! DON'T PUT LISTS/ARRAYS IN imp_param.py !!
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








# files and folders


def output_file_choice() : 

    print(
    '''
    ----------------------------------------------
    Please write the path for the output text file
    on which data are going to be written in.
    Default: data.out
    ----------------------------------------------
    ''')
    output_folder = 'output/'
    output_file = input('File name : ') or 'data.out'
    output_file_path = output_folder + output_file
    return output_file_path

def config_file_choice() : 

    print(
    '''
    ----------------------------------------------
    Please enter a name for the file in which 
    simulations parameters will be stored
    Default: data.params (just press Enter)
    ----------------------------------------------
    ''')
    config_folder = 'output/'
    config_file = input('File path : ') or 'data.params'
    config_file_path = config_folder + config_file
    return config_file_path




def delete_file_if_exists(arr_file) : 

    print('')
    for ii in range(len(arr_file)) : 

        if os.path.exists(arr_file[ii]) : os.remove(arr_file[ii])
        print(f'File {arr_file[ii]} has been removed.')
    return 0

def create_if_not_exists(arr_folder) : 

    print('')
    for ii in range(len(arr_folder)) : 
        if os.path.exists(arr_folder[ii]) == False : 
            os.makedirs(arr_folder[ii])
            print(f'Folder {arr_folder[ii]} has been created.')
    return 0

    

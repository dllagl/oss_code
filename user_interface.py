

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

    1) Integrate a three level system of ODE for 
    the populations S0,S1 and T1.
    In this option, everything is fixed and the 
    resulting populations are written with time 
    on an unique output file.
    
    To costum parameters such as rates, time of 
    integration and so on, go to imp_param.py.

    ----------------------------------------------
    ----------------------------------------------
    ''')

    return 0








def simulation_start() : 

    print(
    '''
    Computation has started ..
    '''
    )

    return 0

def simulation_finished() : 

    print(
    '''
    Computation has finished !
    '''
    )

    return 0











def output_file_choice() : 

    print(
    '''
    ----------------------------------------------
    Please write the path for the output text file
    on which data are going to be written in. 

    If the file already exists, the previous 
    version will be permanently deleted

    For default name (data.out) press Enter.
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
    Ex : simu.params
    
    For default name (data.params) press Enter.
    ----------------------------------------------
    ''')
    config_folder = 'output/'
    config_file = input('File path : ') or 'data.params'
    config_file_path = config_folder + config_file
    return config_file_path






# files and folder 


def delete_file_if_exists(arr_file) : 

    print('')
    for ii in range(len(arr_file)) : 

        if os.path.exists(arr_file[ii]) : os.remove(arr_file[ii])
        print(f'File {arr_file[ii]} has been removed.')
    print('')
    return 0

def create_if_not_exists(arr_folder) : 

    print('')
    for ii in range(len(arr_folder)) : 
        if os.path.exists(arr_folder[ii]) == False : 
            os.makedirs(arr_folder[ii])
            print(f'Folder {arr_folder[ii]} has been created.')
    print('')
    return 0

    

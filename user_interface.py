

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

    Two options : 
    Relative path : ../folder/simu.out
    Absolute path : ~/Documents/folder/simu.out

    If the file already exists, the previous 
    version will be permanently deleted
    ----------------------------------------------
    ''')

    output_file_path = 'output/' + input('File path : ')
    return output_file_path

def config_file_choice() : 

    print(
    '''
    ----------------------------------------------
    Please enter a name for the file in which 
    simulations parameters will be stored
    Ex : simu.params
    ----------------------------------------------
    ''')

    config_file_path = 'output/' + input('File path : ')
    return config_file_path







def delete_file_if_exists(arr_file) : 

    print('')
    for ii in range(len(arr_file)) : 

        if os.path.exists(arr_file[ii]) : os.remove(arr_file[ii])
        print(f'File {arr_file[ii]} has been removed.')
    print('')
    return 0
    

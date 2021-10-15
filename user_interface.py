

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








# files and folders

def output_folder_choice() : 

    folder = input('Output folder name : ') or 'output'
    return folder

def output_file_choice(output_folder) : 

    print(
    '''
    ----------------------------------------------
    Please write the path for the output text file
    on which data are going to be written in.
    Default: data.out
    ----------------------------------------------
    ''')
    output_file = input('File name : ') or 'data.out'
    output_file_path = output_folder + '/' + output_file
    return output_file_path

def config_file_choice(output_folder) : 

    print(
    '''
    ----------------------------------------------
    Please enter a name for the file in which 
    simulations parameters will be stored
    Default: data.params (just press Enter)
    ----------------------------------------------
    ''')
    config_file = input('File path : ') or 'data.params'
    config_file_path = output_folder + '/' + config_file
    return config_file_path




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

    



# choose which variable to iterate on in 
# simu_multiple_params() function
def choose_param() : 

    print(
    '''
    ---------------------------------
    0)  doping
    1)  sigma_abs (m2)
    2)  n_eff
    3)  nbr_active_molecule (m-3)
    4)  molar_mass (g/mol)
    5)  lambda_abs (m)
    6)  lambda_fluo (m)
    7)  tau_f (s)
    8)  tau_t (s)
    9)  sigma_em (m2)
    10) sigma_S1S2_pump (m2)
    11) sigma_S1S2_laser (m2)
    12) sigma_T1T2_pump (m2)
    13) sigma_T1T2_laser (m2)
    14) kSI
    15) kisc (s-1) 
    16) ksta (m3.s-1)
    17) kssa (m3.s-1)
    18) ktta (m3.s-1)
    ---------------------------------
    ''')
    print('Which variable du you want to iterate ?')
    return int(input("Enter its corresponding number : "))



def choose_param_values() : 

    print('')
    print('Press enter after each written.')
    print('When finish, press Enter once more.')
    print('')
    arr = []
    count = 1
    temp = input(f'Value {count} (Press Enter when finish) : ')
    count += 1

    while temp : 
        arr.append(eval(temp))
        temp = input(f'Value {count} (Press Enter when finish) : ')
        count += 1
    
    return arr



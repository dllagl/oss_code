



# files and folders
def output_folder_choice() : 

    print(
    '''
    ----------------------------------------------
    Please write the path for the output folder in
    which data are going to be written in.
    Default (Press Enter): output
    ----------------------------------------------
    ''')

    folder = input('Output folder name : ') or 'output'
    return folder

def output_file_choice(output_folder) : 

    print(
    '''
    ----------------------------------------------
    Please write the path for the output text file
    on which data are going to be written in.
    Default (Press Enter): data.out
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
    Default (Press Enter): data.params
    ----------------------------------------------
    ''')
    config_file = input('File path : ') or 'data.params'
    config_file_path = output_folder + '/' + config_file
    return config_file_path











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

    while temp : 
        count += 1
        arr.append(eval(temp))
        temp = input(f'Value {count} (Press Enter when finish) : ')
    
    return arr


import os 

# main menu 
def welcome() : 
    print(
    '''
-------------------------------------------

      --------     -------     -------   
     |        |   |           |
     |        |   |           |
     |        |   --------    --------
     |        |           |           |
     |        |           |           |
      --------     -------    --------

          Organic Systems Simulator

-------------------------------------------

    ''')
    return 0

def print_available_systems() : 
    print(
'''
>> Populations
1) two level   : S0/S1
2) three level : S0/S1/T1

>> Populations + lasing intensity (ongoing development)
3) two level : S0/S1/intensity
4) three level : S0/S1/T1/intensity
''')
    return 0







# stupid stuffs
def print_something(str) : 
    print(f'{str}')
    return 0

def simulation_start() : 
    print_something('Computation has started ..')
    return 0

def simulation_finished() : 
    print_something('Computation has finished.')
    return 0












# files and folders
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

    




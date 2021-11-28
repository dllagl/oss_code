'''
-------------------------------------------------------------------
This file is part of the OSS source code 
Copyright (C) 2021 Anthony Dall'agnol 

This program is free software: you can redistribute it and/or modify 
it under the terms of the GNU General Public License as published 
by the Free Software Foundation, either version 3 of the License, or 
any later version. 
This program is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
GNU General Public License for more details. 
You should have received a copy of the GNU General Public License 
along with this program. If not, see <https://www.gnu.org/licenses/>
-------------------------------------------------------------------

@author    : Anthony Dall'agnol
@copyright : Copyright (C) 2021 Anthony Dall'agnol
@license   : GNU General Public License

-------------------------------------------------------------------
Related to interface message and files creation/deletion

Called in: main.py,simu_populations.py,simu_laser.py,simu_lasing_regime.py
-------------------------------------------------------------------
'''

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
Please choose a system to work on.

-> Populations
1) two level   : S0/S1
2) three level : S0/S1/T1

-> Populations + resonator
3) two level   : S0/S1/intensity
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

    




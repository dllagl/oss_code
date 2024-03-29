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
Related to the terminal interface where user has to 
choose something 

@user_type_choice     : type of simulations 
@output_folder_choice : name of folder for output files
@output_file_choice   : name of output data file
@config_file          : build config file based on output_file_choice

@choose_param_populations   : choice of parameter to iterate (no resonator)
@choose_param_laser         : choice of parameter to iterate with resonator
@choose_param_values        : choice of different values of the chosen parameter
@choose_param_lasing_regime : min and max values of the chosen parameter for lasing regime simu

@ask_plot         : do you want to plot right away ? 
@plot_two_pop     : choice of variable to plot between S0/S1
@plot_three_pop   : choice of variable to plot between S0/S1/T1
@plot_two_laser   : choice of variable to plot between S0/S1/I
@plot_three_laser : choice of variable to plot between S0/S1/T1/I

Called in: main.py,simu_populations.py,simu_laser.py,simu_lasing_regime.py
-------------------------------------------------------------------
'''



# choice of simulations type for populations and lasing 
# simulations (called in main.py)
def user_type_choice() : 

    print(
'''
1) one simulation with one set of parameters (to be customed in imp_param.py)
2) n simulations for n values of one parameter (ex : kisc = 1e6, 1e7, 1e8)
3) Lasing regime study for a large range of values (beta)
''')

    return eval(input('Which simulation (1,2) ? '))




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
Default (Press Enter): data
----------------------------------------------
''')
    output_file = input('File name : ') or 'data'
    output_file_path = output_folder + '/' + output_file + '.out'
    return output_file_path

def config_file(output_file_path) : 
    
    config_file = output_file_path.partition('.')
    config_file_path = config_file[0] + '.params'
    return config_file_path











# choose which variable to iterate on in 
# simu_multiple_params() function
def choose_param_populations() : 
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
19) Ip (W.m-2)
---------------------------------
''')
    print('Which variable du you want to iterate ?')
    return int(input("Enter its corresponding number : "))





def choose_param_laser() : 
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
19) Ip (W.m-2)
20) gamma
21) Q-factor
//
24) pump_area (m2)
---------------------------------
''')
    print('Which variable du you want to iterate ?')
    return int(input("Enter its corresponding number : "))


# user enter values of the parameter chosen in the functions 
# choose_param_populations() ; choose_param_laser()
# return list of values 
# called in main.py
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


def choose_param_lasing_regime() : 

    print('')
    print('''The objective is to run the simulations
a wide range of value of the desired parameter.
If you want the parameter to go from 1e4 to 1e6, enter
4 and 6 as lowest and highest values.
''')
    low     = int(input('Enter the power of the lowest desired value : '))
    high    = int(input('Enter the power of the highest desired value : '))
    nbr_val = int(input('Number of value : ')) 

    from numpy import logspace

    return logspace(low,high,nbr_val)










########## plot 


# ask user if he/she wants to preview plot
def ask_plot() : 
    return input('Do you want to plot some datas from this simulation (y/n) ? ')

# S0/S1
def plot_two_pop() : 

    print(
'''
What do you want to plot with time ? 
1) S0
2) S1
''')
    return int(eval(input('Your choice : '))
    )



# S0/S1/T1
def plot_three_pop() : 

    print(
'''
What do you want to plot with time ? 
1) S0
2) S1
3) T1
''')
    return int(eval(input('Your choice : '))
    )



# S0/S1/I
def plot_two_laser() : 

    print(
'''
What do you want to plot with time ? 
1) S0
2) S1
3) lasing intensity
''')
    return int(eval(input('Your choice : '))
    )

     

# S0/S1/T1/I
def plot_three_laser() : 

    print(
'''
What do you want to plot with time ? 
1) S0
2) S1
3) T1
4) lasing intensity
''')
    return int(eval(input('Your choice : '))
    )

     
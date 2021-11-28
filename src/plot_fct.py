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
Related to plotting data right after integration

@plot_setup  : setup of the figure 
@plot_multiple_params : plot curves for each value of the chosen 
parameter

Called in: main.py
-------------------------------------------------------------------
'''

# external libraries 
import matplotlib.pyplot as plt 
import numpy as np

# external files 
import user_choice as uc 




def plot_setup(data_arr, idx, ylabel) :


    font_size = 20
    tick_size = 15
    plt.plot(data_arr[:,0]*1e6, data_arr[:,int(idx)]) 
    plt.yscale('log')
    plt.xscale('linear')
    plt.xlabel('Time (us)', fontsize = font_size)
    plt.ylabel(ylabel, fontsize = font_size)
    plt.yticks(fontsize = tick_size)
    plt.xticks(fontsize = tick_size)
    plt.tight_layout()




def plot_multiple_params(name_file,nbr_file,idx,ylabel) : 
    
    for ii in range(nbr_file) : 
        temp_file = name_file + f'_{int(ii)}' + '.out'
        data = np.loadtxt(temp_file,skiprows=5)
        plot_setup(data,idx,ylabel)
    
    plt.legend(
        np.linspace(0,nbr_file,nbr_file+1).astype(int),
        frameon=False,
        prop = {'size':15})





def main_plot_fixed_params(sys,file) :

    '''
    sys : system of the simuations (S0/S1 or S0/S1/T1 ..)
    file : file in which output data are written
    '''

    # load data file 
    data = np.loadtxt(file,skiprows=5)

    # number of columns (to guess which system it is )
    nbr_cols = int(np.size(data,1))

    # no lasing (S0/S1 or S0/S1/T1)
    if (sys <= 2) : 

        # S0/S1
        if (nbr_cols == 3) : 
            str_arr = ['S0/N', 'S1/N']
            idx = uc.plot_two_pop()
            plot_setup(data,idx,str_arr[idx-1])

        else : 
            str_arr = ['S0/N', 'S1/N', 'T1/N']
            idx = uc.plot_three_pop()
            plot_setup(data,idx,str_arr[idx-1])

    # lasing (S0/S1/I or S0/S1/T1/I)
    else : 

        # S0/S1/I
        if (nbr_cols == 4) : 
            str_arr = ['S0/N', 'S1/N', 'I/Isat']
            idx = uc.plot_two_laser()
            plot_setup(data,idx,str_arr[idx-1])

        else : 
            str_arr = ['S0/N', 'S1/N', 'T1/N', 'I/Isat']
            idx = uc.plot_three_laser()
            plot_setup(data,idx,str_arr[idx-1])

    plt.show()














def main_plot_multiple_params(sys,file_name,file_nbr) :

    '''
    sys : system of the simuations (S0/S1 or S0/S1/T1 ..)
    file : file in which output data are written
    '''

    # load first data file to count the columns 
    first_file_name = file_name + '_0.out'
    temp_data = np.loadtxt(first_file_name,skiprows=5,max_rows=2)

    # number of columns (to guess which system it is )
    nbr_cols = int(np.size(temp_data,1))
    del temp_data

    # no lasing (S0/S1 or S0/S1/T1)
    if (sys <= 2) : 

        # S0/S1
        if (nbr_cols == 3) : 
            str_arr = ['S0/N', 'S1/N']
            idx = uc.plot_two_pop()
            plot_multiple_params(file_name,file_nbr,idx,str_arr[idx-1])

        else : 
            str_arr = ['S0/N', 'S1/N', 'T1/N']
            idx = uc.plot_three_pop()
            plot_multiple_params(file_name,file_nbr,idx,str_arr[idx-1])

    # lasing (S0/S1/I or S0/S1/T1/I)
    else : 

        # S0/S1/I
        if (nbr_cols == 4) : 
            str_arr = ['S0/N', 'S1/N', 'I/Isat']
            idx = uc.plot_two_laser()
            plot_multiple_params(file_name,file_nbr,idx,str_arr[idx-1])

        else : 
            str_arr = ['S0/N', 'S1/N', 'T1/N', 'I/Isat']
            idx = uc.plot_three_laser()
            plot_multiple_params(file_name,file_nbr,idx,str_arr[idx-1])

    plt.show()





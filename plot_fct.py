
# external libraries 
import matplotlib.pyplot as plt 
import numpy as np

# external files 
import user_choice as uc 




def plott(data_arr, idx, ylabel) :

    # tex syntax enabled
    plt.rc('text',usetex = True)

    font_size = 20
    tick_size = 15
    plt.plot(data_arr[:,0]*1e6, data_arr[:,int(idx)]) 
    plt.yscale('log')
    plt.xscale('linear')
    plt.xlabel('$\\rm Time \\ (\\mu s)$', fontsize = font_size)
    plt.ylabel(ylabel, fontsize = font_size)
    plt.yticks(fontsize = tick_size)
    plt.xticks(fontsize = tick_size)
    plt.tight_layout()
    plt.show()



def main_plot(sys,file) :

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
            str_arr = ['$S_0$', '$S_1$']
            idx = uc.plot_two_pop()
            plott(data,idx,str_arr[idx-1])

        else : 
            str_arr = ['$S_0$', '$S_1$', '$T_1$']
            idx = uc.plot_three_pop()
            plott(data,idx,str_arr[idx-1])


    # lasing (S0/S1/I or S0/S1/T1/I)
    else : 

        # S0/S1/I
        if (nbr_cols == 4) : 
            str_arr = ['$S_0$', '$S_1$', '$\\rm Intensity$']
            idx = uc.plot_two_laser()
            plott(data,idx,str_arr[idx-1])

        else : 
            str_arr = ['$S_0$', '$S_1$', '$T_1$', '$\\rm Intensity$']
            idx = uc.plot_three_laser()
            plott(data,idx,str_arr[idx-1])






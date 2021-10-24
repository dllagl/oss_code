

import numpy as np 
import matplotlib.pyplot as plt 



def read_txt_file(file) : 


    data = np.loadtxt(file, skiprows=5)

    time = data[:,0]
    S0   = data[:,1]
    S1   = data[:,2]
    T1   = data[:,3]
    amp  = data[:,4]

    plt.plot(time*1e6,amp)
    plt.yscale('log')
    plt.show()



read_txt_file('../output/data.out')
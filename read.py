import numpy as np 
import matplotlib.pyplot as plt 



def read_laser(file) : 

    data = np.loadtxt(file,skiprows=5)
    time = data[:,0]
    fluo = data[:,2]
    amp  = data[:,3]

    plt.plot(time,fluo)
    plt.yscale('log')


read_laser('output/data.out')
plt.show()
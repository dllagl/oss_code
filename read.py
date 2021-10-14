import numpy as np 
import matplotlib.pyplot as plt 



def read(file) : 

    data = np.loadtxt(file)
    time = data[:,0]
    fluo = data[:,2]

    plt.plot(time,fluo)


read('output/data_2.out')
read('output/data.out')
plt.show()
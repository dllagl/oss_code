import numpy as np 
import matplotlib.pyplot as plt 



def read(file) : 

    data = np.loadtxt(file)
    time = data[::100,0] * 1e6
    amp  = data[::100,2]
    print(len(amp))


    plt.plot(time,amp)
    plt.yscale('log')
    plt.show()


read('test.txt')

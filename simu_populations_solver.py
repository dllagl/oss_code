

# external libraries
import numpy as np


def solver(method,sys,initial_pop,tmin,tmax,doping,
    param_arr,output_file,config_file,user_sys_choice,
    time_counter,time_unit,nbr_pts) :

    ofile = open(output_file,'a+')
    ofile.write('\n\n')
    ofile.write('@config file : %s\n\n' % config_file)

    if user_sys_choice == 1 : 
        ofile.write('%s %14s %13s\n' % ('time', 'S0', 'S1'))

    elif user_sys_choice == 2 : 
        ofile.write('%s %13s %10s %11s\n' % ('time', 'S0', 'S1', 'T1'))


    for ii in range(time_counter) : 

        # define time vector iteration
        tmin     = ii*time_unit
        tmax     = (ii+1)*time_unit
        time_vec = np.linspace(tmin,tmax,int(nbr_pts))

        # integrating the ODE system with odeint
        sol = method(sys,initial_pop,time_vec, args=(doping,
            param_arr)
            )



        # two level system
        if user_sys_choice == 1 : 
            
            # actualized initial populations
            initial_pop = [sol[-1,0], sol[-1,1]]
            
            # write populations with time on file 
            for jj in range(len(sol)) :
                ofile.write('%.3e %13.3e %13.3e\n' 
                % (time_vec[jj],sol[jj,0],sol[jj,1]))

        # three level system
        elif user_sys_choice == 2 : 

            initial_pop = [sol[-1,0], sol[-1,1], sol[-1,2]]

            for jj in range(len(sol)) :
                ofile.write('%.3e\t%.3e\t%.3e\t%.3e\n' 
                % (time_vec[jj],sol[jj,0],sol[jj,1],sol[jj,2]))

    
    ofile.close()



    return 0
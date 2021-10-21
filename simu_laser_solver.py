

# external libraries
import numpy as np


def solver(method,sys,initial_pop,tmin,tmax,doping,pump_fluence,
    param_arr,output_file,config_file,user_sys_choice,
    time_counter,time_unit,nbr_pts) :

    ofile = open(output_file,'a+')
    ofile.write('\n\n')
    ofile.write('@config file : %s\n\n' % config_file)

    if user_sys_choice == 3 : 
        ofile.write('%s %14s %13s %13s\n' % ('time', 'S0', 'S1', 'I'))

    elif user_sys_choice == 4 : 
        ofile.write('%s %13s %10s %11s %11s\n' % ('time', 'S0', 'S1', 'T1', 'I'))

    for ii in range(time_counter) : 

        # more points for the first time step (relaxation oscillation are stiffs)
        if ii == 0 : 
            nbr_pts_eff = nbr_pts * 10
        else : 
            nbr_pts_eff = nbr_pts

        # define time vector iteration
        time_vec = np.linspace(ii*time_unit,(ii+1)*time_unit,int(nbr_pts_eff))

        # integrating the ODE system with odeint
        sol = method(sys,initial_pop,time_vec, args=(doping, pump_fluence,
            param_arr)
            )



        # two level system
        if user_sys_choice == 3 : 
            
            # actualized initial populations
            initial_pop = [sol[-1,0], sol[-1,1], sol[-1,2]]
            
            # write populations with time on file 
            for jj in range(len(sol)) :
                ofile.write('%.3e %13.3e %13.3e %13.3e\n' 
                % (time_vec[jj],sol[jj,0],sol[jj,1],sol[jj,2]))

        # three level system
        elif user_sys_choice == 4 : 

            initial_pop = [sol[-1,0], sol[-1,1], sol[-1,2], sol[-1,3]]

            for jj in range(len(sol)) :
                ofile.write('%.3e\t%.3e\t%.3e\t%.3e\t%.3e\n' 
                % (time_vec[jj],sol[jj,0],sol[jj,1],sol[jj,2],sol[jj,3]))

    
    ofile.close()



    return 0
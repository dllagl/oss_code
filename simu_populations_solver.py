


import numpy as np


def solver(method,sys,initial_pop,tmin,tmax,doping,pump_fluence,
    sample_arr,molecule_arr,rates_arr,output_file, user_sys_choice,
    time_counter,time_unit,nbr_pts) :


    for ii in range(time_counter) : 

        # define time vector iteration
        time_vec = np.linspace(ii*time_unit,(ii+1)*time_unit,int(nbr_pts))

        # integrating the ODE system with odeint
        sol = method(sys,initial_pop,time_vec, args=(doping, pump_fluence,
            sample_arr,molecule_arr,rates_arr)
            )



        ofile = open(output_file,'a+')

        # two level system
        if user_sys_choice == 1 : 
            
            # actualized initial populations
            initial_pop = [sol[-1,0], sol[-1,1]]
            
            # write populations with time on file 
            for jj in range(len(sol)) :
                ofile.write('%.3e\t%.3e\t%.3e\n' 
                % (time_vec[jj],sol[jj,0],sol[jj,1]))

        # three level system
        elif user_sys_choice == 2 : 

            initial_pop = [sol[-1,0], sol[-1,1], sol[-1,2]]

            for jj in range(len(sol)) :
                ofile.write('%.3e\t%.3e\t%.3e\t%.3e\n' 
                % (time_vec[jj],sol[jj,0],sol[jj,1],sol[jj,2]))

        ofile.close()



    return 0


# external libraries
import numpy as np


def solver(method,sys,initial_pop,tmin,tmax,doping,
    param_arr,laser_sat,output_file,config_file,user_sys_choice,
    time_counter,time_unit,nbr_pts) :

    ofile = open(output_file,'a+')
    ofile.write('\n\n')
    ofile.write('@config file : %s\n\n' % config_file)

    if user_sys_choice == 3 : 
        ofile.write('%s %15s %13s %14s\n' % ('time', 'S0/N', 'S1/N', 'I/Isat'))

    elif user_sys_choice == 4 : 
        ofile.write('%s %13s %11s %11s %13s\n' % ('time', 'S0/N', 'S1/N', 'T1/N', 'I/Isat'))






    #---------------------------------------------------#
    #---------------------------------------------------#
    # integrate first time for relaxation oscillation 
    # (require more points for ~20ns)
    time_osc     = 20e-9
    nbr_pts_osc  = 1e4
    time_vec_osc = np.linspace(0,time_osc,int(nbr_pts_osc))

    sol = method(sys,initial_pop,time_vec_osc, args=(doping,
        param_arr)
        )


    # two level system (S0/S1/I)
    if user_sys_choice == 3 : 
        
        # actualized initial populations
        initial_pop = [sol[-1,0], sol[-1,1], sol[-1,2]]
        
        # write populations with time on file 
        for jj in range(len(sol)) :
            ofile.write('%.3e %13.3e %13.3e %13.3e\n' 
            % (time_vec_osc[jj],sol[jj,0],sol[jj,1],sol[jj,2]/laser_sat))

    # three level system (S0/S1/T1/I)
    elif user_sys_choice == 4 : 

        initial_pop = [sol[-1,0], sol[-1,1], sol[-1,2], sol[-1,3]]

        for jj in range(len(sol)) :
            ofile.write('%.3e\t%.3e\t%.3e\t%.3e\t%.3e\n' 
            % (time_vec_osc[jj],sol[jj,0],sol[jj,1],sol[jj,2],sol[jj,3]/laser_sat))

    #---------------------------------------------------#
    #---------------------------------------------------#







    #---------------------------------------------------#
    #---------------------------------------------------#
    # integration after relaxtion oscillation (larger time step
    # and less points)
    for ii in range(time_counter) : 

        # define time vector iteration
        tmin     = ii*time_unit + time_osc
        tmax     = (ii+1)*time_unit + time_osc
        time_vec = np.linspace(tmin,tmax,int(nbr_pts))

        # integrating the ODE system with odeint
        sol = method(sys,initial_pop,time_vec, args=(doping,
            param_arr)
            )


        # two level system (S0/S1/I)
        if user_sys_choice == 3 : 
            
            # actualized initial populations
            initial_pop = [sol[-1,0], sol[-1,1], sol[-1,2]]
            
            # write populations with time on file 
            for jj in range(len(sol)) :
                ofile.write('%.3e %13.3e %13.3e %13.3e\n' 
                % (time_vec[jj],sol[jj,0],sol[jj,1],sol[jj,2]/laser_sat))


        # three level system (S0/S1/T1/I)
        elif user_sys_choice == 4 : 

            initial_pop = [sol[-1,0], sol[-1,1], sol[-1,2], sol[-1,3]]

            for jj in range(len(sol)) :
                ofile.write('%.3e\t%.3e\t%.3e\t%.3e\t%.3e\n' 
                % (time_vec[jj],sol[jj,0],sol[jj,1],sol[jj,2],sol[jj,3]/laser_sat))

    
    #---------------------------------------------------#
    #---------------------------------------------------#

    


    ofile.close()
    return 0
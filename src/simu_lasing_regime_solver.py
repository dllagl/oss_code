

# external libraries
import numpy as np

# external files 
import simu_lasing_regime_fct as fct 





def solver_three_pop(method,sys,initial_pop,tmin,tmax,doping,
    param_arr,laser_sat,ofile,
    time_counter,time_unit,nbr_pts,var) :

    # if I/Isat <= lasing_criteria : lasing is gone
    # only fluorescence remains
    lasing_criteria = 1e-2

    #---------------------------------------------------#
    #---------------------------------------------------#
    # integrate first time for relaxation oscillation 
    # (require more points for ~20ns)

    time_osc     = 20e-9
    nbr_pts_osc  = 1e4
    time_vec_osc = np.linspace(0,time_osc,int(nbr_pts_osc))


    # integrating the ODE system with odeint
    sol = method(sys,initial_pop,time_vec_osc, args=(doping,
        param_arr)
        )

    # actualizd initialtion population for next integration step
    initial_pop = [sol[-1,0], sol[-1,1], sol[-1,2], sol[-1,3]]

    # if normalized intensity is lower than 1e-2 after 
    # relaxation oscillation : no lasing (abitrary criteria)
    if ((sol[-1,3]/laser_sat) <= lasing_criteria) : 
        fct.write_no_lasing(ofile,var)
        return 


    #---------------------------------------------------#
    #---------------------------------------------------#






    #---------------------------------------------------#
    #---------------------------------------------------#
    # integration after relaxation oscillation (larger time step
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

        # actualized initialtion population for next integration step
        initial_pop = [sol[-1,0], sol[-1,1], sol[-1,2], sol[-1,3]]


        '''
        algorithm to find what the emitted lasing regime is 
        (no lasing, pulse or true cw)
        '''

        int_norm = sol[:,3] / laser_sat

        diff_threshold = 1e-5
        diff = np.abs(int_norm[-1] - int_norm[0])

        # only fluorescence remains -> have to search 
        # the duration of the lasing pulse 
        if (int_norm[-1] < lasing_criteria) : 

            temp = fct.find_pulse_duration(time_vec,int_norm)
            fct.write_pulse(ofile,var,temp[0])
            return 

        # if the intensity has reached a stable value without the previous
        # condition being fullfilled, then it is cw lasing 
        elif (diff < diff_threshold) : 

            fct.write_cw(ofile,var)
            return 

        # if intensity has not reached stable value during the last 
        # integration time step, then we write the integration time as 
        # a pulse.
        elif (ii == time_counter - 1) : 

            fct.write_undefined(ofile,var)
            return 


    

    #---------------------------------------------------#
    #---------------------------------------------------#

    return 0
















def solver_two_pop(method,sys,initial_pop,tmin,tmax,doping,
    param_arr,laser_sat,ofile,
    time_counter,time_unit,nbr_pts,var) :

    # if I/Isat <= lasing_criteria : lasing is gone
    # only fluorescence remains
    lasing_criteria = 1e-2

    #---------------------------------------------------#
    #---------------------------------------------------#
    # integrate first time for relaxation oscillation 
    # (require more points for ~20ns)

    time_osc     = 20e-9
    nbr_pts_osc  = 1e4
    time_vec_osc = np.linspace(0,time_osc,int(nbr_pts_osc))


    # integrating the ODE system with odeint
    sol = method(sys,initial_pop,time_vec_osc, args=(doping,
        param_arr)
        )

    # actualizd initialtion population for next integration step
    initial_pop = [sol[-1,0], sol[-1,1], sol[-1,2]]

    # if normalized intensity is lower than 1e-2 after 
    # relaxation oscillation : no lasing (abitrary criteria)
    if ((sol[-1,2]/laser_sat) <= lasing_criteria) : 
        fct.write_no_lasing(ofile,var)
        return 


    #---------------------------------------------------#
    #---------------------------------------------------#






    #---------------------------------------------------#
    #---------------------------------------------------#
    # integration after relaxation oscillation (larger time step
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

        # actualized initialtion population for next integration step
        initial_pop = [sol[-1,0], sol[-1,1], sol[-1,2]]


        '''
        algorithm to find what the emitted lasing regime is 
        (no lasing, pulse or true cw)
        '''

        int_norm = sol[:,2] / laser_sat

        # no lasing 
        if int_norm < lasing_criteria : 
            fct.write_no_lasing(ofile,var)
        
        # lasing
        else : 
            fct.write_cw(ofile,var)
        return 


    

    #---------------------------------------------------#
    #---------------------------------------------------#

    return 0
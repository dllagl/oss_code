'''
-------------------------------------------------------------------
This file is part of the OSS source code 
Copyright (C) 2021 Anthony Dall'agnol 

This program is free software: you can redistribute it and/or modify 
it under the terms of the GNU General Public License as published 
by the Free Software Foundation, either version 3 of the License, or 
any later version. 
This program is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
GNU General Public License for more details. 
You should have received a copy of the GNU General Public License 
along with this program. If not, see <https://www.gnu.org/licenses/>
-------------------------------------------------------------------

@author    : Anthony Dall'agnol
@copyright : Copyright (C) 2021 Anthony Dall'agnol
@license   : GNU General Public License

-------------------------------------------------------------------
@solver_three_pop : integrate ODE systems S0/S1/T1
@solver_two_pop   : integrate ODE systems S0/S1

Called in: simu_lasing_regime.py
-------------------------------------------------------------------
'''

# external libraries
from numpy import linspace,abs

# external files 
import simu_lasing_regime_fct as fct 





def solver_three_pop(method,sys,initial_pop,tmin,tmax,doping,
    param_arr,laser_sat,ofile,
    time_counter,time_unit,nbr_pts,var) :

    '''
    method          : solver (e.g. odeint)
    sys             : system of equation
    initial_pop     : <array> initial values of the population
    tmin, tmax      : <float> start/end time of integration
    doping          : <float> proportion of active molecule in the film
    param_arr       : <array> constants of the equation (@imp_param.py)
    laser_sat       : <float> saturation of the transition at lasing wavelength
    ofile           : <str>   opened output data file 
    time_counter    : <int>   number of time step from tmin to tmax
    time_unit       : <float> duration of one integration step
    nbr_pts         : <int>   number of points per time_unit
    '''

    # if I/Isat <= lasing_criteria : lasing is gone
    # only fluorescence remains
    lasing_criteria = 1e-2

    #---------------------------------------------------#
    #---------------------------------------------------#
    # integrate first time for relaxation oscillation 
    # (require more points for ~20ns)

    time_osc     = 20e-9
    nbr_pts_osc  = 1e4
    time_vec_osc = linspace(0,time_osc,int(nbr_pts_osc))


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
        time_vec = linspace(tmin,tmax,int(nbr_pts))

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
        diff = abs(int_norm[-1] - int_norm[0])

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

    '''
    method          : solver (e.g. odeint)
    sys             : system of equation
    initial_pop     : <array> initial values of the population
    tmin, tmax      : <float> start/end time of integration
    doping          : <float> proportion of active molecule in the film
    param_arr       : <array> constants of the equation (@imp_param.py)
    laser_sat       : <float> saturation of the transition at lasing wavelength
    ofile           : <str>   opened output data file 
    time_counter    : <int>   number of time step from tmin to tmax
    time_unit       : <float> duration of one integration step
    nbr_pts         : <int>   number of points per time_unit
    '''

    # if I/Isat <= lasing_criteria : lasing is gone
    # only fluorescence remains
    lasing_criteria = 1e-2

    #---------------------------------------------------#
    #---------------------------------------------------#
    # integrate first time for relaxation oscillation 
    # (require more points for ~20ns)

    time_osc     = 20e-9
    nbr_pts_osc  = 1e4
    time_vec_osc = linspace(0,time_osc,int(nbr_pts_osc))


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
        time_vec = linspace(tmin,tmax,int(nbr_pts))

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
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
@solver : integrate the ODE systems defined in @system_populations.py

Called in: simu_populations.py
-------------------------------------------------------------------
'''

# external libraries
from numpy import linspace


def solver(method,sys,initial_pop,tmin,tmax,doping,
    param_arr,output_file,config_file,user_sys_choice,
    time_counter,time_unit,nbr_pts) :

    '''
    method          : solver (e.g. odeint)
    sys             : system of equation
    initial_pop     : <array> initial values of the population
    tmin, tmax      : <float> start/end time of integration
    doping          : <float> proportion of active molecule in the film
    param_arr       : <array> constants of the equation (@imp_param.py)
    laser_sat       : <float> saturation of the transition at lasing wavelength
    output_file     : <str>   output data file 
    config_file     : <str>   output config file 
    user_sys_choice : <int>   define ODE system
    time_counter    : <int>   number of time step from tmin to tmax
    time_unit       : <float> duration of one integration step
    nbr_pts         : <int>   number of points per time_unit
    '''

    ofile = open(output_file,'a+')
    ofile.write('\n\n')
    ofile.write('@config file : %s\n\n' % config_file)

    if user_sys_choice == 1 : 
        ofile.write('%s %15s %13s\n' % ('time', 'S0/N', 'S1/N'))

    elif user_sys_choice == 2 : 
        ofile.write('%s %13s %11s %11s\n' % ('time', 'S0/N', 'S1/N', 'T1/N'))


    for ii in range(time_counter) : 

        # define time vector iteration
        tmin     = ii*time_unit
        tmax     = (ii+1)*time_unit
        time_vec = linspace(tmin,tmax,int(nbr_pts))

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
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
Systems of equations of different configuration

@sys_equations_two_pop   : S0/S1
@sys_equations_three_pop : S0/S1/T1


Called in: simu_populations.py
-------------------------------------------------------------------
'''


# external libraries
from numpy import empty

# external files 
import phys_constants as cs




def sys_equations_two_pop(s, t, doping,param_vec) : 

    '''
    S0    = s[0]
    S1    = s[1]
    '''

    doping,sigma_abs_p, n, N,\
    molar_mass,lambda_abs,lambda_fluo,tau_f,tau_t,\
    sigma_em,sigma_S1S2_pump,sigma_S1S2_laser,sigma_T1T2_pump,sigma_T1T2_laser,kSI,\
    kISC, kSTA, kSSA, kTTA,\
    Ip = param_vec


    # vector of the solution
    sdot = empty((2,))   


    ########################################################

    # S0 equation
    sdot[0] = ( 
            ( - sigma_abs_p * lambda_abs * Ip * s[0] / cs.C_HC )
            + ( s[1] / tau_f ) 
    )

    # S1 equation
    sdot[1] = (
            (sigma_abs_p * lambda_abs * Ip * s[0]) / cs.C_HC
            - ( s[1] * (1/tau_f) )
    )

    ########################################################
    return sdot













def sys_equations_three_pop(s, t, doping, param_vec) : 

    '''
    S0    = s[0]
    S1    = s[1]
    T1    = s[2]
    '''

    # equations parameters
    doping,sigma_abs_p, n, N,\
    molar_mass,lambda_abs,lambda_fluo,tau_f,tau_t,\
    sigma_em,sigma_S1S2_pump,sigma_S1S2_laser,sigma_T1T2_pump,sigma_T1T2_laser,kSI,\
    kISC, kSTA, kSSA, kTTA,\
    Ip = param_vec


    # vector of the solution
    sdot = empty((3,))   


    ########################################################

    # S0 equation
    sdot[0] = ( 
            ( - sigma_abs_p * lambda_abs * Ip * s[0] / cs.C_HC )
            + ( s[1] / tau_f ) 
            + ( s[2] / tau_t )
            + ( kSTA * s[1] * s[2] )
            + ( kTTA * s[2] * s[2] )
            + ( kSSA * s[1] * s[1] )
    )

    # S1 equation
    sdot[1] = (
            (sigma_abs_p * lambda_abs * Ip * s[0]) / cs.C_HC
            - ( s[1] * (1/tau_f + kISC) )
            - ( kSTA * s[1] * s[2] ) 
            + (cs.C_ZETA * kTTA * s[2] * s[2] )
            - ( kSSA * s[1] * s[1] * (2- cs.C_ZETA) )
            - ( sigma_S1S2_pump * (1-kSI) * lambda_abs * Ip * s[1] / cs.C_HC )
    )

    # T1 equation
    sdot[2] = (
            ( kISC * s[1] )
            - ( s[2] / tau_t )
            + ( kSSA * s[1] * s[1] * (1-cs.C_ZETA) )
            - ( (1+cs.C_ZETA) * kTTA * s[2] * s[2] )
            - ( sigma_T1T2_pump * lambda_abs * Ip * s[2] / cs.C_HC )
            + ( sigma_S1S2_pump * (1-kSI) * lambda_abs * Ip * s[1] / cs.C_HC )
    )

    ########################################################
    return sdot

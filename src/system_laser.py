


# external libraries
import numpy as np 

# external files 
import phys_constants as cs




def sys_equations_two_pop(s, t, doping, param_vec) : 

    '''
    S0  = s[0]
    S1  = s[1]
    I   = s[2]
    '''

    doping,sigma_abs_p, n, N,\
    molar_mass,lambda_abs,lambda_fluo,tau_f,tau_t,\
    sigma_em,sigma_S1S2_pump,sigma_S1S2_laser,sigma_T1T2_pump,sigma_T1T2_laser,kSI,\
    kISC, kSTA, kSSA, kTTA,\
    Ip,\
    gama,qfactor,nu,tau_cav,pump_area,spont = param_vec

    
    # vector of the solution
    sdot = np.empty((3,))   


    ########################################################

    # S0 equation
    sdot[0] = ( 
            ( - sigma_abs_p * lambda_abs * Ip * s[0] / cs.C_HC )
            + ( s[1] / tau_f ) 
            + ( kSSA * s[1] * s[1] )
            + ( s[1] * sigma_em * s[2] * lambda_fluo / cs.C_HC )
    )

    # S1 equation
    sdot[1] = (
            (sigma_abs_p * lambda_abs * Ip * s[0]) / cs.C_HC
            - ( s[1] * (1/tau_f) )
            - ( kSSA * s[1] * s[1] * (2- cs.C_ZETA) )
            - ( s[1] * sigma_em * s[2] * lambda_fluo / cs.C_HC )
    )

    # intensity equation
    sdot[2] = (
            cs.C_C/n * N * gama * sigma_em * s[1] * (s[2] + spont)
            - (s[2] / tau_cav)		
    )

    ########################################################
    return sdot













def sys_equations_three_pop(s, t, doping, param_vec) : 

    '''
    S0 = s[0]
    S1 = s[1]
    T1 = s[2]
    T  = s[3]
    '''

    # equations parameters
    doping,sigma_abs_p, n, N,\
    molar_mass,lambda_abs,lambda_fluo,tau_f,tau_t,\
    sigma_em,sigma_S1S2_pump,sigma_S1S2_laser,sigma_T1T2_pump,sigma_T1T2_laser,kSI,\
    kISC, kSTA, kSSA, kTTA,\
    Ip,\
    gama,qfactor,nu,tau_cav,pump_area,spont = param_vec


    # vector of the solution
    sdot = np.empty((4,))   


    ########################################################

    # S0 equation
    sdot[0] = ( 
            ( - sigma_abs_p * lambda_abs * Ip * s[0] / cs.C_HC )
            + ( s[1] / tau_f ) 
            + ( s[2] / tau_t )
            + ( kSTA * s[1] * s[2] )
            + ( kTTA * s[2] * s[2] )
            + ( kSSA * s[1] * s[1] )
            + ( s[1] * sigma_em * s[3] * lambda_fluo / cs.C_HC )
    )

    # S1 equation
    sdot[1] = (
            (sigma_abs_p * lambda_abs * Ip * s[0]) / cs.C_HC
            - ( s[1] * (1/tau_f + kISC) )
            - ( kSTA * s[1] * s[2] ) 
            + ( cs.C_ZETA * kTTA * s[2] * s[2] )
            - ( kSSA * s[1] * s[1] * (2- cs.C_ZETA) )
            - ( s[1] * sigma_em * s[3] * lambda_fluo / cs.C_HC )
            - ( sigma_S1S2_pump * (1-kSI) * lambda_abs * Ip * s[1] / cs.C_HC )
    )

    # T1 equation
    sdot[2] = (
            ( kISC * s[1] )
            - ( s[2] / tau_t )
            + ( kSSA * s[1] * s[1] * (1-cs.C_ZETA) )
            - ( (1+cs.C_ZETA) * kTTA * s[2] * s[2] )
            + ( sigma_S1S2_pump * (1-kSI) * lambda_abs * Ip * s[1] / cs.C_HC )
            - ( sigma_T1T2_pump * lambda_abs * Ip * s[2] / cs.C_HC )
    )

    # intensity equation
    sdot[3] = ( 
            cs.C_C/n * N * gama * sigma_em * s[1] * (s[3] + spont)
            - (cs.C_C/n * N * gama * sigma_T1T2_laser * s[2] * s[3])
            - (s[3] / tau_cav)		
    )

    ########################################################
    return sdot
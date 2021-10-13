


# external libraries
import numpy as np 

# external files 
import constants as cs




def sys_equations_two_pop(s, t, doping, Ip,
                param_sample,
                param_molecule,
                param_interaction_rate) : 

    '''
    S0    = s[0]
    S1    = s[1]
    '''

    # equations parameters
    doping,sigma_abs_p, n, N = param_sample
    molar_mass,lambda_abs,lambda_fluo,tau_f,tau_t,sigma_em,sigma_S1S2_pump,sigma_S1S2_laser,sigma_T1T2_pump,sigma_T1T2_laser,kSI = param_molecule
    kISC, kSTA, kSSA, kTTA = param_interaction_rate


    # vector of the solution
    sdot = np.empty((2,))   


    ########################################################

    # S0 equation
    sdot[0] = ( 
            ( - sigma_abs_p * lambda_abs * Ip * s[0] / cs.C_HC )
            + ( s[1] / tau_f ) 
            + ( kSSA * s[1] * s[1] )
    )

    # S1 equation
    sdot[1] = (
            (sigma_abs_p * lambda_abs * Ip * s[0]) / cs.C_HC
            - ( s[1] * (1/tau_f) )
            - ( kSSA * s[1] * s[1] * (2- cs.C_ZETA) )
    )

    ########################################################
    return sdot













def sys_equations_three_pop(s, t, doping, Ip,
                param_sample,
                param_molecule,
                param_interaction_rate) : 

    '''
    S0    = s[0]
    S1    = s[1]
    T1    = s[2]
    '''

    # equations parameters
    doping,sigma_abs_p, n, N = param_sample
    molar_mass,lambda_abs,lambda_fluo,tau_f,tau_t,sigma_em,sigma_S1S2_pump,sigma_S1S2_laser,sigma_T1T2_pump,sigma_T1T2_laser,kSI = param_molecule
    kISC, kSTA, kSSA, kTTA = param_interaction_rate


    # vector of the solution
    sdot = np.empty((3,))   


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
            + ( cs.C_ZETA * kTTA * s[2] * s[2] )
            - ( kSSA * s[1] * s[1] * (2- cs.C_ZETA) )
    )

    # T1 equation
    sdot[2] = (
            ( kISC * s[1] )
            - ( s[2] / tau_t )
            + ( kSSA * s[1] * s[1] * (1-cs.C_ZETA) )
            - ( (1+cs.C_ZETA) * kTTA * s[2] * s[2] )
    )

    ########################################################
    return sdot
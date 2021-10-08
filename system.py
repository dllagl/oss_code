import numpy as np 




def sys_equations(s, t, doping, Ip,
                param_sample,
                param_molecule,
                param_interaction_rate) : 

    '''
    S0    = s[0]
    S1    = s[1]
    T1    = s[2]
    I(t)  = s[3]
    '''

    # equations parameters
    doping,sigma_abs_p, n, N = param_sample
    molar_mass,lambda_abs,lambda_fluo,tau_f,tau_t,sigma_em,sigma_S1S2_pump,sigma_S1S2_laser,sigma_T1T2_pump,sigma_T1T2_laser,kSI = param_molecule
    kISC, kSTA, kSSA, kTTA = param_interaction_rate




    # vector of the solution
    sdot = np.empty((3,)) 
    
    # plank's constant * speed of light
    hc = 1.9864458571489286e-25 
    
    # speed of light
    c  = 299792458.0      

    zeta = 0.25
    # singlets spin-statistics creation ratio   




    ########################################################

    # S0 equation
    sdot[0] = ( 
            ( - sigma_abs_p * lambda_abs * Ip * s[0] / hc )
            + ( s[1] / tau_f ) 
            + ( s[2] / tau_t )
            + ( kSTA * s[1] * s[2] )
            + ( kTTA * s[2] * s[2] )
            + ( kSSA * s[1] * s[1] )
    )

    # S1 equation
    sdot[1] = (
            (sigma_abs_p * lambda_abs * Ip * s[0]) / hc
            - ( s[1] * (1/tau_f + kISC) )
            - ( kSTA * s[1] * s[2] ) 
            + ( zeta * kTTA * s[2] * s[2] )
            - ( kSSA * s[1] * s[1] * (2- zeta) )
    )



    # T1 equation
    sdot[2] = (
            ( kISC * s[1] )
            - ( s[2] / tau_t )
            + ( kSSA * s[1] * s[1] * (1-zeta) )
            - ( (1+zeta) * kTTA * s[2] * s[2] )
    )



    ########################################################





    return sdot
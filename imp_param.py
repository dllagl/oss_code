


# external libraries
import numpy as np 

# external files 
import constants as cs





# molecule intrinsic parameters
def param_molecule() :

    '''
    molar mass  : (kg/mol)
    lambda_abs  : absorption at the pump wavelength (m)
    lambda_fluo : mean fluorescence wavelength (m)

    tau_f : fluorescence lifetime (s)
    tau_t : triplet lifetime (s)

    sigma_em         : absorption cross section at the laser wavelength (m2)
    sigma_S1S2_pump  : absorption cross section of S1->S2 at the pump wavelength (m2)
    sigma_S1S2_laser : absorption cross section of S1->S2 at the laser wavelength (m2)
    sigma_T1T2_pump  : absorption cross section of T1->T2 at the pump wavelength (m2)
    sigma_T1T2_laser : absorption cross section of T1->T2 at the laser wavelength (m2)
    kSI              : probability for one molecule in Sn to fall down to S1
    '''

    molar_mass       = 339.44e-3  
    lambda_abs       = 408e-9
    lambda_fluo      = 480e-9
    tau_f            = 1.28e-9
    tau_t            = 175e-6
    sigma_em         = 2.8e-20
    sigma_S1S2_pump  = 0.0
    sigma_S1S2_laser = 0.0
    sigma_T1T2_pump  = 0.0
    sigma_T1T2_laser = 0.0
    kSI              = 0.9

    arr= [molar_mass,lambda_abs,lambda_fluo,tau_f,tau_t,
        sigma_em,sigma_S1S2_pump,sigma_S1S2_laser,
        sigma_T1T2_pump,sigma_T1T2_laser,kSI]

    return arr










# sample parameters 
def param_sample(molar_mass) : 

    '''
    doping         : ratio of dye molecule in the host matrix (0 to 1)
    rho_matrix     : density of the host matrix of the dye (kg/m3)
    nbr_active_mol : number of dye molecule (m-3)
    absorption     : A = 1-R-T 
    thickness      : thicknes of the film or the cuvette 
    alpha          : absorption coefficient (m-1)
    sigma_abs_pump : absorption cross section at the pump wavelength (m2) 
    '''
    
    doping          = 1.0
    rho_matrix      = 1.15e3
    nbr_active_mol  = (doping*rho_matrix*cs.C_AVO) / molar_mass
    absorption      = 0.8
    thickness       = 200e-9
    alpha           = - np.log(1-absorption) / thickness
    sigma_abs_pump  = alpha/nbr_active_mol
    neff            = 1.7


    return [doping, sigma_abs_pump,neff,nbr_active_mol]














# photophysical rates 
def param_rates(nbr_dye_molecules) : 

    '''
    kisc : intersystem crossing (s-1)
    ksta : singlet-triplet annihilation (m3/s) 
    ktta : triplet-triplet annihilation (m3/s)
    kssa : singlet-singlet annihilation (m3/s)

    Careful : In this system, the populations S0,S1,T1
    are normalized, hence the factor "nbr_dye_molecules"
    for every interactions that are proportionnal to 
    the populations.
    '''

    kisc = 1e8
    ksta = 1e-10 * 1e-6 * nbr_dye_molecules
    ktta = 0.0 * 1e-6 * nbr_dye_molecules
    kssa = 0.0 * 1e-6 * nbr_dye_molecules


    return [kisc,ksta,kssa,ktta]










# pump parameters
def param_pump() : 

    '''
    pump fluence : fluence of the pump (kW/cm2) * 1e7 (W/m2)
    '''

    pump_fluence    = 10 * 1e7

    return [pump_fluence]











# time parameters
def param_time() : 

    # start of the integration
    tmin = 0.0
    # end of the integration
    tmax = eval(input('Enter a time of integration in secs (ex: 10e-6) :  '))

    return tmin,tmax
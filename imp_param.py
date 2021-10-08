

from math import log



# constants 
AVOGADRO = 6.0221407e23



# molecule intrinsic parameters
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

molar_mass        = 339.44e-3  
lambda_abs        = 450e-9
lambda_fluo       = 521e-9
tau_f             = 1e-9
tau_t             = 100e-6
sigma_em          = 1e-20
sigma_S1S2_pump   = 0.0
sigma_S1S2_laser  = 0.0
sigma_T1T2_pump   = 0.0
sigma_T1T2_laser  = 0.0
kSI               = 0.9





# sample parameters 
'''
doping         : doping_ratio from 0 to 1 (1=neat)
rho_matrix     : density of the host matrix of the dye (kg/m3)
nbr_active_mol : number of dye molecule (m-3)
absorption     : A = 1-R-T 
thickness      : thicknes of the film or the cuvette 
alpha          : absorption coefficient (m-1)
sigma_abs_pump : absorption cross section at the pump wavelength (m2) 
'''

doping            = 1.0
rho_matrix        = 1.15e3
nbr_active_mol    = (doping*rho_matrix*AVOGADRO) / molar_mass
absorption        = 0.8
thickness         = 17e-6
alpha             = - log(1-absorption) / thickness
sigma_abs_pump    = alpha/nbr_active_mol
neff              = 1.7





# photophysical rates 
'''
kisc : intersystem crossing (s-1)
ksta : singlet-triplet annihilation (m3/s) 
ktta : triplet-triplet annihilation (m3/s)
kssa : singlet-singlet annihilation (m3/s)

Careful : In this system, the populations S0,S1,T1
are normalized, hence the factor "nbr_active_mol"
for every interactions that are proportionnal to 
the populations.
'''

kisc              = 1e7
ksta              = 1e-10 * 1e-6 * nbr_active_mol
ktta              = 0.0 * 1e-6 * nbr_active_mol
kssa              = 0.0 * 1e-6 * nbr_active_mol

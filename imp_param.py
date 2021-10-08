

import numpy as np 

# constants 
AVOGADRO = 6.0221407e23

# molecule intrinsic parameters
molar_mass        = 339.44e-3  
lambda_abd        = 450e-9
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
doping            = 1.0
rho_matrix        = 1.15e3
nbr_active_mol    = (doping*rho_matrix*AVOGADRO) / molar_mass
absorption        = 0.8
thickness         = 17e-6
alpha             = - np.log(1-absorption) / thickness
sigma_abs_pump    = alpha/nbr_active_mol
neff              = 1.7

# photophysical rates 
kisc              = 1e7
ksta              = 1e-10 * 1e-6 * nbr_active_mol
ktta              = 0.0 * 1e-6 * nbr_active_mol
kssa              = 0.0 * 1e-6 * nbr_active_mol

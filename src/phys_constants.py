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
Physical constants

Called in: system_laser.py,system_populations.py,simu_laser.py,
imp_param.py
-------------------------------------------------------------------
'''

# general physical constants used in the differents files

C_PI    = 3.14157         # PI
C_C     = 299792458.0     # speed of light (m.s-1)
C_ZETA  = 0.25            # spin statistic singlet creation
C_AVO   = 6.0221407e23    # Avogadro's contants (mol-1)
C_H     = 6.62607015e-34  # Planck's constants (J.s-1)
C_HC    = C_H * C_C 
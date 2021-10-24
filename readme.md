# OSS : Organic Systems Simulator

Terminal based application to study the energy state population dynamics of organic lasing devices.

## Recommanded tools

- Git 
- A text editor (e.g. [VS code](https://code.visualstudio.com/)) for UNIX system users
- A Python IDE (e.g. [Spyder](https://www.spyder-ide.org/)) for Windows users

## Required libraries

- numpy >= 1.21.2
- matplotlib >= 3.3.3
- scipy.integrate >= 1.6.0
- platform >= 2.0.2
- os 

To check if libraries are installed on your computer, run the following command. 
```bash
numpy --version
```

If you don't use an integrated development environement, follow these instructions to install missing librairies.

#### 1. Install pip 

Download this python script [get-pip.py](https://bootstrap.pypa.io/get-pip.py) and execute it,
```bash
cd path/to/get-pip.py
python get-pip.py
```
or install it from your package manager. 
```bash
sudo apt update 
sudo apt install python3-pip
```

#### 2. Install some libraries 
```bash 
pip install --m numpy 
```


## Obtain the source code 
You can download it on the [main page](https://github.com/dllagl/tui.git) or clone it on your computer. 
```bash 
cd path/to/your/work/folder
git clone https://github.com/dllagl/tui.git
```

## Run simulations 

#### 1. Execute OSS source code

Once you are in the 'oss' folder and you have the required libraries you can execute the OSS code. 
```bash 
python main.py 
```
If you choose the default names for the folders and files, it will create an 'output' folder in the same 
directory with the output data files in it.

#### 2. Run it your way

Other than implementing your own functions and fork the project, the only interation you need to have 
with the code is when changing the initial inputs in the `imp_param.py` python file. 

```python
# molecule intrinsic parameters
def param_molecule() :

    '''
    molar mass  : (kg/mol)
    lambda_abs  : absorption at the pump wavelength (m)
    lambda_fluo : mean fluorescence wavelength (m)
    tau_f       : fluorescence lifetime (s)
    tau_t       : triplet lifetime (s)
    sigma_em    : absorption cross section at the laser wavelength (m2)
    kSI         : probability for one molecule in Sn to fall down to S1
    '''

    molar_mass       = 339.44e-3  
    lambda_abs       = 408e-9
    lambda_fluo      = 480e-9
    tau_f            = 1.28e-9
    tau_t            = 175e-6
    sigma_em         = 2.8e-20
    kSI              = 0.9

    arr= [molar_mass,lambda_abs,lambda_fluo,tau_f,tau_t,
        sigma_em,sigma_S1S2_pump,sigma_S1S2_laser,
        sigma_T1T2_pump,sigma_T1T2_laser,kSI]

    return arr
```
Each python file can 
be opened with a typical text editor. 


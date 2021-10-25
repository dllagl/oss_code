# OSS : Organic Systems Simulator

Terminal based application to study the energy state population dynamics of organic lasing devices.

## Tables of contents
1. Recommended tools
2. Required tools
3. Installing missing libraries
4. Obtain the source code
5. Run simulations 
## Recommended tools

- Git 
- A text editor (e.g. [VS code](https://code.visualstudio.com/)) or a Python IDE (e.g. [Spyder](https://www.spyder-ide.org/))

## Required 
- Python 3.X
- numpy >= 1.21.2
- matplotlib >= 3.3.3
- scipy >= 1.6.0
- platform >= 2.0.2
- os 

NOTE : If you use an integrated developement environement such as Spyder, you should not be concerned by the lake of libraries on your computer. 

Although basic ones are pre-installed in most Linux distributions or in MacOS, specific ones sometimes require manual installation.
To check if the library `example` is installed on your computer, run the following command on a terminal:
```bash
pip freeze | grep <example>
```
If PIP is not installed, look for the required module in `/usr/lib/python3.X/site-packages` or follow the next section to install PIP.

## Install missing libraries

### 1. Install pip 

PIP is a terminal tool used to ease the installation of external packages or libraries. If you want more details, look over the [documentation](https://docs.python.org/fr/3.6/installing/index.html).
There are two main ways to install it on your computer. You can download either this [python script](https://bootstrap.pypa.io/get-pip.py) and execute it by running these command in a terminal:

```bash
cd path/to/get-pip.py
python get-pip.py
```
or install it from your package manager. 
```bash
sudo apt update 
sudo apt install python3-pip
```
The syntax will be similar for most Linux distribution or in MacOS.

### 2. Install some libraries 
To install the library `example`, run this command from anywhere on a terminal:
```bash 
pip install --m example 
```


## Obtain the source code 
You can download it on the [main page](https://github.com/dllagl/tui.git) or clone it on your computer. 
```bash 
cd path/to/your/work/folder
git clone https://github.com/dllagl/tui.git
```

## Run simulations 

### 1. Execute OSS source code

Once you are in the 'oss' folder and you have the required libraries you can execute the OSS code. 
```bash 
python main.py 
```

This will automatically create a folder name after what you enter in the terminal prompt (`output` by default) which will contain : 
-  `data.out` which contain the output datas (time, populations ..)
- `data.params` which contain the configuration of the simulation (date, computer's infos and contants)

Examples of those files can be found in the `refs` folder for each available simulation.
Note that `data` is the default name and is easily customizable when going through the terminal prompt of the program.

### 2. Run it your way

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


### 3. Read the output files 

A python script `read.py` can be found in the `refs` folder alongside output files to guide the Python beginners to plot the results of their simulations. 
Besides, all datas are written in text files so they can be processed in any language.

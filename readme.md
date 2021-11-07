# OSS : Organic Systems Simulator

Terminal based application to study the energy state population dynamics of organic lasing devices.

## Tables of contents
1. [Introduction](#introduction)
2. [Copyright and license](#copyright-and--license)
3. [Recommended tools](#recommended-tools)
4. [Required modules](#required-modules)
5. [Install missing libraries](#install-missing-libraries)
6. [Obtain the source code](#Obtain-the-source-code)
7. [Run simulations](#run-simulations) 
8. [Useful ressources](#useful-ressources)


## Introduction 
The OSS code can be used to simulate the dynamics of the energy states populations of organic molecules. Thanks to its relative simplicity, it can also easily be used to study the evolution of the photon density inside a resonator, from DFBs to VCSELs.
Moreover, an original algorithm is implemented to evaluate the lasing regime (none, pulse, CW) in a given photophysical and optical configuration. 

The details concerning the core of the equations and the different algorithms used in OSS are extensively discussed in the [white sheet](doc/whitesheet.pdf) of the project and in the cited [published papers](#useful-ressources).

The project folder is structured as follows:
- Python scripts : contain the source code of the project
- Refs : example of the output datas processed by the program for each available simulation.
- Doc : whitesheet of the project and scientifics references to look over.

## Copyright and license
The OSS project is licensed under the GNU General Public License version 3. The details of this license can be found in the file `LICENSE.md`.


## Recommended tools

- [Git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git) 
- A text editor (e.g. [VS code](https://code.visualstudio.com/)) or a Python IDE (e.g. [Spyder](https://www.spyder-ide.org/))

## Required modules
- Python 3.X
- numpy >= 1.21.2
- matplotlib >= 3.3.3
- scipy >= 1.6.0
- platform >= 2.0.2
- os 

NOTE : If you use an integrated developement environement such as Spyder, you should not be concerned by the lake of libraries on your computer. 

Although basic modules are pre-installed in most Linux distributions or in MacOS, specific ones sometimes require manual installation.
To check if the module `example` is installed on your computer, run the following command on a terminal:
```bash
cd /usr/lib/python3.X/site-packages/
ls -l | grep <example>
```
where `X` is your current version of python, obtained by the command `python --version`.

## Install missing libraries

### 1. Install pip 

PIP is a terminal tool used to ease the installation of external packages or libraries. If you want more details, look over the [documentation](https://docs.python.org/fr/3.6/installing/index.html).
There are two main ways to install it on your computer. You can either download this [python script](https://bootstrap.pypa.io/get-pip.py) and execute it by running these command in a terminal:

```bash
cd path/to/get-pip.py
python get-pip.py
```
or install it from your package manager. 
```bash
sudo apt update 
sudo apt install python3-pip
```

### 2. Install some libraries 
To install the Python module `example`, run this command from anywhere on a terminal:
```bash 
pip install --m <example> 
```

It is recommended to check afterwards that the module is installed correctly in your system.
```bash
pip freeze | grep <example>
```


## Obtain the source code 
You can download it on the [main page](https://github.com/dllagl/tui.git) or clone it (provided that [git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git) is installed on your machine)via the following commands. This will automatically create a folder `tui` containing each files and folders of the project.
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

Examples of those files can be found in the [refs](refs) folder for each available simulation.

### 2. Run it your way

Other than implementing your own functions and fork the project, the only interation you need to have 
with the code is when changing the initial inputs in the [imp_param.py](imp_param.py) python file. 


### 3. Read the output files 

Python scripts can be found alongside examples data files to guide the Python beginners to plot the results of their simulations. 
Moreover, datas are written in text files so they can be processed in any language.


## Useful ressources

### 1. Scientific papers

Here are some peer-reviewed scientific papers, Ph.D. thesis or books that work with the system of equations implemented in OSS : 
- [[1]](https://doi.org/10.1063/1.2425003) C. Gärtner, C. Karnutsch, U. Lemmer and C. Pflumm, Journal
of Applied Physics, 2007, 101, 023107
- [[2]](https://link.springer.com/book/10.1007/978-3-642-36705-2) S. Forget and S. Chénais, Organic solid-state lasers, Springer,
Heidelberg, 2013.
- [[3]](https://doi.org/10.1063/1.5121485) F. Bencheikh, A. S. D. Sandanayaka, T. Fukunaga, T. Mat-
sushima and C. Adachi, Journal of Applied Physics, 2019, 126,
185501.


### 2. Instructional videos (ongoing production)

<!-- In order to help new users to get the most out of OSS, a few videos have been recorded.
- Windows :
- UNIX :  -->

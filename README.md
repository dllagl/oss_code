# OSS : Organic Systems Simulator

Terminal based application to study the energy state population dynamics of organic semiconductor lasers.

## Tables of contents
1. [Introduction](#introduction)
2. [Copyright and license](#copyright-and-license)
3. [Recommended tools](#recommended-tools)
4. [Required modules](#required-modules)
5. [Install missing libraries](#install-missing-libraries)
6. [Obtain the source code](#Obtain-the-source-code)
7. [Run simulations](#run-simulations) 
8. [Useful ressources](#useful-ressources)
9. [Roadmap](#roadmap)


## Introduction 
The OSS code can be used to simulate the dynamics of the energy states populations of organic molecules in thin films. The populations can be integrated with or without a resonator via an equation governing the photon density inside it.
Moreover, an algorithm is implemented to evaluate the lasing regime in precise photophysical and optical configurations. 

The details concerning the core of the equations and the different algorithms used in OSS are extensively discussed in the [white sheet](doc/whitesheet.pdf) of the project and in the cited [published papers](#useful-ressources).

The project folder is structured as follows:
- src : python scripts to run the proram
- refs : example of the output datas processed by the program for each available simulation.
- doc : whitesheet of the project and scientifics references to look over. (not published yet)

## Copyright and license
The OSS project is licensed under the GNU General Public License version 3. The details of this license can be found in the file `LICENSE.md`.


## Recommended tools

- Git
- A text editor (e.g. [VS code](https://code.visualstudio.com/)) or a Python IDE (e.g. [Spyder](https://www.spyder-ide.org/))

## Required modules
- Python 3.X
- numpy >= 1.21.2
- matplotlib >= 3.3.3
- scipy >= 1.6.0
- platform >= 2.0.2
- os 

NOTE : If you use an integrated developement environement, you should not be concerned by the lake of libraries on your computer. 

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
You can download it on the main page or clone it via the following commands. This will automatically create a folder `oss` containing each files and folders of the project.
```bash 
cd path/to/your/work/folder
git clone https://github.com/dllagl/oss.git
```

## Run simulations 

### 1. Execute OSS source code

Once you are in the 'oss' folder and you have the required libraries you can execute the OSS code. 
```bash 
cd src
python main.py 
```

This will automatically create a folder name after what you enter in the terminal prompt (`output` by default) which will contain : 
-  `data.out` which contains the output datas (time, populations ..)
- `data.params` which contains the configuration of the simulation (date, computer's infos and contants)

Examples of those files can be found in the [refs](refs) folder for each available simulation.

### 2. Run it your way

For the simpliest simulations options, the only interactions you need to have with the code is to change the values of the photophysical and optical constants in [imp_param.py](src/imp_param.py).
The prompt will guide you for other options.


### 3. Read the output files 

Python scripts can be found alongside examples data files to guide Python beginners to plot the results of their simulations. 
Since datas are written in text files, they can be processed in any language anyway.


## Useful ressources

### 1. Scientific papers

Here are some peer-reviewed scientific papers, Ph.D. thesis or books that work with the system of equations implemented in OSS : 
- [[1]](https://doi.org/10.1063/1.2425003) C. Gärtner, C. Karnutsch, U. Lemmer and C. Pflumm, Journal
of Applied Physics, 2007, 101, 023107
- [[2]](https://link.springer.com/book/10.1007/978-3-642-36705-2) S. Forget and S. Chénais, Organic solid-state lasers, Springer,
Heidelberg, 2013.
- [[3]](https://doi.org/10.1063/1.5121485) F. Bencheikh, A. S. D. Sandanayaka, T. Fukunaga, T. Mat-
sushima and C. Adachi, Journal of Applied Physics, 2019, 126, 185501.


### 2. Instructional videos (ongoing production)

<!-- In order to help new users to get the most out of OSS, a few videos have been recorded.
- Windows :
- UNIX :  -->



## Roadmap 

- [ ] Write complete documentation 
- [ ] Tutorial videos
- [ ] Parallelize lasing regime computation 
- [ ] Add an option to iterate over two variables at once for the lasing regime study
- [ ] Add different cavities    

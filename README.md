
# Notepad

This is a GUI project made to clone a basic Notepad of our computer.

## Features

- Toolbar & Statusbar are displayed by default.
- Can hide Toolbar & Statusbar.
- Can open or save any type of file you want.


## Modules Used

- tkinter
- os


## Event Bindings 

The most important part to make a better GUI is to learn the event binding process. The most used key bindings in tkinter with their uses are:

|Event Key | Key Binded |
|----------|------------|
|Button-1  |Single left click |
|Button-3  |Single right click |
|Return    |Enter key |
|ButtonRelease|Release mouse button |
|Enter     |Mouse cursor entering in the widget |
|Double-Button-1  |Double left click |
|Double-Button-3  |Double right click |
|Leave |Mouse cursor leaving the widget |

  
## How to convert .py to.exe

By converting into a executable file, you can run this program on any computer irrespective the system has python installed or not. 

You can convert this project(.py) into a executable file(.exe) by following the steps mentioned: 

- Open the command prompt and run command given below.
- First command to make both.exe file with MicroSoft Installer(MSI) setup. 
- Second command to make only .exe file.
```bash
setup.py bsdit_msi
setup.py build
```

## Installation of setup (.msi file)

- Open the setup file.
- Select the directory, make sure that a folder is been selected where you install the software
- Click on Install and the Notepad will be successfully installed.

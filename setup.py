import cx_Freeze
# import os
import sys
base=None

if sys.platform=="win32":
    base="Win32GUI"

# os.environ["TCL_LIBRARY"]=r"C:\Users\Hp\AppData\Local\Programs\Python\Python38-32\tcl\tcl8.6"
# os.environ["Tk_LIBRARY"]=r"C:\Users\Hp\AppData\Local\Programs\Python\Python38-32\tcl\tk8.6"

executables = [cx_Freeze.Executable("Notepad.py", base=base, icon="1.ico")]

cx_Freeze.setup(
    name="Notepad",
    options={"build_exe" : {"packages":["tkinter", "os"], "include_files":["1.ico", "tcl86t.dll", "tk86t.dll", "icons for notepad"]}},
    version="2.4.16",
    description="Notepad - Jay Patel & Priyanshi Desai",
    executables=executables
)
import shutil
import os
from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]
includefiles = ["defintions.zip", "extruders.zip"]
packages = ["os", "zipfile", "getpass", "urllib.request", "shutil", "sys", ]
options = {
    'build_exe': {    
        'packages':packages,
        'include_files':includefiles
    },    
}

setup(
    name = "Cura-Setup",
    options = options,
    version = "4.9",
    description = 'Setting up cura',
    executables = executables,
)
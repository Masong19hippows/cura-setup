import os
import sys
import shutil
import zipfile
import getpass
import urllib.request

user = getpass.getuser()
if os.name == 'nt':
    usrDir = f'C:/Users/{user}/AppData/Roaming/cura/4.9/'
    mainDir = "C:/Program Files/Ultimaker Cura 4.9.0/resources/"
    configDir = f'C:/Users/{user}/AppData/Roaming/cura/4.9/'
else:
    mainDir = f'/home/{user}/squashfs-root/usr/bin/resources/'
    configDir = f'/home/{user}/.config/cura/4.9/'
    usrDir = f'/home/{user}/.local/share/cura/4.9/'
    os.chdir(f'/home/{user}/')
    os.system("./cura --appimage-extract")
    
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

qidiVar = "\n[QidiPrint]\ninstances = " + '{\
"Qidi-Home-Internal": \
{"ip": "192.168.1.91"}, \
"Qidi-Home-External": \
{"ip": "' + external_ip + '"}}\n'

octoVar = "\n[octoprint]\n" + "manual_instances = " + '{\
"Octo-Home-External": \
{"address": "' + external_ip + '", "port": 80, "path": "/", "useHttps": false, "userName": "", "password": ""}, \
"Octo-Home-Internal": \
{"address": "192.168.1.169", "port": 80, "path": "/", "useHttps": false, "userName": "", "password": ""}} \
\nkeys_cache = eyJPY3RvLUhvbWUtRXh0ZXJuYWwiOiAiOTJFNTdBREI3N0IyNDUxNjhENzgxREQ0NjU2MjZDRDAifQ==\
\nuse_zeroconf = False\n'

with open(configDir + "cura.cfg",'r') as config_file:
    content = config_file.read()
    new = content.replace("[QidiPrint]", qidiVar)
    new_new = new.replace("[octoprint]", octoVar)

with open(configDir + "cura.cfg", "w") as new_file:    
    new_file.write(new_new)

with zipfile.ZipFile(os.getcwd + "definitions.zip","r") as zip_ref:
    zip_ref.extractall(mainDir + "defintions")

with zipfile.ZipFile(os.getcwd + "extruders.zip","r") as zip_ref:
    zip_ref.extractall(mainDir + "extruders")

with zipfile.ZipFile(os.getcwd + "QidiPrint.zip","r") as zip_ref:
    zip_ref.extractall(usrDir + "plugins")

if sys.platform == "linux":
    os.chdir("/home/{user}/cura-setup")
    os.system(f"./appimage -v /home/{user}/squashfs-root")
    shutil.move(os.getcwd + "Cura-x86_64.AppImage", "~/cura")
    os.system("chmod +x ~/cura")

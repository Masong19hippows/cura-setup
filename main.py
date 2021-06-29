import os
import sys
import shutil
import zipfile
import getpass
import urllib.request

user = getpass.getuser()
if os.name == 'nt':
    usrDir = f'C:/Users/{user}/AppData/Roaming/cura/4.9'
    mainDir = "C:/Program Files/Ultimaker Cura 4.9.0/resources"
    configDir = f'C:/Users/{user}/AppData/Roaming/cura/4.9'
else:
    mainDir = f'/home/{user}/squashfs-root/usr/bin/resources'
    configDir = f'/home/{user}/.config/cura/4.9'
    os.system(f"mkdir -p {configDir}")
    usrDir = f'/home/{user}/.local/share/cura/4.9'
    os.chdir(f'/home/{user}')
    os.system("./cura --appimage-extract")
    os.chdir(f'/home/{user}/cura-setup')

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

with open(os.path.join(configDir, "cura.cfg"), "a") as new_file:
    new_file.write(octoVar + qidiVar)

with zipfile.ZipFile(os.path.join(os.getcwd(), "definitions.zip"),"r") as zip_ref:
    zip_ref.extractall(os.path.join(mainDir, "definitions"))

with zipfile.ZipFile(os.path.join(os.getcwd(), "extruders.zip"),"r") as zip_ref:
    zip_ref.extractall(os.path.join(mainDir, "extruders"))

if sys.platform == "linux":
    os.system(f"./appimagetool -v /home/{user}/squashfs-root")
    shutil.move(os.path.join(os.getcwd(), "Cura-x86_64.AppImage"), f"/home/{user}/cura")
    os.system(f"chmod +x ~/cura")
    os.system(f"rm -r {os.path.join(os.getcwd(), 'squashfs-root')}")


import os
import sys
import shutil
import zipfile
import getpass
import urllib.request
from distutils.version import LooseVersion

versionSet = []
user = getpass.getuser()
compare = "0"
if os.name == 'nt':
    for f in os.listdir(f'C:/Users/{user}/AppData/Roaming/cura'):
        if not f.startswith('st'):
            versionSet.append(f)
    for f in versionSet:
        if LooseVersion(f) > LooseVersion(compare):
            compare = f
            version = f
    if version.count('.') == 2:
        programVersion = version
    elif version.count('.') == 0:
        programVersion = version + ".0.0"
    else:
        programVersion = version + ".0"

    mainDir = f'C:/Program Files/Ultimaker Cura {programVersion}/resources'
    configDir = f'C:/Users/{user}/AppData/Roaming/cura/{version}'
else:
    for f in os.listdir(f'/home/{user}/.config/cura'):
        if not f.startswith('st'):
            versionSet.append(f)
    for f in versionSet:
        if LooseVersion(f) > LooseVersion(compare):
            compare = f
            version = f
    if version.count('.') == 2:
        programVersion = version
    elif version.count('.') == 0:
        programVersion = version + ".0.0"
    else:
        programVersion = version + ".0"

    mainDir = f'/home/{user}/squashfs-root/usr/bin/resources'
    configDir = f'/home/{user}/.config/cura/{version}'
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
\n1NjI2Q0QwIn0=\
\nuse_zeroconf = False\n'

with open(os.path.join(configDir, "cura.cfg"), "a") as new_file:
    new_file.write(octoVar + qidiVar)

with zipfile.ZipFile(os.path.join(os.getcwd(), "definitions.zip"),"r") as zip_ref:
    zip_ref.extractall(os.path.join(mainDir, "definitions"))

with zipfile.ZipFile(os.path.join(os.getcwd(), "extruders.zip"),"r") as zip_ref:
    zip_ref.extractall(os.path.join(mainDir, "extruders"))

with zipfile.ZipFile(os.path.join(os.getcwd(), "X-Plus_mesh.zip"),"r") as zip_ref:
    zip_ref.extractall(os.path.join(mainDir, "meshes"))

with zipfile.ZipFile(os.path.join(os.getcwd(), "x-plus_quality.zip"),"r") as zip_ref:
    zip_ref.extractall(os.path.join(mainDir, "quality"))

if sys.platform == "linux":
    os.system(f"./appimagetool -v /home/{user}/squashfs-root")
    shutil.move(os.path.join(os.getcwd(), "Cura-x86_64.AppImage"), f"/home/{user}/cura")
    os.system(f"chmod +x ~/cura")
    os.system(f"rm -r {os.path.join(os.getcwd(), '..', 'squashfs-root')}")


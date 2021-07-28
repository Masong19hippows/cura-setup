# cura-setup
This is a quick setup file for Cura

## Instructions

The setup is pretty simple. All you need to do is install cura and open it for the first time. Once you open it, it will prompt you for your credentials. After this, it will ask you to select a printer to add. At this time just select a random printer and add it. Next, you need to instal the plugins from your account. Finaly, it will ask you to quit cura to finish installing plugins.

Now, Follow instructions for your OS.

### Windows

The windows setup is stupidly simple. All you need to do is go to the folder build/exe.win-amd64-3.8 - there will be an exe file called main.exe. Execute this <u>with admin</u> privilages and it will install everything for you. Now, you can go back to cura and enjoy the 3d printer and configs that are now present.

### Linux

The linux install requires that you have python 3.7. The cura appimage needs to be in your home directory and be named "cura". It also needs to have executable rights. After this, just clone the respoitory in the home directory using 

`git clone https://github.com/masong19hippows/cura-setup`

And then cd into the directory and execute the python script <u>without root</u>. 

`python3 main.py`

## All Done! Have Fun

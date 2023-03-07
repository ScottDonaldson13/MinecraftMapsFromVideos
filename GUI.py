import tkinter as tk
from tkinter.filedialog import askdirectory
import subprocess
import os
import shutil

# More functional UI, show users it is doing something when it is working with COLMAP, interactive choice list to scale structure, option to rotate structure.


def save_directory():
    
    directory = askdirectory()
    return directory
   
def startProcess():
    colProcess()

def fix_directory(string):
    return string.replace("\\", "/")



UserInterface = tk.Tk()
UserInterface.configure(bg="#5A5A5A")
UserInterface.title("Maps from Videos")

label1 = tk.Label(UserInterface, text="Welcome to the "'Minecraft Maps from Videos'" program!", font=('Helvetica bold', 14), bg='#5A5A5A', fg="white").place(x=200, y=25)

label2 = tk.Label(UserInterface, text="Press the button below to begin: \n You will be prompted to select a folder where your images from the video are located", font=('Helvetica bold', 12), bg='#5A5A5A', fg="white").place(x=150, y=50)

UserInterface.geometry('900x600')



    
   

    
    
button = tk.Button(UserInterface, text="Press Button to Start", font=('Helvetica bold', 12), height=1, command=startProcess).place(x=150, y=100)







def colProcess():

    workspace= "workspace"
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), workspace)
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    
    os.mkdir(folder_path)
    
    folder_path = fix_directory(folder_path)
    images = save_directory()

    cwd = os.getcwd()
    
    nwd = os.path.join(cwd, "COLMAP-3.7-windows-cuda")
    os.chdir(nwd)
    
    
    
    command = ("colmap automatic_reconstructor --workspace_path " + folder_path + " --image_path " + images)
    subprocess.run(command, shell=True)


    current_dir = os.getcwd()
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    os.chdir(parent_dir)
    main_file = os.path.join(os.getcwd(), "Graphing.py")
    main_file = fix_directory(main_file)
    

    exec(open(main_file).read())





UserInterface.mainloop()



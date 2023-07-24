import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import ttk
import subprocess
import os
import io
import shutil
from Graphing import *


'''

    This code is written by Scott Donaldson (2474880D)
    This code is where the GUI of the program sits that allows the user to interact with the program.
    The other file that accompanies this code is Graphing.py




'''

def gui():

    # Setting global variables to be used throughout the program.
    global plane_horz
    global plane_vert
    
    plane_horz = 0
    plane_vert = 0

    
    


    # Get the current working directory.
    current_dir = os.getcwd()
    
    # Create the window popup, set the background and title it.
    UserInterface = tk.Tk()
    UserInterface.geometry('900x600')
    UserInterface.configure(bg="#5A5A5A")
    UserInterface.title("Maps from Videos")
    


    # Create labels that are used in the UI.
    label1 = tk.Label(UserInterface, text="Welcome to the "'Minecraft Maps from Videos'" program!", font=('Helvetica bold', 14), bg='#5A5A5A', fg="white").place(x=200, y=25)

    label2 = tk.Label(UserInterface, text="Press the button below to begin: \n You will be prompted to select a folder where your images are located", font=('Helvetica bold', 12), bg='#5A5A5A', fg="white").place(x=150, y=50)

    label3 = tk.Label(UserInterface, text="Rotation Buttons:", font=('Helvetica bold', 14), bg='#5A5A5A', fg="white").place(x=180, y=420)
    


    
    # Create a text box that shows what the console is outputting.
    text_box = tk.Text(UserInterface, height=15)
    text_box.place(x=150, y=150)
    
    # Create a tick box to allow the user to overwrite the folder protection check.
    Overwrite = tk.BooleanVar()
    tick_box = tk.Checkbutton(UserInterface, text="Tick this box to overwrite existing structure folder", font=('Helvetica bold', 12), height=1, variable=Overwrite)
    tick_box.place(x=370, y=100)

    # Button to start the process and open the folder search window.
    button = tk.Button(UserInterface, text="Press Button to Start", font=('Helvetica bold', 12), height=1, command=lambda: start_process(text_box, Overwrite))
    button.place(x=150, y=100)

    

    
    # Four buttons to dictate the rotation that the structure is placed.
    button_rotateLeft = tk.Button(UserInterface, text="Left", font=('Helvetica bold', 12), height=1, width=5, command=lambda: change_value("left", text_box))
    button_rotateLeft.place(x=150, y=450)

    button_rotateRight = tk.Button(UserInterface, text="Right", font=('Helvetica bold', 12), height=1, width=5, command=lambda: change_value("right", text_box))
    button_rotateRight.place(x=200, y=450)

    button_rotateUp = tk.Button(UserInterface, text="Up", font=('Helvetica bold', 12), height=1, width=5, command=lambda: change_value("up", text_box))
    button_rotateUp.place(x=250, y=450)

    button_rotateDown = tk.Button(UserInterface, text="Down", font=('Helvetica bold', 12), height=1, width=5, command=lambda: change_value("down", text_box))
    button_rotateDown.place(x=300, y=450)



    # Label and drop-down selection box to allow the user to select the scaling size of the structure.
    size_label_text = tk.Label(UserInterface, text="Select the size scaling of the structure '1-10':", font=('Helvetica bold', 14), bg='#5A5A5A', fg="white").place(x=450, y= 420)
    size_scaling = tk.IntVar(value=1)
    size_label_option= ttk.Combobox(UserInterface, textvariable=size_scaling, font=('Helvetica bold', 12), height=1, width=5, values=list(range(1,11)), state="readonly")
    size_label_option.place(x=450, y=450)



    # Button to send the input to Graphing.py to create the structure.
    button_place_structure = tk.Button(UserInterface, text="Place", font=('Helvetica bold', 12), height=1, width=15, command=lambda: change_structure(plane_horz, plane_vert, size_scaling.get(), "place", current_dir, text_box))
    button_place_structure.place(x=300, y=500)

    # Button to send the input to Grahping.py to remove the structure.
    button_clear_structure = tk.Button(UserInterface, text="Clear", font=('Helvetica bold', 12), height=1, width=15, command=lambda: change_structure(plane_horz, plane_vert, size_scaling.get(), "clear", current_dir, text_box))
    button_clear_structure.place(x=450, y=500)


    UserInterface.mainloop()
    
# This method changes the horz and vert variables to represent the degrees the structure is to be rotated by in each axis. It is referenced by the rotation buttons.
def change_value(orientation=None, text_box=None):
        global plane_horz
        global plane_vert

        if orientation == 'left':
            plane_horz = plane_horz + 45
            if plane_horz >= 360:
                plane_horz = plane_horz - 360

        elif orientation == 'right':
            plane_horz = plane_horz - 45
            if plane_horz < 0:
                plane_horz = plane_horz + 360

        elif orientation == 'up':
            plane_vert = plane_vert + 45
            if plane_vert >= 360:
                plane_vert = plane_vert - 360
        
        elif orientation == 'down':
            plane_vert = plane_vert - 45
            if plane_vert < 0:
                plane_vert = plane_vert + 360
        
        # Print the rotation changes in the console.
        text_box.insert(tk.END, "\nHorizontal Change: {}".format(plane_horz))
        text_box.insert(tk.END, "\nVertical Change: {}".format(plane_vert))
        text_box.insert(tk.END, "\n ------------------- \n")
        text_box.see(tk.END)
        text_box.update()
        
    
# Method to sned the parameters and start Graphing.py.
def change_structure(plane_horz, plane_vert, size_scaling, instruction, current_dir, text_box):
     
    # Finds Graphing.py in the same working fodler.
    main_file = os.path.join(current_dir, "Graphing.py")
    main_file = fix_directory(main_file)
    
    # Runs the file, if found, with the parameters it needs to rotate, scale the size and distinguish whether to place or clear the structure. 
    try:
        text_box.insert(tk.END, "Found file \n")
        text_box.see(tk.END)
        text_box.update()
        
        command = ["python", "-c", "import Graphing; Graphing.start({}, {}, {}, '{}')".format(plane_horz, plane_vert, size_scaling, instruction)]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        
        for line in iter(process.stdout.readline, ""):
            text_box.insert(tk.END, line)
            text_box.see(tk.END)
            text_box.update()
        
        process.wait()

        if process.returncode != 0:
            print("An error occurred while running Graphing.py. Stopping Graphing.py.")
            process.terminate()

    except MinecraftConnectionError as e:
        # connection failed
        print("Failed to connect to Minecraft server.", e.message)
        process.terminate()

    except ConnectionRefusedError:
        print("Failed to launch file.")
         

    

# This method outputs the console output to the text box on the GUi.
def start_process(text_box, Overwrite):
        


    
        # Calls the col_process function
        command = ["python", "-c", "import io; from GUI import col_process; col_process({})".format(Overwrite.get())]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

        for line in iter(process.stdout.readline, ""):
            text_box.insert(tk.END, line)
            text_box.see(tk.END)
            text_box.update()


        process.stdout.close()
        return_code = process.wait()

        if return_code != 0:
            text_box.insert(tk.END, "Process failed with return code {}".format(return_code))

# This method swaps backslashes for forward slashes as some commands and directories break with improper slashes.
def fix_directory(string):
        return string.replace("\\", "/")

# This method runs COLMAP and everything needed by COLMAP.
def col_process(Overwrite=False):
        
        # Looks to where the workspace directory will be created, and if prompted by the user removes the existing one and replaces it with an empty one.
        workspace= "workspace"
        folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), workspace)
        if Overwrite and os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            os.mkdir(folder_path)
        
        # Fixes the directory path.
        folder_path = fix_directory(folder_path)

        # Prompts the user to select a folder that contains images.
        images = askdirectory()
        if images == "":
             print("No image folder was selected")
        else:
             

            cwd = os.getcwd()
            
            nwd = os.path.join(cwd, "COLMAP-3.7-windows-cuda")
            os.chdir(nwd)
            
            
            # Runs COLMAP with the requisites needed. 
            command = ("colmap automatic_reconstructor --workspace_path " + folder_path + " --image_path " + images)
            subprocess.run(command, shell=True)

            print("COLMAP has completed you may now proceed")
        
    

# Method to start the program when used the file is ran.
if __name__ == '__main__':
    gui()






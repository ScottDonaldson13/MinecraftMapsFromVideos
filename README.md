# MinecraftMapsFromVideos
Project repo for my University Project- Minecraft Maps from Videos

Welcome to the Minecraft Maps from Videos Program!
The Official Github repository is at https://github.com/ScottDonaldson13/MinecraftMapsFromVideos

This program allows a user to take a room or building from the real world and place it directly into the game Minecraft.

Make sure to have a clean install of Java and Python.
This can be found at https://www.oracle.com/uk/java/technologies/downloads/#jdk17-windows for Java (Make sure it is Java 17).
And use https://www.python.org/downloads/ for Python.

Next, enter a command prompt at the location where you placed the programs files. (This can be done by entering the folder containing MinecraftMapsFromVideos, clicking on the folder directory
at the top and replacing it with cmd).

From there enter the following command: pip install -r requirements.txt

If any errors occur when doing this please make sure a correct Python environment is installed.

Make sure that the folder downloaded from GitHub isn't placed in a OneDrive active directory, else issues with COLMAP will arise. This can be solved by making sure the drive the folder is stored
on isn't connected to OneDrive.

----

To begin using this program launch the MinecraftMapsFromVideos.bat file found in the downloaded folder from GitHub.

If this is the first time you are using the program or you want to create a new project please make sure to tick the tick box labelled "Tick this box to overwrite exisiting structure folder."
Once that is ticked press "Press button to start" and select the folder that holds the images of the place you want to transfer into Minecraft.

If this isn't the first time you are using the program and you want to continue using the same images used prior leave the box unticked. This can also be used in the event of
accidentally closing the program when COLMAP is creating a render.

Now let COLMAP create the render and once COLMAP is completed a message will appear saying that it is completed.

Next is to launch the game Minecraft and the server that the program will be connected to. 

Make sure that the version of Minecraft you are launching in 1.19.3. You can choose the version of Minecraft by going to "Installation" on the Minecraft.exe Launcher, "New installation" and
changing the selected version to "release 1.19.3".  

Now go into the "server" directory found in the folder downloaded from GitHub and launch "run.bat". When this is run you will be told that the EULA isn't set to true and so it can't be ran.
To fix this, inside the sever directory open eula.txt, and change "eula=false" to "eula=true". You can then run the server application properly.
Wait for this program to be completed. For ease of use it is recommended to OP the accountyou are playing on so you can access creative mode for flight to fully be able 
to see the structure you've placed.

To "OP" yourself go to the cmd created by "run.bat" and type "op [player_name]" where [player_name] is the name of your minecraft account.

Now launch Minecraft, go to "Multiplayer" and press "Add Server". In server address enter "127.0.0.1" and then click "Done". Now connect to the server you've created. It should be joinable
as long as "run.bat" in the "server" folder has been completed. 

Then in-game type "/gamemode creative" in order to be able to fly.

Now position yourself wherever you want and you can place the structure from the program with the "place" button.

If you wish to delete the structure that you have just placed press the "clear" button.

----

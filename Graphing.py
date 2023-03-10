from plyfile import PlyData
import numpy as np
from mcpi.minecraft import Minecraft
import os
import math




'''

    This code is written by Scott Donaldson (2474880D)
    This code is where the main body of the program sits that does all the manipulation of blocks and voxels to place the structure into minecraft.
    The other file that accompanies this code is GUI.py




'''

def start(plane_horz, plane_vert, size_scaling, instruction):

    
    # Creates a variable to store where the workplace file should exist.
    cwd = os.getcwd()
    data_directory = os.path.join(cwd, 'workspace/dense/0/fused.ply')

    # Checks to see if the directory of the file exists
    if os.path.exists(data_directory) == False:
        print("Workplace file can't be found")
        exit()

    # Takes the file from the workplace and adds it to an array using Plyfile module.
    data = PlyData.read(data_directory)

    # Dictionary of block, their colours and their respective ingame ID's.
    block_colour = {
    '#c86646': [5, 4], #acacia plank
    '#969795': [1, 5], #andesite
    '#cabb85': [5, 2], #birch plank
    '#111117': [251, 15], #black concrete
    '#2b1e19': [159, 15], #black terracotta
    '#212d25': [35, 15], #black wool
    '#2f3088': [251, 11], #blue concrete
    '#6aa8fa': [266], #blue ice
    '#4e404b': [159, 11], #blue terracotta
    '#37363f': [35, 11], #blue wool
    '#b5644a': [45], #bricks
    '#633a27': [251, 12], #brown concrete
    '#503729': [159, 12], #brown terracotta
    '#80512d': [35, 12], #brown wool
    '#999ab0': [82], #clay
    '#151515': [173], #charcoal block
    '#9c6f50': [3], #dirt
    '#646464': [4], #cobblestone
    '#0076a6': [251, 9], #cyan concrete
    '#5a5d5d': [159, 9], #cyan terracotta
    '#0094a6': [35, 9], #cyan wool
    '#543a22': [5, 5], #dark oak plank
    '#396b5b': [168, 2], #dark prismarine
    '#38f3e3': [57], #diamond block
    '#f4fca6': [121], #end stone
    '#dce0a2': [206], #end stone brick
    '#ffe059': [41], #gold block
    '#b47c6b': [1, 1], #granite
    '#393c3f': [251, 7], #gray concrete
    '#3f302d': [159, 7], #gray terracota
    '#424b4f': [35, 7], #gray wool
    '#495c2c': [251, 13], #green concrete
    '#4e5532': [159, 13], #green terracota
    '#516a28': [35, 13], #green wool
    '#eaeaea': [42], #iron block
    '#ac7c60' : [5, 3], #jungle wood plank
    '#1b3d8b': [22], #lapis lazuli block
    '#0088c4': [251, 3], #light blue concrete
    '#725168': [159, 3], #light blue terracota
    '#00aaD3': [35, 3], #light blue wool
    '#7d7d74': [251, 8], #light gray concrete
    '#896b62': [159, 8], #light gray terracota
    '#8e8e87': [35, 8], #light gray wool
    '#55a931': [251, 5], #lime concrete
    '#657d3b': [159, 5], #lime terracota
    '#67ba34': [35, 5], #lime wool
    '#ae3197': [251, 2], #magenta concrete
    '#985769': [159, 2], #magenta terracota
    '#C64FB2': [35, 2], #magenta wool
    '#321d21': [112], #nether bricks
    '#6e0b0c': [214], #nether wart block
    '#56001f': [87], #netherrack
    '#aa864f': [5, 1], #oak wood plank
    '#e86121': [251, 1], #orange concrete
    '#a65530': [159, 1], #orange terracota
    '#f36a26': [35, 1], #orange wool
    '#dd658d': [251, 6], #pink concrete
    '#a75052': [159, 6], #pink terracota
    '#fb8baa': [35, 6], #pink wool
    '#838584': [1, 6], #polished andesite
    '#bcbdc0': [1, 4], #polished diorite
    '#a87362': [1, 2], #polished granite
    '#682198': [251, 10], #purple concrete
    '#794756': [159, 12], #brown terracota
    '#7d29a6': [35, 12], #purple wool
    '#e4ddd3': [155], #quartz block
    '#942629': [251, 14], #red concrete
    '#591518': [215], #red nether brick
    '#964136': [159, 14], #red terracota
    '#a42a29': [35, 14], #red wool
    '#806037': [5, 1], #spruce wood plank
    '#7f7f7f': [1], #stone block
    '#9f5d45': [172], #hardened clay block
    '#cdd2d3': [251, 0], #white concrete
    '#d2b4a1': [159, 0], #white terracota
    '#eff1f1': [35, 0], #white wool
    '#f0ae15': [251, 4], #yellow concrete
    '#b78222': [159, 4], #yellow terracota
    '#f9ca2b': [35, 4], #yellow wool
    }



    # Value to make changing iterations easier.
    iteration_value=5

    # Creating an empty array of the size the pointcloud.
    Graph_array = np.zeros((len(data.elements[0].data[0::iteration_value]), 4)).astype(object)
    
    # Assigning the values of the pointcloud into a numpy array and setting it as an array of x, y, z, colour.
    for i in range(len(data.elements[0].data[0::iteration_value])):
        for j in range(3):
           Graph_array[i][j] = data.elements[0].data[0::iteration_value][i][j]
        Graph_array[i][3] = nearest_block_colour('%02x%02x%02x' % (data.elements[0].data[0::iteration_value][i][-3], data.elements[0].data[0::iteration_value][i][-2], data.elements[0].data[0::iteration_value][i][-1]), list(block_colour.keys()))
      

    # Creating a temporary array allowing matrix operation on float values by using them as a double.
    temp_array = np.array(Graph_array[:, :3], dtype=np.double)

    # Rounding the values in the array so they can be used effectively in a voxel.
    voxel_size = 0.1
    voxelized_points = np.round(temp_array[:, :3]* size_scaling / voxel_size) * voxel_size

    
    
    # Setting the values to int so they can be manipulated.
    voxelized_points = np.floor(voxelized_points).astype(int)
   
    
    # Connecting to the local minecraft server in order to place the structure.
    try:
        server = Minecraft.create(address="localhost", port=4711)
        # connection successful
        print("Connected to Minecraft server")
    except ConnectionRefusedError:
        # connection failed
        print("Failed to connect to Minecraft server")


    # Centralising the voxel so it can be cleanly rotated, then rounding it so it can be dealt with as an int.
    centred_voxelized_points = voxelized_points - np.mean(voxelized_points, axis=0)
    rotated_voxelized_points = rotate_voxel(centred_voxelized_points, plane_horz, plane_vert)
    rotated_voxelized_points -= np.min(rotated_voxelized_points, axis=0)
    rotated_voxelized_points = np.round(rotated_voxelized_points).astype(int)





    
    # Getting the player's position to place structure around them.
    player_pos = server.player.getTilePos()
       
    # Calculating distance between player and original block placement.
    x_differential = np.round(np.mean(rotated_voxelized_points[:,0])) - player_pos.x
    y_differential = np.round(np.mean(rotated_voxelized_points[:,1])) - player_pos.y
    z_differential = np.round(np.mean(rotated_voxelized_points[:,2])) - player_pos.z
    

    # If statement to see whether or not the command of place or clear was sent.
    if instruction == "place":
        print("Placing structure")

        # Looping through array of blocks placing each on as their specific block type.
        for i in (range(Graph_array.shape[0])):
            x, y, z = rotated_voxelized_points[i]
            
        

            
            colour = Graph_array[i, 3]
                
            try:
                # Removing the differential from the original coordinate places the structure around the player instead of a random position.
                server.setBlock(x-x_differential, y-y_differential, z-z_differential, block_colour[colour])
               
            except IndexError:
                print(f"IndexError: ({x}, {y}, {z}) is out of bounds")
        print("Structure has been placed") 

        # Saving the position of the player when the structure was placed to a file called "player_pos.txt".
        np.savetxt("workspace/player_pos.txt", [x_differential, y_differential, z_differential])
       

    elif instruction == "clear":
        
        print("Clearing structure")

        # Checks to see if the file containing the original coordinates of the player when the structure was placed exists.
        if os.path.isfile("workspace/player_pos.txt"):

            # Loading the file with the player position and saving the coordinates to differential variables to clear the structure at the blocks where it was placed.
            [x_differential, y_differential, z_differential] = np.loadtxt("workspace/player_pos.txt", unpack=True)

            for j in (range(Graph_array.shape[0])):
                x, y, z = rotated_voxelized_points[j]
                
                try:
                    server.setBlock(x-x_differential, y-y_differential, z-z_differential, [0])
                    

                except IndexError:
                    print(f"IndexError: ({x}, {y}, {z}) is out of bounds")

            # As the blocks have been removed the file is deleted since there is no more need for the players coordinates.
            os.remove("workspace/player_pos.txt")
            print("Structure has been cleared")
        else:
            print("The file for player position does not exist.")
           
        

   


# Method to find the nearest block colour according to the RGB value of the pointcloud point.
def nearest_block_colour(hex_code, block_colours):
    
    red = int(hex_code[0:2], 16)
    green = int(hex_code[2:4], 16)
    blue = int(hex_code[4:6], 16)

    closest_hex = block_colours[0]
    closest_block_difference = (red - int(closest_hex[1:3], 16))**2 + (green - int(closest_hex[3:5], 16))**2 + (blue - int(closest_hex[5:7], 16))**2

    for colour in block_colours[1:]:
        colour_difference = (red - int(colour[1:3], 16))**2 + (green - int(colour[3:5], 16))**2 + (blue - int(colour[5:7], 16))**2
        if colour_difference < closest_block_difference:
            closest_hex = colour
            closest_block_difference = colour_difference
    
    return closest_hex


# Method to rotate the voxel.
def rotate_voxel(array, plane_horz, plane_vert):

    # Takes the degrees sent from the User in the GUI to be turned into radians.
    transformed_horz, transformed_vert = np.radians(plane_horz), np.radians(plane_vert)

    # Each axis is sent to its own method to be rotated as they use different equations.
    rotated_y = rotation_matrix_y(transformed_vert)
    rotated_array = np.dot(array, rotated_y)

    rotated_x = rotation_matrix_x(transformed_horz)
    rotated_array = np.dot(rotated_array, rotated_x)

    rotated_z = rotation_matrix_z(transformed_horz)
    rotated_array = np.dot(rotated_array, rotated_z)

    return rotated_array


# Method to rotate the y axis.
def rotation_matrix_y(radian):
    cos, sin = math.cos(radian), math.sin(radian)
    return np.array([[cos, 0, sin], [0, 1, 0], [-sin, 0, cos]])

# Method to rotate the x axis.
def rotation_matrix_x(radian):
    cos, sin = math.cos(radian), math.sin(radian)
    return np.array([[1, 0, 0], [0, cos, -sin], [0, sin, cos]])

# Method to rotate the z axis.
def rotation_matrix_z(radian):
    cos, sin = math.cos(radian), math.sin(radian)
    return np.array([[cos, 0, sin], [0, 1, 0], [-sin, 0, cos]])

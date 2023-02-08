from plyfile import *
import numpy as np
import matplotlib.pyplot as plt
from mcpi.minecraft import Minecraft





def main():
    data = PlyData.read("P:\\UniWork\\Project\\BowlingClub\\Workplace\\dense\\0\\fused.ply")

    # Dictionary of block, their colours and their respective ingame ID's
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

    #fig = plt.figure()
    #ax = fig.add_subplot(projection='3d')

    # Value to make changing iterations easier
    iteration_value=5

    # Creating an empty array of the size the pointcloud.
    Graph_array = np.zeros((len(data.elements[0].data[0::iteration_value]), 4)).astype(object)
    
    # Assigning the values of the pointcloud into a numpy array and setting it as an array of x, y, z, colour
    for i in range(len(data.elements[0].data[0::iteration_value])):
        for j in range(3):
           Graph_array[i][j] = data.elements[0].data[0::iteration_value][i][j]
        Graph_array[i][3] = nearest_block_colour('%02x%02x%02x' % (data.elements[0].data[0::iteration_value][i][-3], data.elements[0].data[0::iteration_value][i][-2], data.elements[0].data[0::iteration_value][i][-1]), list(block_colour.keys()))
      
    #print(Graph_array[:,3])
    #ax.scatter(Graph_array[:,0], Graph_array[:,1], Graph_array[:,2], color=Graph_array[:,3], alpha=0.5)
    

    #plt.show()
    plt.savefig("render.png")

    # Creating a temporary array allowing matrix operation on float values by using them as a double.
    temp_array = np.array(Graph_array[:, :3], dtype=np.double)

    # Rounding the values in the array so they can be used effectively in a voxel
    voxel_size = 0.1
    voxelized_points = np.round(temp_array[:, :3]*10 / voxel_size) * voxel_size
    
    # Setting the values to int so they can be manipulated
    voxelized_points = np.floor(voxelized_points).astype(int)
    voxel_indices = np.unique(voxelized_points, axis=0)
    
    # Setting the shape of the voxel
    voxel_shape = (int(np.max(voxel_indices[:, 0]) + abs(min(voxel_indices[:, 0]))), int(np.max(voxel_indices[:, 1]) + abs(min(voxel_indices[:, 1]))), int(np.max(voxel_indices[:, 2]) + abs(min(voxel_indices[:, 2]))))
    
    # Creating an object to hold the structure 
    structure = np.zeros(voxel_shape).astype(object)

    # Connecting to the local minecraft server in order to place the structure.
    server = Minecraft.create(address="localhost", port=4711)

    # Loop to tie each x, y, z coordinate to its corrosponding colour and to place it into Minecraft.
    for i in (range(Graph_array.shape[0])):
        x, y, z = voxelized_points[i]
        
        colour = Graph_array[i, 3]
        
        structure[x, y, z] = colour

        server.setBlock(x, y, z, block_colour[colour])

        #server.setBlock(x, y, z, [0])
        
        

    #ax = fig.gca(projection='3d')
    #ax.voxels(structure)
    #plt.show()


# Method to find the nearest block colour according to the RGB value of the pointcloud point
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

if __name__ == '__main__':
    main()


#print(data.elements[0].data[0::100][0], data.elements[0].data[0::100][1], data.elements[0].data[0::100][2])
#print(type(data.elements[0].data[0::10][0][-3]), data.elements[0].data[0::10][0][-2], data.elements[0].data[0::10][0][-1])
#for i in range(len(data.elements[0].data[0::1000])):
#   ax.scatter(data.elements[0].data[0::1000][i][0], data.elements[0].data[0::1000][i][1], 30, '#%02x%02x%02x' % (data.elements[0].data[0::1000][i][-3], data.elements[0].data[0::1000][i][-2], data.elements[0].data[0::1000][i][-1]), alpha=0.2)
    
#ax.scatter(data.elements[0].data[0::100][:][0], data.elements[0].data[0::100][:][1], data.elements[0].data[0::100][:][2], color='#%02x%02x%02x' % (data.elements[0].data[0::100][:][-3], data.elements[0].data[0::100][:][-2], data.elements[0].data[0::100][:][-1]), alpha=0.2)
     

#print(nearest_block_colour("614f24"))

#block_array = np.zeros((100, 100, 50))

# Point transformed/point_in_blocks will be point * factor1 + factor2 (transform the graph)
# Block array of 1/0's/colours to show a point exists
# Key words to google (convert pointcloud to voxel)

#for i in range(len(data.elements[0].data[0::500])):
    #point = data.elements[0].data[0::500][i]  # make it xyz later      
    #[i][3] = '#%02x%02x%02x' % (data.elements[0].data[0::500][i][-3], data.elements[0].data[0::500][i][-2], data.elements[0].data[0::500][i][-1])








#Try doing without the loop
#abs pose mins in recon settings
#3dim numpy array (or 4 for colour) for actual array of blocks, each axis is manually picked size-wise, 4th dimension is whether there is or isnt a block. (Or could be 0 red, 1 green, 2 blue)
# Dont worry about colours for now, just get actual blocks in place.
# https://matplotlib.org/stable/gallery/mplot3d/scatter3d.html 3d scatterplot
# https://matplotlib.org/stable/gallery/mplot3d/voxels.html visualizing blocks 
# Sketchfab models, free to download, if club doesnt work.
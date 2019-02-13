import numpy as np

Map = np.zeros((4,7), dtype=int)
Map[0][1] = 4
Map[1][0] = 4
Map[1][1] = 4
Map[2][1] = 4
Map[2][2] = 8
Map[2][3] = 8
Map[0][2] = 7
Map[0][3] = 7

def find_c_in_c_radius(H, W, D, c):
    """
    returns all of the spots within radius from a given spot on the map
    recieves the height, width of map, max distance for radius scan, and coordinates of given spot
    """
    # H - int
    # W - int
    # D - int
    # c - tuple
    floorH = max(c[0]-D, 0)
    floorW = max(c[1]-D, 0)
    ceilingH = min(c[0]+D+1, H)
    ceilingW = min(c[1]+D+1, W)
    """
    Another way of writing this part:
    floorH = c[0]-D if c[0]-D > 0 else 0
    floorW = c[1]-D if c[0]-D > 0 else 0
    ceilingH = c[0]+D+1 if c[0]+D+1 < H else H
    ceilingW = c[1]+D+1 if c[1]+D+1 < W else W
    """
    coor_list = []
    for y in range(floorH, ceilingH):
        for x in range(floorW, ceilingW):
            if (abs(y-c[0])+abs(x-c[1])) <= D:
                coor_list.append((y,x))
    return list(filter(lambda x: x != c, coor_list))

def find_c_in_building_radius(Map, v, D):
    """
    returns a list of values for occupied spots on the map within radius from given building
    receives the 2d array of our map, the value of a given spot on the map and the max distance of our radius
    """
    # map - matrix
    # c - tuple
    # D - int
    building_c = list(zip(*np.where(Map == v)))
    surrounding_c = []
    map_indexes = []
    for i in building_c:
        surrounding_c = surrounding_c + find_c_in_c_radius(len(Map), len(Map[0]), D, i)
    surrounding_c = [x for x in surrounding_c if x not in building_c]
    irrel_c = list(zip(*np.where(Map == 0)))
    uti_c = list(set(x for x in surrounding_c if x not in irrel_c))
    return uti_c

# c_list = find_c_in_building_radius(Map, 4, 2)
# uti_buildings = {7:(0,5) , 8:(4,6)}

def get_unique_uti(Map, c_list, uti_buildings):
    """
    returns number of unique utility buildings within radius from a given building
    recieves a list of coordinates of occupied spots of utility buildings within radius and a dictionary of utility buildings on whole map
    """
    # v_list - list
    # utibuildings - dict
    diff_uti_types = []
    for i in c_list:
        if Map[i[0]][i[1]] not in diff_uti_types:
            diff_uti_types.append(Map[i[0]][i[1]])
    return len(diff_uti_types)

# print(get_unique_uti(Map, c_list, uti_buildings))

# next step: a function to calculate how much points this r building adds to our score.

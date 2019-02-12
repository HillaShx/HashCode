def find_c_in_radius(H, W, D, c):
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

# next step: check only the coordinates within the radius and not all over the board)

print(find_c_in_radius(4,7,2,(3,6)))

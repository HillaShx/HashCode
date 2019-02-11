def find_c_in_radius(H, W, D, c):
    # H - int
    # W - int
    # D - int
    # c - tuple
    coor_list = []
    for x in range(H):
        for y in range(W):
            if (abs(x-c[0])+abs(y-c[1])) <= D:
                coor_list.append((x,y))
    return list(filter(lambda x: x != c, coor_list))

# next step: check only the coordinates within the radius and not all over the board)

print(find_c_in_radius(4,7,2,(0,3)))

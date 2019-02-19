import numpy as np
def create_mock_grid(dimentions=(5,10)):
    y=dimentions[0]
    x=dimentions[1]
    grid=np.zeros((y,x),dtype="int")
    for y_ in range(1,y-1):
        for x_ in range(1,x-1):
            grid[y_][x_]=1
    print(grid)
    return (grid)

def pizza_solver(grid,tl_coordinates, br_coordinates, L, H,print_to_screen=False):

    """
    gets first and second coordinates
    L: int- the minimum number of 0 and 1 we need on the slice
    H: int- max slice size
    :return:int number_of_slices, list list_of_cuts, int total_surface
    list list_of_cuts (list(1coordinate,2coordinate))
    1coordinate, 2coordinate: tupple (R,C)
    """
    # get coordinates for sub-rectangle to work on
    y1= tl_coordinates[0]
    x1= tl_coordinates[1]
    y2= br_coordinates[0]
    x2= br_coordinates[1]
    # get some data to decide what to do
    surface_size=np.abs((x2-x1)*(y2-y1))
    Tcount=np.sum(grid[y1:y2,x1:x2])
    Mcount=surface_size-Tcount
    if print_to_screen:
        # broadcast
        print("subgrid surface area",surface_size)
        print("grid slice:")
        print(grid[y1:y2,x1:x2])
        print("number of 1 digits",Tcount)
        print("number of 0 digits", Mcount)
    divide_further = False

    number_of_slices = 0
    list_of_cuts = list()
    total_surface = 0
    best_params = (number_of_slices, list_of_cuts, total_surface)
    if Tcount<L or Mcount<=L: #slice is insatisfactory
        return(best_params)
    else: #enough Mushrooms and Tomatoes
        if surface_size>H:
            for row= range(x):
                for col= range(y):
                    best_params_right=resolve_split_pizza_params(pizza_solver(),
                                                                     pizza_solver(),
                                                                     pizza_solver())
                    best_param_left=resolve_split_pizza_params(pizza_solver(),
                                                                     pizza_solver(),
                                                                     pizza_solver())
                    if best_param_left[2]>best_params_right[2]:
                        if best_param_left[2]>best_params[2]:
                            best_params= best_param_left
                    else:
                        if best_param_left[2]>best_params[2]:
                            best_params= best_param_left
            return(best_params)
        else:
            number_of_slices=1
            list_of_cuts.append((tl_coordinates,br_coordinates))
            total_surface=surface_size
            return(number_of_slices, list_of_cuts, total_surface)


    if !devide_further:
        return(number_of_slices, list_of_cuts, total_surface)
    return surface_size

    #    return (number_of_slices, list_of_cuts, total_surface)

pizza_solver(create_mock_grid(),(1,1),(5,10),5,6,print_to_screen=True)

def grid_slices():
    X=10
    Y=5
    grid=np.zeros((Y,X),dtype=int)
    i=0
    for y in range(Y):
        for x in range(X):
            grid[y][x]=i
            i+=1
    print(grid)
    print()
    for i in range(X):
        print(i,grid[2:4,1:i])


    return

#grid_slices()
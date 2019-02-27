import numpy as np
solution=dict()


def create_mock_grid(dimentions=(5,10)):
    y=dimentions[0]
    x=dimentions[1]
    grid=np.zeros((y,x),dtype="int")
    for y_ in range(1,y-1):
        for x_ in range(1,x-1):
            grid[y_][x_]=1
    print(grid)
    return (grid)

def resolve_split_pizza_params(*args):
    # each param has (number_of_slices, list_of_cuts, total_surface)
    number_of_slices= 0
    list_of_cuts=list()
    total_surface=0
    for arg in args:
        number_of_slices+= arg[0]
        list_of_cuts+=arg[1]
        total_surface+= arg[2]
    return((number_of_slices, list_of_cuts, total_surface))

def pizza_solver(grid,tl_coordinates, br_coordinates, L, H ,print_to_screen=True):
    global solution
    if (tl_coordinates,br_coordinates) in solution.keys():
        print("HERE WE SAVE ONE DETOUR")
        return solution[(tl_coordinates,br_coordinates)]
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
    ylim,xlim= grid.shape

    # get some data to decide what to do
    surface_size=np.abs((x2-x1+1)*(y2-y1+1))
    Tcount=np.sum(grid[y1:y2+1,x1:x2+1])
    Mcount=surface_size-Tcount
    if print_to_screen:
        # broadcast
        print("limits of grid",tl_coordinates,(y2,x2))
        print("grid slice:")
        print(grid[y1:y2+1, x1:x2+1])
        print("subgrid surface area",surface_size)
        print("number of 1 digits",Tcount)
        print("number of 0 digits", Mcount)
    divide_further = False

    number_of_slices = 0
    list_of_cuts = list()
    total_surface = 0
    best_params = (number_of_slices, list_of_cuts, total_surface)

    if Tcount<L or Mcount<L: #slice is insatisfactory
        if print_to_screen:
            print ("this slice doesn't have enough tomatoes or mushrooms")
        solution.update({(tl_coordinates, br_coordinates):best_params})
        return(best_params)
    else: #enough Mushrooms and Tomatoes
        if Tcount>=L and Mcount>=L:
            print("this slice satisfies #T>L and #M>L")
        if surface_size>H:
            if print_to_screen:
                print ("surface is big- trying to devide further")
            for row in range(0,x2-x1+1):
                for col in range(0,y2-y1+1):
                    if y1+col+1<ylim:
                        best_params_right=resolve_split_pizza_params(pizza_solver(grid,tl_coordinates, (y1+col,x1+row), L, H),
                                                                     pizza_solver(grid,(y1+col+1,x1), (y2,x1+row), L, H),
                                                                     pizza_solver(grid,(y1,x1+row+1),br_coordinates,L,H))
                    else:
                        print("***Right Short***")
                        if (x1+row+1)<xlim:
                            best_params_right=resolve_split_pizza_params(pizza_solver(grid,tl_coordinates, (y1+col,x1+row), L, H),
                                                                     pizza_solver(grid,(y1,x1+row+1),br_coordinates,L,H))
                    if (x1+row+1)<xlim:
                        best_param_left=resolve_split_pizza_params(pizza_solver(grid,tl_coordinates, (y1+col,x1+row), L, H),
                                                                     pizza_solver(grid,(y1,x1+row+1),(y1+col,x2),L,H),
                                                                     pizza_solver(grid,(y1+col+1,x1),br_coordinates,L,H))
                    else:
                        print("***Left Short***")
                        if (y1 + col + 1) < ylim:
                            best_param_left=best_param_left=resolve_split_pizza_params(pizza_solver(grid,tl_coordinates, (y1+col,x1+row), L, H),
                                                                     pizza_solver(grid,(y1+col+1,x1),br_coordinates,L,H))
                    if best_param_left[2]>best_params_right[2]:
                        if best_param_left[2]>best_params[2]:
                            best_params= best_param_left
                            divide_further=True
                    else:
                        if best_params_right[2]>best_params[2]:
                            best_params= best_params_right
                            divide_further=True
            solution.update({(tl_coordinates,br_coordinates):best_params})
            return(best_params)
        else:
            if print_to_screen:
                print("this slice is potentially IN!")
            number_of_slices=1
            list_of_cuts.append((tl_coordinates,(y2,x2)))
            total_surface=surface_size
            solution.update({(tl_coordinates, br_coordinates): (number_of_slices,list_of_cuts,total_surface)})
            return(number_of_slices,list_of_cuts,total_surface)
    if not(divide_further):
        solution.update({(tl_coordinates, br_coordinates): (number_of_slices, list_of_cuts, total_surface)})
        return(number_of_slices, list_of_cuts, total_surface)
    solution.update({(tl_coordinates, br_coordinates): best_params})
    return best_params

    #    return (number_of_slices, list_of_cuts, total_surface)
def grid_slices(X=4,Y=2,print_to_screen=False):
    grid=np.zeros((Y,X),dtype=int)
    i=0
    for y in range(Y):
        for x in range(X):
            grid[y][x]=i
            i+=1
    if print_to_screen:
        print(grid)
    return grid

def check_list_of_tupple_behaviour():
    A=list((((2,3),(4,5))))
    print(A)
    B=list((A,A))
    print(B)
    C= B + B
    s=list()

    ## this code is taken from the outputter in main
    for cut in C:
        TR_coordinate = cut[0]
        BL_coordinate = cut[1]
        s.append(" ".join([str(i) for i in list([TR_coordinate[0], TR_coordinate[1], BL_coordinate[0], BL_coordinate[1]])]))
    message = '\n'.join(s)
    print(message)
    return

#grid_slices()
R=3
C=3
number_of_slices= 0
list_of_cuts=list()
total_surface=0
best_params= (number_of_slices,list_of_cuts,total_surface)

for x in range (0,R):
    for y in range (0,C):
        coordinate=(y,x)
        solution[coordinate,coordinate]= best_params

print(pizza_solver(create_mock_grid((R,C)),(0,0),(R-1,C-1),1,2,print_to_screen=True))

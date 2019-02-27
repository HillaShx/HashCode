import io
import numpy as np
from pizza_solver import pizza_solver

def initialize_from_input(input_filename): #Hilla
    with open(input_filename) as file:
        parameters = np.fromstring(file.readline(), dtype=int, sep=' ') #[int(x) for x in list(file.readline())[:-1] if x != " "]
        R,C,L,H = parameters[0], parameters[1], parameters[2], parameters[3]
        grid = np.zeros((R,C), dtype=int)
        for i in range(R):
            toppings = [x for x in list(file.readline())[:-1]]
            for j in range(len(toppings)):
                if toppings[j] == "M":
                    grid[i][j] = 1
    return R, C, L, H, grid

# def print_solution_to_file(number_of_slices, list_of_cuts, total_surface,output_filename): #shahar
#     # prints to file
#     return
def print_solution_to_file(number_of_slices, list_of_cuts,output_filename,print_to_screen=False): #shahar
    s=list()
    s.append(str(number_of_slices))
    for cut in list_of_cuts:
        TR_coordinate= cut[0]
        BL_coordinate=cut[1]
        s.append(" ".join([str(i) for i in list([TR_coordinate[0],TR_coordinate[1],BL_coordinate[0],BL_coordinate[1]])]))
    message='\n'.join(s)
    if print_to_screen==True:
        print(message)
    text_file = open("Output.txt", "w")
    text_file.write(message)
    text_file.close()
    # prints to file
    return

def pizza_main(input_filename,output_filename):
    R, C, L, H, grid = initialize_from_input(input_filename)
    number_of_slices, list_of_cuts, total_surface = pizza_solver(grid,(0,0),(R-1,C-1),L,H)
    # outputter(number_of_slices, list_of_cuts, total_surface,output_filename)
    number_of_slices, list_of_cuts, total_surface = pizza_solver((0,0),(R-1,C-1),L,H)
    print_solution_to_file(number_of_slices, list_of_cuts, output_filename)
    return

pizza_main("a_example.in",3)
def check_for_print_solution_to_file():
    cuts=list()
    cuts.append(((0,0),(0,0)))
    cuts.append(((0,1),(2,0)))
    print_solution_to_file(2,cuts, "output.txt", print_to_screen=True)
    return

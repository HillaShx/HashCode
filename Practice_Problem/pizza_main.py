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

def pizza_main(input_filename,output_filename):
    R, C, L, H, grid = initialize_from_input(input_filename)
    number_of_slices, list_of_cuts, total_surface = pizza_solver(grid,(0,0),(R-1,C-1),L,H)
    # outputter(number_of_slices, list_of_cuts, total_surface,output_filename)

pizza_main("a_example.in",3)

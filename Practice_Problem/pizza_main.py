import numpy as np
import pizza_solver

def initialize_from_input(input_filename): #Hilla
    # opens file and reads information
    return(R, C, L, H, grid)

def print_solution_to_file(number_of_slices, list_of_cuts, total_surface,output_filename): #shahar
    # prints to file
    return

def pizza_main(input_filename,output_filename):
    R, C, L, H, grid = initialize_from_input(input_filename)
    number_of_slices, list_of_cuts, total_surface = pizza_solver((0,0),(R-1,C-1),L,H)
    outputter(number_of_slices, list_of_cuts, total_surface,output_filename)

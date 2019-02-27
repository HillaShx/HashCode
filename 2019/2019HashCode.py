import numpy as np
import io
import time

def initializer(input_file):
    # reads parameters from input file and stores it in variables
    with open(input_file) as file:
        variableA, variableB, variableC = file.readline().split()
        for line in file.readlines():
            # do whatever
            pass

    return

def output(solution,output_file):
    # writes the solution onto the output file

    return

def solver(variableA,variableB,variableC):
    # finds the solution
    solution=[]
    return solution

def main(input_file, output_file):
    # runs the script in the correct order of executaion.
    variableA, variableB, variableC= initializer(input_file)
    solution=solver(variableA,variableB,variableC)
    output(solution,output_file)
    return

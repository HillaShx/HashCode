import numpy as np
import io
import time

# CONFLICT!!!!!!!!!!

class classA():
    def __init__(self,var1=0,var2=0):
        self.internal_var1=var1
        self.internal_var2=var2
        return
    def inject_variables(self,var1,var2):
        self.internal_var1=varA
        self.internal_var2=varB
        return
    def __str__(self):
        return "string"
        #return f"{self.plan.CreatePlanPrintout()}"


def initializer(input_file):
    with open(input_file) as file:
        line = file.readline() # read first line
        variableA, variableB, variableC = np.fromstring(line, dtype=int, sep=' ')
        data = file.read() # read all other lines
        data2 = data.split('\n') # use the splitted info from file
        # use data to understand stuff...

        # matrix = np.zeros((hp, wp), dtype=int)
        # for i in range(hp):
        #     #                   print(data2[i+1])
        #     for j, char in enumerate(data2[i + 1]):
        #         matrix[i][j] = char == '#'
        #         #               print(matrix)

        classAinstance=ClassA()
        classBinstance=ClassB()

    return (variableA, variableB, variableC, classAinstance, classBinstance)

def output(solution,output_file,print_to_screen=False):
    s = list()
    # s.append(str(number_of_slices))
    # for cut in list_of_cuts:
    #     TR_coordinate = cut[0]
    #     BL_coordinate = cut[1]
    #     s.append(
    #         " ".join([str(i) for i in list([TR_coordinate[0], TR_coordinate[1], BL_coordinate[0], BL_coordinate[1]])]))
    message = '\n'.join(s)
    if print_to_screen == True:
        print(message)
    text_file = open(output_file, "w")
    text_file.write(message)
    text_file.close()
    # prints to file
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

import numpy as np
import io
import time

class Picture(id,attribute,tags):
    def __init__(self,id=0,attribute=0,tags):
        self.id=id
        self.attribute=""
        self.tags=list()
        return
    def inject_variables(self,attribute, tags):
        self.attribute=attribute
        self.tags=tags
        return
    def add_tag(self,tag):
        self.tags= self.tags.append(tag)
    def __str__(self):
        return " ".join([str(i) for i in tags])
        #return f"{self.plan.CreatePlanPrintout()}"


def initializer(input_file):
    with open(input_file) as file:
        num_of_pics = int(file.readline())
        horiz_pics = []
        vertic_pics = []
        for i in range(num_of_pics):
            properties = file.readline().split()
            if properties[i] == "V":
                
        data = file.read() # read all other lines
        data2 = data.split('\n') # use the splitted info from file
        # use data to understand stuff...

        # matrix = np.zeros((hp, wp), dtype=int)
        # for i in range(hp):
        #     #                   print(data2[i+1])
        #     for j, char in enumerate(data2[i + 1]):
        #         matrix[i][j] = char == '#'
        #         #               print(matrix)

        # classAinstance=ClassA()
        # classBinstance=ClassB()

    # return (variableA, variableB, variableC, classAinstance, classBinstance)

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
    # variableA, variableB, variableC= initializer(input_file)
    # solution=solver(variableA,variableB,variableC)
    output(solution,output_file)
    return

initializer("a_example.txt")

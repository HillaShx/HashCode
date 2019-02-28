import numpy as np
import io
import time

class Picture():
    def __init__(self,id,attribute,tags):
        self.id=id
        self.attribute=attribute
        self.tags=tags
        return
    def inject_variables(self,attribute, tags):
        self.attribute=attribute
        self.tags=tags
        return
    def add_tag(self,tag):
        self.tags= self.tags.append(tag)
    def __repr__(self):
        # return " ".join([str(i) for i in tags])
        return f"Picture({self.id},{self.attribute},{self.tags})"

class slide():
    def __init__(self):
        self.content=list()
        self.tags=list()
    def add_H_pic(self,Hpic):
        self.content.append(Vpic)
        return
    def add_2V_pic(self, Vpic1,Vpic2):
        self.content.append((Vpic1,Vpic2))
        return
    def add_tags(self):
        for i in self.content:
            self.tags.append(i.tags)
        self.tags = list(set(self.tags))
        return self.tags

class slideshow():
    pass


def initializer(input_file):
    with open(input_file) as file:
        num_of_pics = int(file.readline())
        horiz_pics = []
        vertic_pics = []
        tags_dict = dict()
        for i in range(num_of_pics):
            i = i+1
            properties = file.readline().split()
            tags = []
            for t in range(2,int(properties[1])+1):
                tags.append(properties[t])
                if properties[t] not in tags_dict:
                    tags_dict[properties[t]] = [i]
                else:
                    tags_dict[properties[t]].append(i)
            if properties[0] == "V":
                vertic_pics.append(Picture(i,properties[0],tags))
            else:
                horiz_pics.append(Picture(i,properties[0],tags))
    print(tags_dict)



    return (num_of_pics, horiz_pics,vertic_pics)

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

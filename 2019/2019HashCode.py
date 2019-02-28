import numpy as np
import io
import time

class Picture():
    def __init__(self,id,attribute,tags):
        self.id=id
<<<<<<< HEAD
        self.attribute=""
        self.tags=list()
=======
        self.attribute=attribute
        self.tags=tags
        return
>>>>>>> 8eebc9b414bd4785772a3d8b3fa9dda46b409b83
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
    def add_H_pic(self,Vpic):
        self.content.append(Vpic)
        return
    def add_2V_pic(self, Hpic1,Hpic2):
        self.content.append((Hpic1,Hpic2))
        return

class slideshow():
<<<<<<< HEAD
    def __init__(self):
        self.order=list()
    def insert_slide(self,slide):
        self.order.append(slide)
    def __str__(self):
        s=str(length(self.order))
            
=======
    pass

>>>>>>> 8eebc9b414bd4785772a3d8b3fa9dda46b409b83

def initializer(input_file):
    with open(input_file) as file:
        num_of_pics = int(file.readline())
        horiz_pics = []
        vertic_pics = []
        for i in range(num_of_pics):
            properties = file.readline().split()
            tags = []
            for t in range(2,int(properties[1])+1):
                tags.append(properties[t])
<<<<<<< HEAD
            print(tags)

            if properties[0] == "V":
                vertic_pics.append()
=======
            if properties[0] == "V":
                vertic_pics.append(Picture(i,properties[0],tags))
            else:
                horiz_pics.append(Picture(i,properties[0],tags))
        print(horiz_pics, vertic_pics)
>>>>>>> 8eebc9b414bd4785772a3d8b3fa9dda46b409b83

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

<<<<<<< HEAD
     return (numics, Hpictures,Vpictures)
=======
    return (num_of_pics, horiz_pics,vertic_pics)
>>>>>>> 8eebc9b414bd4785772a3d8b3fa9dda46b409b83

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

def solver(num_of_pics, horiz_pics,vertic_pics):
    slideshowInstance=slideshow()
    for pic in horiz_pics:
        slideInstance=slide()
        slideInstance.add_H_pic(pic)
        slideshowInstance.insert_slide(pic)
    # finds the solution
    return slideshowInstance

def main(input_file, output_file):
    # runs the script in the correct order of executaion.
<<<<<<< HEAD
    num_of_pics, horiz_pics,vertic_pics= initializer(input_file)
    solution=solver(num_of_pics, horiz_pics,vertic_pics)
=======
    # variableA, variableB, variableC= initializer(input_file)
    # solution=solver(variableA,variableB,variableC)
>>>>>>> 8eebc9b414bd4785772a3d8b3fa9dda46b409b83
    output(solution,output_file)
    return

initializer("a_example.txt")

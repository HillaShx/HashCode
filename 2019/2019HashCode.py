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
        self.content.append(Hpic)
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
    def __init__(self):
        self.order=list()
    def insert_slide(self,slide):
        self.order.append(slide)
    def __str__(self):
        s=str(len(self.order))+"\n"+ "\n".join([str(i.content[0].id) for i in self.order])
        return s
    def silde_pair_score(self, slide_i,slide_j):
        same=0
        unique_i = 0
        unique_j = 0
        for i in range(len(slide_i.tags)):
            if slide_i.tags[i] in slide_j.tags:
                same+=1
            elif slide_j.tags[i] not in slide_i.tags:
                unique_j+=1
            elif slide_i.tags[i] not in slide_j.tags:
                unique_i+=1
        return min(same,unique_i,unique_j)


def initializer(input_file):
    with open(input_file) as file:
        num_of_pics = int(file.readline())
        horiz_pics = []
        vertic_pics = []
        tags_dict = dict()
        for i in range(num_of_pics):
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
    return (num_of_pics, horiz_pics,vertic_pics, tags_dict)

def output(solution,output_file,print_to_screen=False):
    s = str(solution)
    # s.append(str(number_of_slices))
    # for cut in list_of_cuts:
    #     TR_coordinate = cut[0]
    #     BL_coordinate = cut[1]
    #     s.append(
    #         " ".join([str(i) for i in list([TR_coordinate[0], TR_coordinate[1], BL_coordinate[0], BL_coordinate[1]])]))
    message = ''.join(s)
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
        print("pic id:",pic.id)
        slideInstance=slide()
        slideInstance.add_H_pic(pic)
        slideshowInstance.insert_slide(slideInstance)
    print(slideshowInstance)
    # finds the solution
    return slideshowInstance

def main(input_file, output_file):
    # runs the script in the correct order of executaion.
    num_of_pics, horiz_pics,vertic_pics, tags_dict= initializer(input_file)
    solution=solver(num_of_pics, horiz_pics,vertic_pics)
    output(solution,output_file)
    return

#initializer("a_example.txt")
main("b_lovely_landscapes.txt", "output_file_b.txt")

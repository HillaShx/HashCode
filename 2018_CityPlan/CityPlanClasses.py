import numpy as np
from copy import copy, deepcopy

class Building():
    """
    a BUILDING has an index in the project list, dimentions hp and wp,
    a type R or U, and a matrix to show where it' s occupied
    """
    def __init__(self,i,Btype,hp,wp,attribute):
        self.i=i # index in building list
        self.hp=hp
        self.wp=wp
        self.Btype=Btype # can be R or U
        self.attribute=attribute # can be residence or utility number
        self.matrix=np.zeros((hp,wp),dtype=int)
    def set_matrix(self, matrix):
        self.matrix=matrix
    def get_matrix(self):
        return self.matrix
    def print_attributes(self):
#       print(self.i,self.Btype,self.hp,self.wp,self.attribute,'\n',self.matrix)
        pass

class Plan():
    """
    a PLAN is a list of coordinates in the Terrain where Buildings are set.
    it adds buildings to the list,
    counts what should be known to the output
    and formats it
    """
    def __init__(self):
        self.TotalProjects=0
        self.buildings = list()
        self.coordinates = list ()
    def AddBuildingToPlan(self,building,coordinates):
        self.TotalProjects=self.TotalProjects+1
        self.buildings.append(building.i)
        self.coordinates.append(coordinates)
    def CreatePlanPrintout(self):
        output=list()
        output.append(str(self.TotalProjects))
        for i,ProjectIndex in enumerate(self.buildings):
            output.append("%d %d %d" %(ProjectIndex, self.coordinates[i][0], self.coordinates[i][1]))
        for i in output:
            print (i)
        return output

class Terrain():
    def __init__(self, H=0, W=0):
        self.H=H
        self.W=W
        self.matrix= np.zeros((H,W), dtype=int)
    def set_matrix(self, matrix):
        self.matrix=matrix
    def copy(self):
        t=Terrain()
        t.H=self.H
        t.W=self.W
        t.matrix= deepcopy(self.matrix)
        return t


    def CheckInsert(self,building,coordinate):
        can_fit=0
        hp=building.hp
        wp=building.wp
        H=self.H
        W=self.W
        hc=coordinate[0]
        wc=coordinate[1]
        if (H-hc-hp>=0) and (W-wc-wp>=0):
            #make patch
            t_patch= self.matrix[hc:hc+hp,wc:wc+wp]
    #       print(t_patch)
            # count number of occupied squares in building
            NumOcc= np.count_nonzero(building.matrix)
    #       print(t_patch-building.matrix == -1)
            # count number of open places that are now newly filled in terrain patch
            NumSuccesses= np.count_nonzero(t_patch-building.matrix == -1)
            #compare patch
            if NumOcc==NumSuccesses :
                can_fit=1
            return can_fit
        else:
            return can_fit

    def AddBuildingToTerrain(self, building, coordinates, MapIndex):
        mat1=self.matrix
        mat2=building.matrix
        """
        Add two matrices of different sizes in place, offset by xy coordinates
        Usage:
          - mat1: base matrix
          - mat2: add this matrix to mat1
          - xypos: tuple (x,y) containing coordinates
        """
        y, x = coordinates
        ysize, xsize = mat2.shape
        xmax, ymax = (x + xsize), (y + ysize)
        mat1[y:ymax, x:xmax] += mat2*MapIndex
        self.set_matrix(mat1)



class TerrainIndex:
    def __init__(self):
        self.ResidenceBuildings=dict()
        self.UtilityBuildings=dict()
    def AddBuildingToTerrainIndex(self,Building,MapIndex):
        ProjectIndex=Building.i
        if Building.Btype=='R': #residence building
            self.ResidenceBuildings[MapIndex]=(ProjectIndex,Building.attribute)
#           print(self.ResidenceBuildings)
        else: #utility building
            self.UtilityBuildings[MapIndex]=(ProjectIndex,Building.attribute)

#           print(self.UtilityBuildings)

class Map:
    def __init__(self, terrain):
        self.t=terrain.copy()
        self.ti=TerrainIndex()
        self.plan=Plan()
        self.MapIndex=1 #every building put on the map gets an ordinal!
    def CheckInsert(self,building,coordinates):
        return self.t.CheckInsert(building,coordinates)
    def AddBuildingIntoMap(self,building, coordinates):
        self.ti.AddBuildingToTerrainIndex(building, self.MapIndex)
        self.t.AddBuildingToTerrain(building, coordinates, self.MapIndex)
        self.plan.AddBuildingToPlan(building,coordinates)
        self.MapIndex=self.MapIndex+1
    def __str__(self):
        return f"{self.plan.CreatePlanPrintout()}"

class Solution:
    def __init__(self):
        self.m=self.Map()
        self.score=0


def initialize_from_description(input_file):

    terrain= np.zeros([])
    buildings=[]

    W=1
    H=1
    with open(input_file) as file:
        line = file.readline()
        LineArr=np.fromstring(line, dtype=int, sep=' ')
        W= LineArr[0] # Width of terrain
        H= LineArr[1] # Hight of terrain
        D= LineArr[2] # maximum walking Distance
        B= LineArr[3] # Number of Buildings
#           print(W,H,D,B)

        terrain=Terrain(H,W)

        data = file.read()
        data2 = data.split('\n')
        types=['R','U']
        building_list=list([])
        for buildingIndex in range(B):
            line= data2[0]
            Btype=line[0]
            line=line[2:]
            LineArr=np.fromstring(line, dtype=int, sep=' ')
            hp= LineArr[0] # Width of building
            wp= LineArr[1] # Hight of building
            attribute= LineArr[2] #Attribute of building
            NewBuilding=Building(buildingIndex,Btype,hp,wp,attribute)
            matrix=np.zeros((hp,wp),dtype=int)
            for i in range(hp):
#                   print(data2[i+1])
                for j,char in enumerate(data2[i+1]):
                    matrix[i][j]= char=='#'
#               print(matrix)
            NewBuilding.set_matrix(matrix)
            data2=data2[(1+hp):]
            building_list.append(NewBuilding)
        [B.print_attributes() for B in building_list]


#             building_enumerator=0
#             for i,line in enumerate(data):
#                 if any(s in line for s in types): #the line is a description
#
#                     building_enumerator=building_enumerator+1

        #print(data[1,:])

    return (terrain, building_list, D)
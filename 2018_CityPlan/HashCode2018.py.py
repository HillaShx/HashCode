#!/usr/bin/env python
# coding: utf-8

# In[68]:


import numpy as np
import io
from itertools import groupby
from itertools import permutations 
from copy import copy, deepcopy


# In[70]:


class Building():
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
        print(self.t.matrix)
       
class Solution:
    def __init__(self):
        self.m=self.Map()
        self.score=0        


# In[81]:


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
 
def create_map_with_perm(terrain,buildings, perm):
    MyMap=Map(terrain)
    still_place=1
    while (still_place):
        success_flag=0
        for ProjIndx in perm:
            #print(buildings[ProjIndx].matrix)
            i=0
            while (i<=terrain.H):
                j=0
                while (j<=terrain.W):
#                         print(i,j)
                    if MyMap.CheckInsert(buildings[ProjIndx],(i,j)):
                        MyMap.AddBuildingIntoMap(buildings[ProjIndx],(i,j))
                        success_flag=1
                        i=terrain.H+1
                        j=terrain.W+1
                    j+=1
                i+=1  
        if not(success_flag):
            still_place=0  
    return MyMap        
            

def suggest_solutions (terrain, buildings, MaxDistance):
    MapsList= list()
    permuts = list(permutations(range(0, len(buildings)))) 
    print(permuts)
    for perm in permuts:
        print(perm)
        CurrMap=create_map_with_perm(terrain, buildings, perm)
        MapsList.append(CurrMap)
    return (MapsList)

def scorer(Map,D):
        score=0
        return score
def write_plan_to_file (plan, writeto_file):
    #write plan to file
    return


# In[82]:


def CityPlan (input_file_list, writeto_file_list):
    for i,input_file in enumerate(input_file_list):
        terrain, buildings, MaxDistance = initialize_from_description (input_file)

    ############### map is going to go into solution, but it's here now ##########    
        MyMap=Map(terrain)

        MapsList = suggest_solutions(terrain, buildings, MaxDistance) 
        scores=np.zeros(len(MapsList))
        for j,CurrMap in enumerate(MapsList): 
            scores[j]= scorer(CurrMap,MaxDistance)
        print(scores)
#       write_plan_to_file (plans[np.argmax(scores)], writeto_file_list[0])


# In[83]:


CityPlan(list(['input1.txt']),list(['b.txt']))


# In[21]:


H=2
W=2
for building in range(building):
    i=0
    while (i<=H):
        j=0
        while (j<=W):
            print(i,j)
            #put building in place
            j+=1
        i+=1    


# In[67]:


A=3
B=A
A=4
print(B)


# In[ ]:





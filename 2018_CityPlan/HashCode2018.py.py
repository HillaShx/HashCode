import numpy as np
import io
from itertools import groupby
from itertools import permutations
from scorer import scorer
from PIL import Image
import time
from CityPlanClasses import *

def create_map_with_perm(terrain,buildings, perm):
    MyMap=Map(terrain)
    still_place=1
    while (still_place):
        success_flag=0
        last_seen_on = np.zeros((len(buildings), 2), dtype='int')
        for ProjIndx in perm:
            #print(buildings[ProjIndx].matrix)
            hp=buildings[ProjIndx].hp
            wp=buildings[ProjIndx].wp
            last_coordinate=last_seen_on[ProjIndx]
            i=last_coordinate[0]
            while (i<=terrain.H-hp):
                j=last_coordinate[1]
                while (j<=terrain.W-wp):
#                         print(i,j)
                    if MyMap.CheckInsert(buildings[ProjIndx],(i,j)):
                        MyMap.AddBuildingIntoMap(buildings[ProjIndx],(i,j))
                        success_flag=1
                        last_seen_on[ProjIndx]=(i,j)
                        i=terrain.H+1
                        j=terrain.W+1
                    j+=1
                i+=1
        if not(success_flag):
            still_place=0
    return MyMap


def suggest_solutions (terrain, buildings, MaxDistance):
    MapsList= list()
###############################################################
#
#     permuts = list(permutations(range(0, len(buildings))))
###############################################################
    perm = list(range(0, len(buildings)))
    CurrMap=create_map_with_perm(terrain, buildings, perm)
    # img = Image.fromarray(CurrMap.t.matrix,'I')
    # img.show()
    print(CurrMap.t.matrix)
    MapsList.append(CurrMap)
    # print(permuts)
    # for perm in permuts:
    #     print(perm)
    #     CurrMap=create_map_with_perm(terrain, buildings, perm)
    #     MapsList.append(CurrMap)

    return (MapsList)

# def scorer(Map,D):
#         score=0
#         return score
def write_plan_to_file (plan, writeto_file):
    #write plan to file
    return


def CityPlan (input_file_list, writeto_file_list):
    for i,input_file in enumerate(input_file_list):
        terrain, buildings, MaxDistance = initialize_from_description (input_file)

        MapsList = suggest_solutions(terrain, buildings, MaxDistance)
        scores=np.zeros(len(MapsList))

        for j,CurrMap in enumerate(MapsList):
            scores[j]= scorer(CurrMap,MaxDistance)
            print(CurrMap.__str__())
            # print(CurrMap)
        print(scores)
#       write_plan_to_file (plans[np.argmax(scores)], writeto_file_list[0])

start = time.time()
CityPlan(list(['input1.txt']),list(['b.txt']))
end = time.time()
print("it took",end - start,"seconds")

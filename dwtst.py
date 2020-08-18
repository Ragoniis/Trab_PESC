import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
from get_names_lattes import pesc_professors
import math
from unicodedata import normalize
import json
lattes ={}

with open('Files/test_lattes.json', 'r') as f:
	lattes = json.load(f)

#print(pesc_professors)
def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

infinite = math.inf
def dwt(s1,s2):
    x = np.array(list(map(lambda x: ord(x),list(remover_acentos(s1.lower())))))
    y = np.array(list(map(lambda x: ord(x),list(remover_acentos(s2.lower())))))
    distance,path = fastdtw(x, y, dist=euclidean)
    return distance


for x in lattes.keys():
    edges = lattes[x]["edges"] 
    all_names = pesc_professors[x]
    all_names.append(x)
    for y in edges.keys():
        minv=infinite
        best=''
        for z in all_names:
            value = dwt(z,y);
            if(value<minv):
                minv = value
                best=z
        if(minv<30):
            print("\n",y,best,minv,"\n")

        
        


#distances =[]
#m_d = []
#for x in pesc_professors.keys():
#    qnames = pesc_professors[x]
#    min_d = infinite
#    chosen_name = ''
#    for y in qnames:
#        distance = dwt(x,y)
#        print(x,y,distance)
#        if(distance<min_d):
#            min_d = distance
#            chosen_name =y
#        distances.append(distance)
#    m_d.append({x:[min_d,chosen_name]});
#    print(x,y,min_d)

#s= "teste 1"
#s2 = "asdsada teste 2"
#s = list(map(lambda x: ord(x),list(s)))
#s2 = list(map(lambda x: ord(x),list(s2)))
#x = np.array(s)
#y = np.array(s2)
#distance, path = fastdtw(x, y, dist=euclidean)
#print(m_d)
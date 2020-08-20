import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
from get_names_lattes import pesc_professors
import math
from unicodedata import normalize
from pyjarowinkler import distance
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

def jaroWinkler(s1,s2):
    x= ''.join(list(map(lambda x: x if x!=";" else " ",list(remover_acentos(s1.lower())))))
    y = ''.join(list(map(lambda x: x if x!=";" else " ",list(remover_acentos(s2.lower())))))
    result= distance.get_jaro_distance(x.strip(),y.strip())
    return result

pesc_names ={}
for x in lattes.keys(): 
    all_names = pesc_professors[x]
    all_names.append(x)
    pesc_names[x] = all_names


for x in lattes.keys():
    edges = lattes[x]["edges"] 
    #print("\n\n Professor",x,"\n\n")
    for y in edges.keys():
        #print("\n Comparando ",y,"\n");
        for z in pesc_names.keys():
            maxv=0
            best=''
            for w in pesc_names[z]:
                #print(w,",",end='')
                value = jaroWinkler(y,w);
                if(value>maxv):
                    maxv = value
                    best=w
            #print("\n")
            if(maxv>0.9):
                print("\n",y,"======",best,maxv,"\n")


        
        


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
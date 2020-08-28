import networkx as nx
import matplotlib.pyplot as plt
import json

def cria_grafo(ano, dicionario):
    G = nx.Graph()
    for professor in dicionario:
        G.add_node(professor)
    for colaborador in [*dicionario[professor]]:
        for i in range(len(dicionario[professor][colaborador])):
            if (dicionario[professor][colaborador][i]['year'] == str(ano)):
                G.add_edge(professor, colaborador)
    return G

lista_grafos_1 = []
lista_grafos_2 = []
lista_grafos_3 = []

#abre arquivo
with open('Files/test.json', 'r') as f:
    professores_dict = json.load(f)

with open('Files/jarowinkler.json', 'r') as f:
    jw = json.load(f)


translation = {
    "Abilio Pereira de Lucena Filho":"Abilio Lucena",
    "Adilson Elias Xavier":"Adilson Elias Xavier",
    "Alexandre de Assis Bento Lima":"Alexandre A. B. Lima",
    "Ana Regina Cavalcanti da Rocha":"Ana Regina Cavalcanti da Rocha",
    "Antonio Alberto Fernandes de Oliveira": False,
    "Carlos Eduardo Pedreira":"Carlos Eduardo Pedreira",
    "Celina Miraglia Herrera de Figueiredo":"Celina M. H. de Figueiredo",
    "Claudia Maria Lima Werner":"Cláudia Maria Lima Werner",
    "Claudio Esperança":"Claudio Esperança",
    "Claudio Luis de Amorim":"Claudio Luis de Amorim",
    "Claudio Thomas Bornstein":False,
    "Daniel Ratton Figueiredo":"Daniel R. Figueiredo",
    "Edil Severiano Tavares Fernandes":False,
    "Edmundo Albuquerque de Souza e Silva":"Edmundo de Souza e Silva",
    "Eliseu Monteiro Chaves Filho":False,
    "Ernesto Prado Lopes":False,
    "Felipe Maia Galvão França":"Felipe M. G. França",
    "Flávia Coimbra Delicato":False,
    "Franklin de Lima Marquezino":"Franklin L. Marquezino",
    "Fábio Happ Botler":"Fábio Botler",
    "Geraldo Bonorino Xexéo":"Geraldo Xexéo",
    "Geraldo Zimbrao da Silva":"Geraldo Zimbrão",
    "Gerson Zaverucha":"Gerson Zaverucha",
    "Guilherme Horta Travassos":"Guilherme Horta Travassos",
    "Henrique Luiz Cukierman":"Henrique Luiz Cukierman",
    "Ines de Castro Dutra":False,
    "Jano Moreira de Souza":"Jano Moreira de Souza",
    "Jayme Luiz Szwarcfiter":"Jayme Luiz Szwarcfiter",
    "José Ferreira de Rezende":"José Ferreira de Rezende",
    "Laura Silvia Bahiense da Silva Leite":"Laura Bahiense",
    "Lidia Micaela Segre":False,
    "Luidi Gelabert Simonetti":"Luidi Simonetti",
    "Luis Alfredo Vidal de Carvalho":False,
    "Luis Felipe Magalhães de Moraes":"Luís Felipe M. de Moraes",
    "Marcia Helena Costa Fampa":"Marcia Helena Costa Fampa",
    "Mario Roberto Folhadela Benevides":False,
    "Marta Lima de Queiros Mattoso":"Marta Mattoso",
    "Márcia Rosana Cerioli":"Márcia R. Cerioli",
    "Nelson Maculan Filho":"Nelson Maculan",
    "Paulo Augusto Silva Veloso":"Paulo A. S. Veloso",
    "Paulo Roberto Oliveira":"P. Roberto Oliveira",
    "Paulo Roma Cavalcanti":False,
    "Paulo de Figueiredo Pires":False,
    "Priscila Machado Vieira Lima":"Priscila Machado Vieira Lima",
    "Regina Sandra Burachik":False,
    "Ricardo Farias":"Ricardo C. Farias",
    "Ricardo Guerra Marroquim":"Ricardo Marroquim",
    "Rosa Maria Meri Leão":"Rosa Maria Meri Leão",
    "Rubem P Mondaini":"Rubem P. Mondaini",
    "Severino Collier Coutinho":False,
    "Sheila Regina Murgel Veloso":False,
    "Sulamita Klein": "Sulamita Klein",
    "Susana Scheimberg de Makler": "Susana Scheimberg",
    "Toacy Cavalcante de Oliveira": "Toacy Cavalcante de Oliveira",
    "Valmir Carneiro Barbosa": "Valmir Carneiro Barbosa",
    "Vítor Manuel de Morais Santos Costa":False
}


for p in jw:
    if(translation[p]):
        current = professores_dict[translation[p]]
        for colab in jw[p]:
            #print(colab)
            if(translation[colab]):
                if(translation[colab] in current):
                    current[translation[colab]]+= jw[p][colab]
                else:
                    current[translation[colab]] = jw[p][colab] 
            else:
                print(colab)
                current[colab] = jw[p][colab]
    else:
        #print(p,jw[p])
        temp = {}
        for i in jw[p]:
            if(translation[i]):
                temp[translation[i]] = jw[p][i]
            else:
                temp[i] = jw[p][i]
        print(temp)
        professores_dict[p] = temp

#professores_dict = {**professores_dict,**jw}

#for professor in professores_dict:
    #print(professor)

G1 = nx.Graph()
G2 = nx.Graph()
G3 = nx.Graph()
colors ={
"Antonio Alberto Fernandes de Oliveira" : "b",
"Abilio Lucena" : "#FF7F00",
"Adilson Elias Xavier" : "#FF7F00",
"Alexandre A. B. Lima" : "y",
"Ana Regina Cavalcanti da Rocha" : "m",
"Carlos Eduardo Pedreira" : "k",
"Celina M. H. de Figueiredo" : "r",
"Claudio Esperança" : "y",
"Claudio Thomas Bornstein": "b",
"Claudio Luis de Amorim" : "b",
"Cláudia Maria Lima Werner" : "m",
"Daniel R. Figueiredo" : "#FFC0CB",
"Edil Severiano Tavares Fernandes":"b",
"Edmundo de Souza e Silva" : "k",
"Eliseu Monteiro Chaves Filho": "b",
"Ernesto Prado Lopes": "b",
"Felipe M. G. França" : "b",
"Franklin L. Marquezino" : "r",
"Fábio Botler" : "r",
"Flávia Coimbra Delicato":"b",
"Geraldo Xexéo" : "y",
"Geraldo Zimbrão" : "y",
"Gerson Zaverucha" : "k",
"Guilherme Horta Travassos" : "m",
"Henrique Luiz Cukierman" : "c",
"Ines de Castro Dutra":"b",
"Jano Moreira de Souza" : "y",
"Jayme Luiz Szwarcfiter" : "r",
"José Ferreira de Rezende" : "#FFC0CB",
"Laura Bahiense" : "#FF7F00",
"Lidia Micaela Segre": "b",
"Luidi Simonetti" : "#FF7F00",
"Luís Felipe M. de Moraes" : "#FFC0CB",
"Luis Alfredo Vidal de Carvalho":"b",
"Marcia Helena Costa Fampa" : "#FF7F00",
"Mario Roberto Folhadela Benevides": "b",
"Marta Mattoso" : "y",
"Márcia R. Cerioli" : "r",
"Nelson Maculan" : "#FF7F00",
"P. Roberto Oliveira" : "#FF7F00",
"Paulo A. S. Veloso" : "k",
"Paulo Roma Cavalcanti": "b",
"Paulo de Figueiredo Pires": "b",
"Priscila Machado Vieira Lima" : "#FF7F00",
"Regina Sandra Burachik": "b",
"Ricardo C. Farias" : "g",
"Ricardo Marroquim" : "g",
"Rosa Maria Meri Leão" : "#FFC0CB",
"Rubem P. Mondaini" : "#FF7F00",
"Severino Collier Coutinho":"b",
"Sheila Regina Murgel Veloso": "b",
"Sulamita Klein" : "r",
"Susana Scheimberg" : "#FF7F00",
"Toacy Cavalcante de Oliveira" : "m",
"Valmir Carneiro Barbosa" : "r",
"Vítor Manuel de Morais Santos Costa":"b"
}


with open('Files/test1234.json', 'w',encoding='utf-8') as json_file:
  json.dump(professores_dict, json_file,indent=2,ensure_ascii=False)

ano = 1970
while ano <= 2020:
    G1 = nx.Graph(G1) #cria uma copia do proprio grafo, necessario para que alteracoes ocorram so em um grafo
    G2 = nx.Graph(G2) #Peso 1 para cada artigo
    G3 = nx.Graph(G3) #Proporcional à afinidade
    for professor in professores_dict:
        for colaborador in [*professores_dict[professor]]: #retorna as chaves dentro do dicionario do professor. No caso, os colaboradores
            count = 0
            dinamic_count = 0
            for i in range(len(professores_dict[professor][colaborador])):
                if (professores_dict[professor][colaborador][i]['year'] == str(ano)):
                    G1.add_edge(professor, colaborador)
                #elif(int(professores_dict[professor][colaborador][i]['year']) <= ano):
                    count+=1
                    dinamic_count+= 1/professores_dict[professor][colaborador][i]['number_coauthors']
                    
            if(count>0):
                G2.add_edge(professor, colaborador,weight=count)
                G3.add_edge(professor, colaborador,weight=dinamic_count)
    lista_grafos_1.append(G1)
    lista_grafos_2.append(G2)
    lista_grafos_3.append(G3)
    edges = G2.edges()
    print([G2[u][v]['weight'] for u,v in edges])
    weights = [G2[u][v]['weight']*10 for u,v in edges]
    ano += 1 

print(len(lista_grafos_1))
print("Excentridade Ratton: "+ str(nx.eccentricity(G1, "Daniel R. Figueiredo")))
print("Diametro do grafo: "+str(nx.diameter(G1)))

def closureBecauseNX(G):
    Graph = G
    def filterNoNeighbours(V):
        if (len(list((nx.neighbors(Graph,V)))) >0):
            return True
        else:
            return False
    return filterNoNeighbours

list_number = int(input('Qual grafo ? 1,2,3?'))
if(list_number==1):
    real_graph_list = lista_grafos_1
elif(list_number == 2):
    real_graph_list = lista_grafos_2	
else:
    real_graph_list = lista_grafos_3

i=0
while i<=50:
    print (i+1970)
    cfunction = closureBecauseNX(real_graph_list[i])
    graph_colors = [colors[x] for x in nx.subgraph_view(real_graph_list[i],filter_node=cfunction).nodes()]
    sub_graph= nx.subgraph_view(real_graph_list[i],filter_node=cfunction)
    edges = sub_graph.edges()
    print("Urgente")
    if (list_number>1):
        print("Papi")
        weights = [sub_graph[u][v]['weight'] for u,v in edges]
        nx.draw_spring(nx.subgraph_view(real_graph_list[i],filter_node=cfunction),node_color=graph_colors,with_labels=True,node_size=500,font_size=10,width=weights)
    else:
        print("Papa")
        nx.draw_spring(nx.subgraph_view(real_graph_list[i],filter_node=cfunction),node_color=graph_colors,with_labels=True,node_size=500,font_size=10)
    plt.draw()
    #figManager = plt.get_current_fig_manager()
    #figManager.full_screen_toggle()
    l,r = plt.xlim()
    print(l,r)
    plt.xlim(l-2,r+2)
    plt.show()
    i+=1

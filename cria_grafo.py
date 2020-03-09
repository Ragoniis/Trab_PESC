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

lista_grafos = []
lista_grafos_2 = []
lista_grafos_3 = []

#abre arquivo
with open('Files/test.json', 'r') as f:
	professores_dict = json.load(f)

for professor in professores_dict:
	print(professor)

G1 = nx.Graph()
G2 = nx.Graph()
G3 = nx.Graph()
colors ={
"Abilio Lucena" : "#FF7F00",
"Adilson Elias Xavier" : "#FF7F00",
"Alexandre A. B. Lima" : "y",
"Ana Regina Cavalcanti da Rocha" : "m",
"Carlos Eduardo Pedreira" : "k",
"Celina M. H. de Figueiredo" : "r",
"Claudio Esperança" : "y",
"Claudio Luis de Amorim" : "b",
"Cláudia Maria Lima Werner" : "m",
"Daniel R. Figueiredo" : "#FFC0CB",
"Edmundo de Souza e Silva" : "k",
"Felipe M. G. França" : "b",
"Franklin L. Marquezino" : "r",
"Fábio Botler" : "r",
"Geraldo Xexéo" : "y",
"Geraldo Zimbrão" : "y",
"Gerson Zaverucha" : "k",
"Guilherme Horta Travassos" : "m",
"Henrique Luiz Cukierman" : "c",
"Jano Moreira de Souza" : "y",
"Jayme Luiz Szwarcfiter" : "r",
"José Ferreira de Rezende" : "#FFC0CB",
"Laura Bahiense" : "#FF7F00",
"Luidi Simonetti" : "#FF7F00",
"Luís Felipe M. de Moraes" : "#FFC0CB",
"Marcia Helena Costa Fampa" : "#FF7F00",
"Marta Mattoso" : "y",
"Márcia R. Cerioli" : "r",
"Nelson Maculan" : "#FF7F00",
"P. Roberto Oliveira" : "#FF7F00",
"Paulo A. S. Veloso" : "k",
"Priscila Machado Vieira Lima" : "#FF7F00",
"Ricardo C. Farias" : "g",
"Ricardo Marroquim" : "g",
"Rosa Maria Meri Leão" : "#FFC0CB",
"Rubem P. Mondaini" : "#FF7F00",
"Sulamita Klein" : "r",
"Susana Scheimberg" : "#FF7F00",
"Toacy Cavalcante de Oliveira" : "m",
"Valmir Carneiro Barbosa" : "r"
}




#cria um grafo por ano

ano = 1990
while ano <= 2020:
	G1 = nx.Graph(G1) #cria uma copia do proprio grafo, necessario para que alteracoes ocorram so em um grafo
	G2 = nx.Graph(G2) #Peso 1 para cada artigo
	G3 = nx.Graph(G3) #Proporcional à afinidade
	for professor in professores_dict:
		G1.add_node(professor,color=colors[professor])
		G2.add_node(professor,color=colors[professor])
		G3.add_node(professor,color=colors[professor])
		for colaborador in [*professores_dict[professor]]: #retorna as chaves dentro do dicionario do professor. No caso, os colaboradores
			count = 0
			dinamic_count = 0
			for i in range(len(professores_dict[professor][colaborador])):
				if (professores_dict[professor][colaborador][i]['year'] == str(ano)):
					G1.add_edge(professor, colaborador)
				elif(int(professores_dict[professor][colaborador][i]['year']) <= ano):
					count+=1
					dinamic_count+= 1/professores_dict[professor][colaborador][i]['number_coauthors']
					
			if(count>0):
				G2.add_edge(professor, colaborador,weight=count)
				G3.add_edge(professor, colaborador,weight=dinamic_count)
	lista_grafos.append(G1)
	lista_grafos_2.append(G2)
	lista_grafos_3.append(G3)
	edges = G2.edges()
	print([G2[u][v]['weight'] for u,v in edges])
	weights = [G2[u][v]['weight']*10 for u,v in edges]
	ano += 1 

print (len(lista_grafos))
def closureBecauseNX(G):
	Graph = G
	def filterNoNeighbours(V):
		if (len(list((nx.neighbors(Graph,V)))) >0):
			return True
		else:
			return False
	return filterNoNeighbours

i=0
list_number = int(input('Qual grafo ? 0,1,2?'))
if(list_number==0):
	real_graph_list = lista_grafos
elif(list_number == 1):
	real_graph_list = lista_grafos_2	
else:
	real_graph_list = lista_grafos_3

while i<=30:
	print (i+1990)
	cfunction = closureBecauseNX(real_graph_list[i])
	graph_colors = [colors[x] for x in nx.subgraph_view(real_graph_list[i],filter_node=cfunction).nodes()]
	sub_graph= nx.subgraph_view(real_graph_list[i],filter_node=cfunction)
	edges = sub_graph.edges()
	weights = [sub_graph[u][v]['weight'] for u,v in edges]
	nx.draw_spring(nx.subgraph_view(real_graph_list[i],filter_node=cfunction),node_color=graph_colors,with_labels=True,node_size=500,font_size=10,width=weights)
	plt.draw()
	figManager = plt.get_current_fig_manager()
	figManager.window.showMaximized()
	l,r = plt.xlim()
	print(l,r)
	plt.xlim(l-2,r+2)
	plt.show()
	i+=1
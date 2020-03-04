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

#abre arquivo
with open('Files/test.json', 'r') as f:
	professores_dict = json.load(f)

G1 = nx.Graph()

#cria um grafo por ano

ano = 1990
while ano <= 2020:
	G1 = nx.Graph(G1) #cria uma copia do proprio grafo, necessario para que alteracoes ocorram so em um grafo
	for professor in professores_dict:
		G1.add_node(professor)
		for colaborador in [*professores_dict[professor]]: #retorna as chaves dentro do dicionario do professor. No caso, os colaboradores
			for i in range(len(professores_dict[professor][colaborador])):
				if (professores_dict[professor][colaborador][i]['year'] == str(ano)):
					G1.add_edge(professor, colaborador)
		
	lista_grafos.append(G1)
	ano += 1 

print (len(lista_grafos))

i=0
while i<=30:
	print (i)
	nx.draw(lista_grafos[i], with_labels=True)
	plt.draw()
	plt.show()
	i+=1

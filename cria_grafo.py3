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

with open('test.json', 'r') as f:
	professores_dict = json.load(f)

#G1 = nx.Graph()

ano = 1990
while ano <= 2020:
	'''
	for professor in professores_dict:
		G1.add_node(professor)
		for colaborador in [*professores_dict[professor]]:
			for i in range(len(professores_dict[professor][colaborador])):
				if (professores_dict[professor][colaborador][i]['year'] == str(ano)):
					G1.add_edge(professor, colaborador)
		'''
	lista_grafos.append(cria_grafo(ano, professores_dict))
	ano += 1 

print (lista_grafos)

nx.draw(lista_grafos[20], with_labels=True)
plt.draw()
plt.show()

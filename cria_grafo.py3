import networkx as nx
import matplotlib.pyplot as plt
import json


G=nx.Graph()

with open('test.json', 'r') as f:
	professores_dict = json.load(f)

for professor in professores_dict:
	G.add_node(professor)
	for colaborador in [*professores_dict[professor]]:
		G.add_edge(professor, colaborador)
        

#print ([*professores_dict['Abilio Lucena']])


nx.draw(G, with_labels=True)
plt.draw()
plt.show()

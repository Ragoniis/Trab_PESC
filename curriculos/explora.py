from sets import Set
import xml.etree.ElementTree as ET
tree = ET.parse('danielfigueiredo.xml')

colaboradores = Set([])

root = tree.getroot()
bibliografia = root[1]
for i in range(len(bibliografia)):
	tipo = bibliografia[i] #se eh um artigo, trabalho etc.
	print(tipo.tag)

	for j in range(len(tipo)):
		publicacao = tipo[j] #publicacao individual
		print(publicacao.tag)
		ano = [s for s in publicacao[0].keys() if "ANO" in s] #recupera cada tipo de tag com ano no nome
		if 'LIVRO' not in publicacao.tag:
			print(publicacao[0].attrib[ano[0]])

		for k in range(len(publicacao)):
			if publicacao[k].tag == 'AUTORES':
				colaboradores.add(publicacao[k].attrib['NOME-PARA-CITACAO'])
				print(publicacao[k].attrib['NOME-PARA-CITACAO'])

			elif 'LIVRO' in publicacao[k].tag: #necessario pois livro esta uma indentacao abaixo de artigos e trabalhos
				print(publicacao[k].tag)
				ano = [s for s in publicacao[k][0].keys() if "ANO" in s]
				print(publicacao[k][0].attrib[ano[0]])

				for l in range(len((publicacao[k]))):
					if publicacao[k][l].tag == 'AUTORES':
						colaboradores.add(publicacao[k][l].attrib['NOME-PARA-CITACAO'])
						print(publicacao[k][l].attrib['NOME-PARA-CITACAO'])
print (colaboradores)
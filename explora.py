import xml.etree.ElementTree as ET
import json
import os
#tree = ET.parse('curriculos/danielfigueiredo.xml')

arr = os.listdir('curriculos')
pesc_professors = {}
#Todo Ver se é necessario subtrair 1 do número de coautores
for x in arr:
    tree = ET.parse('curriculos/'+x)
    root = tree.getroot()
    dados = root[0]
    name = dados.attrib["NOME-COMPLETO"]
    qname = dados.attrib["NOME-EM-CITACOES-BIBLIOGRAFICAS"].split(",")
    pesc_professors[name] = {"qnames":qname}
    colaboradores = set([])
    edges = {}
    bibliografia = root[1]
    for i in range(len(bibliografia)):
        tipo = bibliografia[i] #se eh um artigo, trabalho etc.
        #print(tipo.tag)
        for j in range(len(tipo)):
            publicacao = tipo[j] #publicacao individual
            #print(publicacao.tag)
            ano = [s for s in publicacao[0].keys() if "ANO" in s] #recupera cada tipo de tag com ano no nome
            if 'LIVRO' not in publicacao.tag:
                #print(publicacao[0].attrib[ano[0]])
                x=0
            #print(publicacao.tag)
            number_ca = 0
            number_cab= 0
            for k in range(len(publicacao)):
                if publicacao[k].tag == 'AUTORES':
                    number_ca+=1
        
            for k in range(len(publicacao)):
                if publicacao[k].tag == 'DADOS-BASICOS-DO-TRABALHO':
                    edge = {
                        "article" : publicacao[k].attrib["TITULO-DO-TRABALHO"],
                        "ano" : publicacao[k].attrib["ANO-DO-TRABALHO"],
                        "number_coauthors":number_ca
                    }
                    #print(edge)
                elif publicacao[k].tag == 'DADOS-BASICOS-DO-ARTIGO':
                    edge = {
                        "article" : publicacao[k].attrib["TITULO-DO-ARTIGO"],
                        "ano" : publicacao[k].attrib["ANO-DO-ARTIGO"],
                        "number_coauthors":number_ca
                    }
                    #print(edge)
                if publicacao[k].tag == 'AUTORES':
                    colaboradores.add(publicacao[k].attrib['NOME-PARA-CITACAO'])
                    if(publicacao[k].attrib["NOME-COMPLETO-DO-AUTOR"] != name):
                        #print(publicacao[k].attrib["NOME-COMPLETO-DO-AUTOR"])
                        #print(name)
                        if(publicacao[k].attrib["NOME-COMPLETO-DO-AUTOR"] in edges):
                            edges[publicacao[k].attrib["NOME-COMPLETO-DO-AUTOR"]].append(edge)
                        else:
                            edges[publicacao[k].attrib["NOME-COMPLETO-DO-AUTOR"]]=[edge]
                    #print(publicacao[k].attrib['NOME-PARA-CITACAO'])

                elif 'LIVRO' in publicacao[k].tag: #necessario pois livro esta uma indentacao abaixo de artigos e trabalhos
                    ano = [s for s in publicacao[k][0].keys() if "ANO" in s]
                    number_cab= 0
                    for l in range(len((publicacao[k]))):
                        print(publicacao[k][l].tag)
                        if publicacao[k][l].tag == 'AUTORES':
                            number_cab+=1

                    for l in range(len((publicacao[k]))):
                        if publicacao[k][l].tag == 'DADOS-BASICOS-DO-CAPITULO':
                            edge = {
                                "article" : publicacao[k][l].attrib["TITULO-DO-CAPITULO-DO-LIVRO"],
                                "ano" : publicacao[k][l].attrib["ANO"],
                                "number_coauthors" : number_cab
                            }	
                        elif publicacao[k][l].tag == 'AUTORES':
                            colaboradores.add(publicacao[k][l].attrib['NOME-PARA-CITACAO'])
                            if(publicacao[k][l].attrib["NOME-COMPLETO-DO-AUTOR"] != name):
                                if(publicacao[k][l].attrib["NOME-COMPLETO-DO-AUTOR"] in edges):
                                    edges[publicacao[k][l].attrib["NOME-COMPLETO-DO-AUTOR"]].append(edge)
                                else:
                                    edges[publicacao[k][l].attrib["NOME-COMPLETO-DO-AUTOR"]]=[edge]
        pesc_professors[name]["edges"] = edges 

#print (colaboradores)
#print(edges)
with open('Files/test_lattes.json', 'w',encoding='utf-8') as json_file:
  json.dump(pesc_professors, json_file,indent=2,sort_keys=True,ensure_ascii=False)
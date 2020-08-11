import xml.etree.ElementTree as ET
import os
import json
arr = os.listdir('curriculos')
print(arr)
pesc_professors = {}

for x in arr:
    tree = ET.parse('curriculos/'+x)
    root = tree.getroot()
    dados = root[0]
    name = dados.attrib["NOME-COMPLETO"]
    qname = dados.attrib["NOME-EM-CITACOES-BIBLIOGRAFICAS"].split(",")
    pesc_professor = {name:qname}
    pesc_professors[name] = qname
    print(pesc_professor)

print(pesc_professors)

with open('Files/professors.json', 'w',encoding='utf-8') as json_file:
  json.dump(pesc_professors, json_file,indent=2,sort_keys=True,ensure_ascii=False)
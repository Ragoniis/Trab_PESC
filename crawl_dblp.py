import requests
from lxml import etree
from lxml import html
import pprint
import json
#return the HTML page for a given URL
def crawl(url):
  tree = ""
  # Retrying the main retry until it works (this is only viable because we are not interested on simulating a DDOS on the website, we are only getting a few pages)
  while True:
    print('Executing Request for ' + url)
    http_response = requests.get(url)

    # Checking Response Status Code (200 Means OK)
    # If we have an OK response, we can break and continue
    if http_response.status_code == 200:
      tree = html.fromstring(http_response.content)
      break

  return tree

#receives an HTML page and gets all possible names that the researcher associated with the page might have
def get_names (tree, url, researcher_main_name, researchers_names,graph):
  main_name                   = tree.xpath('.//span[contains(@class, \'name primary\')]/text()')[0] #filter HTML getting only the node we are interested on
  researcher_main_name[url]   = main_name
  researcher_names[main_name] = main_name

  other_names = tree.xpath('.//span[contains(@class, \'name secondary\')]/text()')
  graph[main_name] = {}
  for n in other_names:
    researcher_names[n] = main_name

#make the relations between each PESC's author
def get_coauthors(tree, researcher_name, researchers,graph):
  coauthors = {}
  article_type = tree.xpath('.//li[contains(@class, \'entry\')]')[0].get('class')
  nodes = tree.xpath('.//ul[contains(@class, \'publ-list\')]/li')
  #//span[contains(@itemprop,\'author\')]//span/text()') #get all authors from all papers
  for node in nodes:
    if(node.text):
      #print(node.text)
      year = node.text
      continue
    authors = node.xpath('.//span[contains(@itemprop,\'author\')]//span/text()')
    title = node.xpath('.//span[contains(@class,\'title\')]/text()')
    type_of_publication = node.get('class')
    real_type_of_publication = node.xpath('./div/img')[0].get('title')
    element = {}
    if(real_type_of_publication not in ["Books and Theses","Journal Articles","Conference and Workshop Papers"]):
    	continue
    for author in authors:  
      if (author not in researchers):
        #this researcher it not from PESC
        continue
      author_normalized_name = researchers[author] #normalize name, since each professor's name might be written differently
      if (author_normalized_name == researcher_name):
        continue
      if (author_normalized_name not in coauthors):
        coauthors[author_normalized_name] = 0
        graph[researcher_name][author_normalized_name] = []
      coauthors[author_normalized_name] += 1
      element["year"]= year
      element["title"] = title
      element["type_of_publication"]= type_of_publication
      element["real_type_of_publication"] = real_type_of_publication
      element["number_coauthors"] = len(authors);
      graph[researcher_name][author_normalized_name].append(element)
  return coauthors
  
#read file containing urls
def read_file (file_path):
  d = []
  with open(file_path) as file:
    for line in file:
      d.append(line.replace("\n",""))
  return d

urls_file_path  = "Files/dblp_urls.txt"
urls            = read_file(urls_file_path)

write_file      = open("Files/dblp_relations_count.txt", "w")

html_trees           = {}
researcher_names     = {}
researcher_main_name = {}
graph = {}

for url in urls:
  tree = crawl(url)
  html_trees[url] = tree
  get_names(tree, url, researcher_main_name, researcher_names,graph)

for url in urls:
  coauthors = get_coauthors(html_trees[url], researcher_main_name[url], researcher_names,graph)
  for c in coauthors:
    write_file.write(researcher_main_name[url] + "-" + c + ":" + str(coauthors[c]) + "\n")
with open('Files/test.json', 'w',encoding='utf-8') as json_file:
  json.dump(graph, json_file,indent=2,sort_keys=True,ensure_ascii=False)
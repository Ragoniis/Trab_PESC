import json
with open('Files/jarowinkler.json', 'r') as f:
    jw = json.load(f)


def main(dic):
    publications = {}
    for i in dic.keys():
        for j in dic[i].keys():
            collaborations = dic[i][j]
            for p in collaborations:
                title = p["title"][0].replace('"','')
                if(title in publications):
                    arr = publications[title]["authors"]
                    if(i not in arr ):
                        arr.append(i)
                    if(j not in arr):
                        arr.append(j)
                else:
                    publications[title] = {
                        "id" : title,
                        "date" : p["year"],
                        "authors": [i,j]
                    }
    return publications

result = main(jw)
arr = {"publications": list(result.values())}

with open('Files/new_json.json', 'w',encoding='utf-8') as json_file:
  json.dump(arr, json_file,indent=2,sort_keys=True,ensure_ascii=False)
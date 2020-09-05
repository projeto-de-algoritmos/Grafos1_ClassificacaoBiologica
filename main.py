import json
import pandas as pd
from grafo import *


def readDB():
    pd.read_csv("export_gisd.csv").to_json("bd.json")

    with open('bd.json') as json_file:
        data_set = json.load(json_file)

    return data_set


def makeAdjacencyList():

    data_set = readDB()

    # Modelando os dados
    data = {}
    cont = 0
    name_id = {}
    title = ()
    for (key, x) in data_set.items():

        title = list(key.split(";"))
        title = tuple(title[:6])
        for y in x.values():
            item = y.replace("\"", "").split(";")
            for group in enumerate(title):
                data[cont] = {'name': item[group[0]], 'group': group[0]}
                if not item[group[0]] in name_id:
                    name_id[item[group[0]]] = {
                        'id': cont}  # enumerando cada nó
                    cont += 1
        with open('name_id.json', 'w') as json_file:
            json.dump(name_id, json_file)
        with open('id_name.json', 'w') as json_file:
            json.dump(data, json_file)

    reinos = ("Animalia", "Monera", "Plantae", "Fungi", "Protista")

    listaDeAdjacencia = {}

    # Linkando os reinos ao nó raiz

    for x in reinos:
        if not listaDeAdjacencia.get(0):
            listaDeAdjacencia[0] = []
        listaDeAdjacencia[0].append(name_id[x]["id"])

    # Montando a lista de adjacencia
    for (key, x) in data_set.items():

        for y in x.values():

            item = y.replace("\"", "").split(";")

            for key in enumerate(title):
                id_nome = id_vizinho = 0
                # Criando aresta da especie para a familia
                if key[0] == 0:
                    id_nome = name_id.get(item[key[0]])['id']
                    id_vizinho = name_id.get(item[5])['id']
                # Criando aresta para os outros nos de forma decrescente
                elif(key[0]+1 < 6):
                    id_nome = name_id.get(item[key[0]+1])['id']
                    id_vizinho = name_id.get(item[key[0]])['id']
                else:
                    continue
                # verificando se o no ja está na lista de adjacencia
                if not listaDeAdjacencia.get(id_vizinho):
                    listaDeAdjacencia[id_vizinho] = []
                # verificando se a aresta ja foi colocada
                if not id_nome in listaDeAdjacencia[id_vizinho]:
                    listaDeAdjacencia[id_vizinho].append(id_nome)
        i = input().lower().capitalize()
        path = find_path(listaDeAdjacencia, 0, name_id[i]["id"])
        for x in path:
            if x != 0:
                print(data[x]["name"])
        return (listaDeAdjacencia)


if __name__ == "__main__":
    makeAdjacencyList()

import json
import pandas as pd
from grafo import *
# from main import *
# Ler 'banco de dados' e pre formata para uso


def read_db():
    data_set = pd.read_csv("export_gisd.csv", sep=";")
    data_set = data_set.iloc[:, 0:6].to_dict()
    return data_set

# retorna id ou nome da lista


def get_id_name(id=None, name=None):
    data = enumerate_data()
    if id:
        return data[id]
    if name:
        return list(data.values()).index(name)

# Enumera cada nome da taxonomia


def enumerate_data():
    data_set = read_db()
    cont = 1
    data_enumareted = {}
    for x in range(len(data_set['Species'])):
        for groups in ('Species', 'Family', 'Order', 'Class', 'Phylum', 'Kingdom'):
            data_enumareted[cont] = data_set[groups][x]
            cont += 1

    with open('bd.json', 'w') as json_file:
        json.dump(data_enumareted, json_file)

    return data_enumareted


def make_adjacent_list():
    adjacency_list = {}
    groups = {0: 'Species', 1: 'Family', 2: 'Order',
              3: 'Class', 4: 'Phylum', 5: 'Kingdom'}
    data = read_db()
    for row_in_data in range(len(data['Species'])):
        for (key, name) in groups.items():
            # Adicionando Reinos à raiz
            # if not (get_id_name(data['Kindgom'][row_in_data] in adjacency_list.get(0))):
            #     adjacency_list[0].append(get_id_name(name=data['Kindgom'][row_in_data]))

            if(key < len(groups)-1):
                # Pegando id dos nós
                id_nome = get_id_name(name=data[name][row_in_data])
                id_vizinho = get_id_name(name=data[groups[key+1]][row_in_data])
                # verificando se o no ja está na lista de adjacencia
                if not adjacency_list.get(id_vizinho):
                    adjacency_list[id_vizinho] = []
                # verificando se a aresta ja foi colocada
                if not id_nome in adjacency_list[id_vizinho]:
                    adjacency_list[id_vizinho].append(id_nome)

    with open('listaAjacencia.json', 'w') as json_file:
        json.dump(adjacency_list, json_file)

    return adjacency_list


if __name__ == "__main__":
    with open('listaAjacencia.json', 'r') as json_file:
        adjacency_list = json.load(json_file)

    a= find_path(adjacency_list, 77, get_id_name(name="Suncus murinus"))
    for x in a:
        print(get_id_name(id=x))
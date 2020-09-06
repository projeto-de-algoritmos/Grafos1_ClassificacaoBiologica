import json
import pandas as pd
import os
# from main import *
# Ler 'banco de dados' e pre formata para uso


def read_db():
    data_set = pd.read_csv("export_gisd.csv", sep=";")
    data_set = data_set.iloc[:, 0:6].to_dict()
    return data_set

data_enumareted = {}

def enumerate_data():
    global data_enumareted
    data_set = read_db()
    cont = 1
    for x in range(len(data_set['Species'])):
        for groups in ('Species', 'Family', 'Order', 'Class', 'Phylum', 'Kingdom'):
            if (data_set[groups][x] not in list(data_enumareted.values())):
                data_enumareted[cont] = data_set[groups][x]
                cont += 1

    with open('bd.json', 'w') as json_file:
        json.dump(data_enumareted, json_file)

    return data_enumareted

data_enumareted = enumerate_data()

# retorna id ou nome da lista
def get_id_name(id=None, name=None):
    global data_enumareted
    data = data_enumareted
    if id:
        return data[id]
    if name:
        return list(data.values()).index(name)+1

def read_adjacent_list():
    if not os.path.exists('data.json'):
        make_adjacent_list()
    with open('listaAjacencia.json', 'r') as json_file:
        adjacency_list = json.load(json_file)
    return (adjacency_list)

# Enumera cada nome da taxonomia
def make_adjacent_list():
    enumerate_data()
    adjacency_list = {}
    groups = {0: 'Species', 1: 'Family', 2: 'Order',
              3: 'Class', 4: 'Phylum', 5: 'Kingdom'}

    data = read_db()

    for row_in_data in range(len(data['Species'])):
        for (key, name) in groups.items():

            # Adicionando Reinos à raiz
            if not adjacency_list.get(0):
                adjacency_list[0] = []
            if not (get_id_name(name=data['Kingdom'][row_in_data]) in adjacency_list.get(0)):
                adjacency_list[0].append(get_id_name(
                    name=data['Kingdom'][row_in_data]))

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

    a = find_path(adjacency_list, 77, get_id_name(name="Suncus murinus"))
    for x in a:
        print(get_id_name(id=x))


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.get(str(start)):
        return None
    for node in graph.get(str(start)):
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


def search():
    adjacency_list = read_adjacent_list()
    i = input("please type what you want to search for:\n").lower().capitalize()
    j = get_id_name(name=i)
    path = find_path(adjacency_list, 0, j)
    if (path == None):
        print("\n\n\n-----------------------------\n Taxonomia nao encontrada\n-----------------------------\n\n\n")
    else:
        for x in path:
            if x != 0:
                print(get_id_name(id=x))


def Menu_de_cadastro():
    while 1:
        print('''Do you want to register by:\n
[1] Phylum
[2] Class
[3] Order
[4] Family
[5] species\n''')

        op = input("Please enter the number of the option you want to select:")

        if op == "1":
            os.system('clear')
            help = input("Enter the Kingdom to which this Phylum belongs:")
            # funçao de busca recebendo o nó Busca_cadastro(help)
            pass

        elif op == "2":
            os.system('clear')
            help = input("Enter the Philo that this Class belongs to:")
            # funçao de busca recebendo o nó Busca_cadastro(help)
            pass

        elif op == "3":
            os.system('clear')
            help = input("Enter the Class to which this Order belongs:")
            # funçao de busca recebendo o nó Busca_cadastro(help)
            pass

        elif op == "4":
            os.system('clear')
            help = input("Enter the Order to which this Family belongs:")
            # funçao de busca recebendo o nó Busca_cadastro(help)
            pass

        elif op == "5":
            os.system('clear')
            help = input("Enter the Family to which this species belongs:")
            # funçao de busca recebendo o nó Busca_cadastro(help)
            pass

        else:
            os.system('clear')
            print("\n\n\n---------------Please enter a valid option---------------\n\n\n")


def Menuinicial():
    os.system('clear')
    while 1:
        print('''Home menu:\n
[1] Search
[2] register\n ''')

        op = input("Please enter the number of the option you want to select:")

        if op == "1":
            os.system('clear')
            search()
            pass

        elif op == "2":
            os.system('clear')
            Menu_de_cadastro()
            pass

        else:
            os.system('clear')
            print("\n\n\n---------------Please enter a valid option---------------\n\n\n")

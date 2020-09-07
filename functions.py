import json
import pandas as pd
import os
# from main import *

# Ler 'banco de dados' e pre formata para uso
columns = ['species', 'genus', 'family',
           'order', 'class', 'phylum', 'kingdom']


def read_db():
    df = pd.read_csv("bd.csv", sep=";")
    df = df.dropna()
    df = df.reindex(
        columns=['species', 'genus', 'family', 'order', 'class', 'phylum', 'kingdom'])
    return df.to_dict()

# Salva no arquivo csv a nova especie


def write_db(taxonomic=[]):
    columns = ['species', 'genus', 'family',
               'order', 'class', 'phylum', 'kingdom']
    df = pd.read_csv("bd.csv", sep=";")
    df = df.loc[:, df.columns.isin(columns)]

    print("Registrando...")

    if len(taxonomic) == 7:
        insert = pd.DataFrame([taxonomic], columns=columns)
        df = df.append(insert, ignore_index=True)
        df.to_csv("bd.csv", sep=";", index=False, header=True)

    return df


data_enumareted = {}

# Enumera cada nome da taxonomia


def enumerate_data():
    global data_enumareted
    data_set = read_db()
    cont = 1
    for x in range(len(data_set['species'])):
        for groups in ('species', 'genus', 'family', 'order', 'class', 'phylum', 'kingdom'):
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
        if not id in list(data.keys()):
            return -1
        return data[id]
    if name:
        if not name in list(data.values()):
            return -1
        return list(data.values()).index(name)+1

# ler a lista de adjacencia do arquivo json caso ela nao exista


def read_adjacent_list():
    if not os.path.exists('listaAjacencia.json'):
        make_adjacent_list()
    with open('listaAjacencia.json', 'r') as json_file:
        adjacency_list = json.load(json_file)
    return (adjacency_list)


# Constroi a lisa de adjacencia
def make_adjacent_list():
    global data_enumareted
    data_enumareted = enumerate_data()
    adjacency_list = {}
    groups = {0: 'species', 1: 'genus', 2: 'family', 3: 'order',
              4: 'class', 5: 'phylum', 6: 'kingdom'}

    data = read_db()

    for row_in_data in range(len(data['species'])):
        species = []

        for name in groups.values():
            species.append(data[name][row_in_data])

        adjacency_list = insert_in_adjacent_list(adjacency_list, species)

    with open('listaAjacencia.json', 'w') as json_file:
        json.dump(adjacency_list, json_file)
    return adjacency_list


def insert_in_adjacent_list(adjacency_list, species):
    index = 1
    for x in species:
        if index < len(species):
            id_no = get_id_name(name=x)
            id_neighbor = get_id_name(name=species[index])
            index += 1
            if not adjacency_list.get(id_neighbor):
                adjacency_list[id_neighbor] = []
            # verificando se a aresta ja foi colocada
            if not id_no in adjacency_list[id_neighbor]:
                adjacency_list[id_neighbor].append(id_no)
        elif index == len(species):
            # Adicionando Reinos à raiz
            if not adjacency_list.get(0):
                adjacency_list[0] = []
            if not (get_id_name(name=species[-1]) in adjacency_list.get(0)):
                adjacency_list[0].append(get_id_name(
                    name=species[-1]))

    return adjacency_list


# Busca profunda para buscar o caminho


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.get(str(start)):
        return None
    for node in graph.get(str(start)):
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None

# retorna o caminho do no


def search(id):
    adjacency_list = read_adjacent_list()
    path = find_path(adjacency_list, 0, id)

    return path

# Mostrar a taxonomia da especie na tela


def show_result(path):
    groups = {7: 'Species', 6: 'Genus', 5: 'Family', 4: 'Order',
              3: 'Class', 2: 'Phylum', 1: 'Kingdom'}
    if (path == None):
        print("\n\n\n-----------------------------\n Taxonomic not found\n-----------------------------\n\n\n")
    else:
        for x in path:
            if x != 0:
                print(f'{groups[path.index(x)]}: {get_id_name(id=x)}')

# Menu de cadastro


def Menu_de_cadastro():
    register = []
    register.append(
        input('Enter the species you wish to register:').lower().capitalize())
    exist = search(get_id_name(name=register[-1]))
    if exist:
        print("This species already exist!")
        show_result(exist)
    else:
        register.append(
            input('Enter the Genus to which the species belongs:').lower().capitalize())
        exist = search(get_id_name(name=register[-1]))
        if exist:
            # cadastrar especie linkando na familia
            register_from_this(register, exist)
            print("Saved successful")
        else:
            register.append(
                input('Enter the family to which the genus belongs:').lower().capitalize())
            exist = search(get_id_name(name=register[-1]))
            if exist:
                # cadastrar especie linkando na familia
                register_from_this(register, exist)
                print("Saved successful")
            else:
                register.append(
                    input('Enter the Order to which this Family belongs:').lower().capitalize())
                exist = search(get_id_name(name=register[-1]))
                if exist:
                    # cadastrar familia linkando na ordem
                    register_from_this(register, exist)
                    print("Saved successful")
                else:
                    register.append(
                        input('Enter the Class to which this Order belongs:').lower().capitalize())
                    exist = search(get_id_name(name=register[-1]))
                    if exist:
                        # cadastrar ordem linkando na classe
                        register_from_this(register, exist)
                        print("Saved successful")
                    else:
                        register.append(
                            input('Enter the Philo that this Class belongs:').lower().capitalize())
                        exist = search(get_id_name(name=register[-1]))
                        if exist:
                            register_from_this(register, exist)
                            # cadastrar classe linkando no filo
                            print("Saved successful")
                        else:
                            register.append(
                                input('Enter the Kingdom to which this Phylum belongs:').lower().capitalize())
                            exist = search(get_id_name(name=register[-1]))
                            if exist:
                                # cadastrar filo linkando no Reino
                                register_from_this(register, exist)
                                print("Saved successful")
                            else:
                                print(register)


# Registra a especie a partir do ultimo nó em comum existente
def register_from_this(register, rest):
    rest.pop()
    while rest:
        if get_id_name(id=rest[-1]):
            register.append(get_id_name(id=rest.pop()))
        else:
            rest.pop()
    write_db(register)
    enumerate_data()
    adjacency_list = read_adjacent_list()
    adjacency_list = insert_in_adjacent_list(adjacency_list, register)

    with open('listaAjacencia.json', 'w') as json_file:
        json.dump(adjacency_list, json_file)
    return adjacency_list

# Menu inicial


def home_menu():
    os.system('clear')
    print('''Home menu:\n[1] Search\n[2] Register\n[0] Exit ''')

    op = input("Please enter the number of the option you want to select:")

    if op == "1":
        os.system('clear')
        i = input(
            "please type the species you want to search:\n").lower().capitalize()
        result = search(get_id_name(name=i))
        show_result(result)
        input("Press ENTER to return to the home menu")
        home_menu()

    elif op == "2":
        os.system('clear')
        Menu_de_cadastro()
        input("Press ENTER to return to the home menu")
        home_menu()
    elif op == "0":
        os.system("clear")
        exit()
    else:
        print("\n\n\n---------------Please enter a valid option---------------\n\n\n")
        home_menu()

import json
import pandas as pd


def main():
    #Abrindo a base de dados
    pd.read_csv("export_gisd.csv").to_json("bd.json")

    with open('bd.json') as json_file:
        data = json.load(json_file)

    #Montando a lista de adjacencia
    listaDeAdjacencia = {}

    for (key, x) in data.items():
        # Separando o Titulo da base de dados
        title = tuple(key.split(";")) 
        for (index, y) in enumerate(title):

            if(index != 0 and index < len(title)-2):

                for  y in x.items():
                    item = y.split(";")
                    name = y.split(";")[index]
                
                    if not listaDeAdjacencia.get(name):
                        listaDeAdjacencia[name] = []

                    if not item[index+1] in listaDeAdjacencia[name]:
                
                        if index+1 == 6:
                            listaDeAdjacencia[name].append(item[0])
                        else:
                            listaDeAdjacencia[name].append(item[index+1])

        print(listaDeAdjacencia)
        # Salvando lista de adjacência
        with open('listaAdjacência.json', 'w') as json_file:
            json.dump(listaDeAdjacencia, json_file)


if __name__ == "__main__":
    main()

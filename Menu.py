#coding: utf-8
import os
def main():
    Menuinicial()


def Busca_pesquisa():
    op = input("Por favor,Digite oque oque deseja buscar:")

def Menu_de_cadastro():
    while 1:
        print('''Deseja cadastrar por:\n
[1] Filo
[2] Classe
[3] Ordem
[4] Familia 
[5] espécie\n''')

        op = input("Por favor,Digite o numero da opcao que dejesa selecionar:")
        
        if op == "1":
            os.system('clear')
            ajuda = input("Digite o Reino aqual esse Filo pertence:")
            #funçao de busca recebendo o nó Busca_cadastro(ajuda)
            pass
                
        elif op == "2":
            os.system('clear')
            ajuda = input("Digite o Filo aqual esse Classe pertence:") 
            #funçao de busca recebendo o nó Busca_cadastro(ajuda)       
            pass  

        elif op == "3":
            os.system('clear')
            ajuda = input("Digite o Classe aqual esse Ordem pertence:") 
            #funçao de busca recebendo o nó Busca_cadastro(ajuda)        
            pass 

        elif op == "4":
            os.system('clear') 
            ajuda = input("Digite o Ordem aqual esse Familia pertence:")  
            #funçao de busca recebendo o nó Busca_cadastro(ajuda)               
            pass 

        elif op == "5":
            os.system('clear') 
            ajuda = input("Digite o Familia aqual essa espécie pertence:")   
            #funçao de busca recebendo o nó Busca_cadastro(ajuda)                 
            pass 
                    
        else:
            os.system('clear') 
            print("\n\n\n---------------Por favor digite uma opção valida---------------\n\n\n")

def Menuinicial():
    os.system('clear') 
    
    while 1:
        print('''Menu inicial:\n
[1] Pesquisar 
[2] cadastrar\n ''')

        op = input("Por favor,Digite o numero da opcao que dejesa selecionar:")
    
        if op == "1":
            os.system('clear')
            Busca_pesquisa()
            pass
                
        elif op == "2":
            os.system('clear')         
            Menu_de_cadastro()
            pass  
                    
        else:
            os.system('clear') 
            print("\n\n\n---------------Por favor digite uma opção valida---------------\n\n\n")
                
                

main()
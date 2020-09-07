
Classificação biológica

**Número da Lista**: 1<br>
**Conteúdo da Disciplina**: Grafos 1 <br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 18/0103580  |  Jonathan Jorge Barbosa Oliveira |
| 18/0100726 | Filipe Campos Guimarães

## Sobre 
O trabalho trata da classificação taxonômica também conhecida como a forma de identificar e classificar os seres vivos.
  
Foi utilizado um banco de dados preexistente com cerca de 1 milhos de especies com suas 7 classificações (Reino, Filo, Classe, Ordem, Família, Gênero, Espécie).

O Banco de dados foi convertido de arquivo "csv" para uma lista de adjacência e a partir desta temos a "estrutura do grafo". 

Podemos exemplificar esse pensamento da seguinte forma: (Espécie: Homo sapiens, Gênero: Homo, Família: Hominidae,Ordem: Primates, Classe: Mammalia, Filo: Chordata, Reino: Animalia) teremos cada classificação como um nó sendo subordinada ao nó que esta na camada acima dele. 

Dessa forma, podemos saber quais nós estão ligados e fazer buscas para identificar classificações preexistentes ou executar novos cadastros.

## Screenshots

###### Menu inicial
![Alt text](/media/image1.jpeg?raw=true "Menu inicial")
###### Aba de busca
![Alt text](/media/image2.jpeg?raw=true "Aba de busca")
###### Registro de espécie existente"
![Alt text](/media/image3.jpeg?raw=true "Registro de espécie existente") 
###### Registro de nova espécie
![Alt text](/media/image4.jpeg?raw=true "Registro de nova espécie")

## Instalação 
**Linguagem**: Python
### Linux

#### Pelo terminal
- Para clonar o repositório:
> $ git clone https://github.com/projeto-de-algoritmos/Grafos1_ClassificacaoBiologica

- Acesse a pasta do projeto:
``` $ cd Grafos1_ClassificacaoBiologica/```
- Instale as dependências:
``` $ pip3 install -r requirements.txt ```

- (Opcional)
   
   Antes de executar o ``` $ pip3 install -r requirements.txt ``` abra uma virtualenv com o comando 
   ``` $ virtualenv . ``` execute a virtualenv com o comando ``` $ source bin/activate ``` e em seguida instale as depedências com o comando
   ``` $ pip3 install -r requirements.txt ```
  
## Uso 
Execute o programa com o comando 
``` $ python3 main.py ```
siga as intruções do termial

## Outros 






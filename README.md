# Tutorial Neo4j

Tutorial para entender a ferramenta chamada Neo4j, um banco de dados que utiliza grafos para otimizar bancos SQL e NOSQL ou aproveitar estes dados para fazer análises em tempo real dos mesmos.

## Como saber se você precisa do Neo4j

A vantagem de utilizar um banco de dados com grafos é que seus dados estarão organizados de forma totalemente diferente do que em uma forma relacional convencional ou não relacional.

Neo4j é uma ferramenta muito poderosa utilizada por diversas empresas que possuem uma grande massa de dados. Dessa forma elas manipulam seu dados em forma de um modelo de grafos que possuem relações em que as bases SQL e NOSQL não conseguiriam observar.  

## SQL

No caso de um banco relacional, temos por exemplo o seguinte diagrama: 
![](relational.png)
Ao observar as tabelas, é necessário saber quais tabelas são de relacionamento e qual o fluxo dos dados caso alguém deseje fazer uma pesquisa. Neste caso utiliza-se o JOIN para juntar tabelas e conseguir fazer buscas. Entretanto, quando os dados começam a ficar muito grandes normalmente é preciso realizar muitos joins, o que além de deixar as queries longas, praticamente só quem está trabalhando nelas possui o conhecimento do modelo. 

## Grafos

Já no Neo4j, o diagrama ficaria mais ou menos da seguinte forma:
![](dbgraph.png)
Agora com os grafos , mesmo para um número gigantesco deles o comportamento do banco de dados será mais eficaz do que o banco relacional, pois a velocidade de deslocamento dos grafos é muito maior do que realizar dezenas de joins. 
Além de simplificar o modelo relacional, o modelo de grafos ainda é considerado ACID que garante a atomicidade, consistência, isolamento, durabilidade, dos dados em condições de transação.  Fazendo com que dados sensíveis sejam passíveis de serem armazenados no Neo4j. 

## Neo4J – Guia de instalação Windows 

#### Primeiro Passo:

    Instalar Neo4j Community edition

    Utilizar a versão Community Server! Não será possível com outra versão.
    

OBS: Colocar de preferência em ~\ 

### Segundo passo: 

    Ajustar as variáveis de ambiente 

**Criar no path** 
```bash
%NEO4J_HOME% = ~\neo4j-community-3.5.12\bin
```
### Rodar em qualquer prompt: neo4j console


### Terceiro passo: 

    -> Acessar o console pelo browser 

    -> Rodar o console em qualquer promt: neo4j console 

    -> Como ele está habilitado na porta 7474 do localhost, acessar: 
        http:// http://localhost:7474/browser/ 
    -> No dashboard o usuário e senha que deverão ser colocados, por padrão são:

    username: neo4j  
    senha: neo4j 
     

**Depois da primeira conexão, ainda no dash, aparecerá a opção de alterar a senha: coloque sua nova senha.** 

### Quarto passo: 

    -> Testar um script em python usando neo4jbolt na porta 7687 

    -> Rode o arquivo neo4j_example.py. Lembre-se de alterar a senha que foi criada no passo anterior. 


## Mac OSx





# Referências

  Os exemplos de tipos de dados relacionais e grafos
https://www.youtube.com/watch?v=NO3C-CWykkY 

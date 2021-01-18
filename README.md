
<p align="center">
  <img style="float: right;" src="assets/holocron.png" alt="Holocron logo"/>
</p>

# Holocron

Extração de referências em bases de dados à partir de termo de busca

Um vocabulário foi definido para facilitar a comunição e pode ser encontrado [aqui](vocabulario.md).

## Instalação

Clone o repositório disponível no github utilizando o comando:

`git clone https://github.com/cassiobotaro/holocron.git`

Dentro da pasta Holocron, crie o seu ambiente virtual de trabalho:

`python -m venv .venv`

Use o gerenciador de bibliotecas pip para instalar a biblioteca scrapy:

`python -m pip install scrapy`

Caso você tenha problemas no Windows, será necessário instalar o Visual Studio CPP Build Tools – Desmarcar todas as opções e deixar marcada apenas a opção “Ferramentas de Build do C++”

## Como executar?

O Holocron é executado com os comandos:

 `scrapy crawl "buscador.periodicos.capes"`
 
 `scrapy crawl sciencedirect`

TODO: termo de busca nas aranhas deve ser dinâmico

```


                                                    +--------+         +------------+
                                               +--->+base de |         |artigos     +------+
                                               |    |dados A +-------->+exportado   |      |
     +------------+      +--------------+      |    +--------+         +------------+      v
     | Termo de   +----->+autenticação  |      |    +--------+         +------------+  +---------+
     | busca      |      |(opcional)    +---------->+base de +-------->+artigos     +->+Mendeley |
     +------------+      +--------------+      |    |dados B |         |exportados  |  |         |
                                               |    +--------+         +------------+  +---------+
                                               |    +--------+         +------------+       ^
                                               +--->+base de +-------->+artigos     |       |
                                                    |dados C |         |exportados  +-------+
                                                    +--------+         +------------+




```


**rascunhos**
- recebe termo de busca como entrada (inicialmente focaremos em palavras chaves)
- pode receber autenticação para utilização de base de dados não livres
- busca revistas de acordo com área de conhecimento
- faz paginação de artigos(com base em entrada do usuário) em formato exporatável para mendeley

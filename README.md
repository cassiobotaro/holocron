
<p align="center">
  <img style="float: right;" src="assets/holocron.png" alt="Holocron logo"/>
</p>

# Holocron

Extração de referências em bases de dados à partir de termo de busca

Um vocabulário foi definido para facilitar a comunicação e pode ser encontrado [aqui](vocabulario.md).

## Instalação

Clone o repositório disponível no Github utilizando o comando:

`git clone https://github.com/cassiobotaro/holocron.git`

Dentro da pasta Holocron, crie o seu ambiente virtual de trabalho:

`python -m venv .venv`

Em seguida, ative seu ambiente virtual:
`.venv\Scripts\activate.bat` (ou `.venv/bin/activate` no Linux)

Use o gerenciador de bibliotecas pip para instalar a biblioteca `Scrapy`:

`python -m pip install scrapy`

Caso você tenha problemas no Windows, será necessário instalar o Visual Studio CPP Build Tools – Desmarcar todas as opções e deixar marcada apenas a opção “Ferramentas de Build do C++”

Para fazer buscas na base Science Direct, será necessária a utilização do `scrapy-splash` e um servidor rodando o serviço `splash`.

A instalação pode ser feita através do comando `python -m pip install scrapy-splash` e para ter o servidor splash rodando, podemos utilizar o [docker](https://docs.docker.com/get-docker/) e o comando `docker run -p 8050:8050 -d scrapinghub/splash`.

## Como executar?

O Holocron é executado com os comandos:

 `scrapy crawl "buscador.periodicos.capes"`

 `scrapy crawl sciencedirect -a query="water AND leaks"`

 `scrapy crawl scielo -a query="water AND leaks"`

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

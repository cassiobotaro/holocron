# :package: Holocron
TODO: descrição do software


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

Um vocabulário foi definido para facilitar a comunição e pode ser encontrado [aqui](vocabulario.md).

**rascunhos**
- recebe termo de busca como entrada (inicialmente focaremos em palavras chaves)
- pode receber autenticação para utilização de base de dados não livres
- busca revistas de acordo com área de conhecimento
- faz paginação de artigos(com base em entrada do usuário) em formato exporatável para mendeley

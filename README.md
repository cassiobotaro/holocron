# :package: Holocron
TODO: descrição do software


```
                      +--------+         +------------+
                 +--->+revista |         |artigos     +------+
                 |    |A       +-------->+exportado   |      |
                 |    +--------+         +------------+      v
+------------+   |    +--------+         +------------+  +---+-----+
| Termo de   +------->+revista +-------->+artigos     +->+Mendeley |
| busca      |   |    |B       |         |exportados  |  |         |
+------------+   |    +--------+         +------------+  +----+----+
                 |    +--------+         +------------+       ^
                 +--->+revista +-------->+artigos     |       |
                      |C       |         |exportados  +-------+
                      +--------+         +------------+
```                   
**rascunhos**
- recebe termo de busca como entrada (inicialmente focaremos em palavras chaves)
- pode receber autenticação para utilização de base de dados não livres
- busca revistas de acordo com área de conhecimento
- faz paginação de artigos(com base em entrada do usuário) em formato exporatável para mendeley

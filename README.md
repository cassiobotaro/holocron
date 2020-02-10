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
- recebe palavras chaves como entrada
- pode receber autenticaçao para utilização de base de dados não livres
- busca revistas de acordo com área de conhecimento
- faz paginação de artigos(com base em entrada do usuário) em formato exporatável para mendeley

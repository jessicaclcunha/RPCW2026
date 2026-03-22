# TPC6 • Biblioteca Temporal — Aplicação Web com Flask e SPARQL
 
**Data:** 18/03/2026
 
### Autor
**ID:** PG60267
 
**Nome:** Jéssica Cristina Lima da Cunha
 
<img src="../imgs/autor.jpg" width="150">
 
## Resumo
 
Este trabalho consistiu na implementação da rota em falta(`/linhas`) de uma aplicação web Flask para consulta de uma ontologia, a Biblioteca Temporal. A aplicação comunica com um repositório GraphDB via SPARQL.
 
Foi implementada a seguinte rota:
 
* **Linhas Temporais (`/linhas`):** Query SPARQL com `SELECT` e `FILTER`/`BIND` para recuperar, por cada linha temporal, o seu tipo (`LinhaOriginal` ou `LinhaAlternativa`) e os livros que nela existem (ID, título e tipo). Os `FILTER` são aplicados antes dos `BIND` para evitar conflitos de variáveis. O agrupamento é feito em Python: um dicionário por linha temporal acumula os livros, e cada livro acumula os seus tipos numa lista (suportando livros com múltiplos tipos). O resultado é passado ao template `linhas.html`, que apresenta as linhas em abas clicáveis (uma aba por linha temporal), com os tipos de livro mostrados como badges coloridos.
 
## Resultados
 
**[app.py](./app.py)**
>*Aplicação Flask com a rota `/linhas` implementada.*
 
---
 
**[templates/linhas.html](./templates/linhas.html)**
>*Template para a lista de linhas temporais.*
 
---
 
**[templates/layout.html](./templates/layout.html)**
>*Template base atualizado com o link de navegação para a página de Linhas Temporais.*
 
---
 
*Trabalho realizado no âmbito da UC de Representação e Processamento de Conhecimento na Web (RPCW) 2025/2026*

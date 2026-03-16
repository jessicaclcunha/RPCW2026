# TPC • Biblioteca Temporal — Aplicação Web com Flask e SPARQL
 
**Data:** 13/03/2026
 
### Autor
**ID:** PG60267
 
**Nome:** Jéssica Cristina Lima da Cunha
 
<img src="../imgs/autor.jpg" width="150">
 
## Resumo
 
Este trabalho consistiu na implementação das rotas em falta de uma aplicação web Flask para consulta de uma ontologia, a Biblioteca Temporal. A aplicação comunica com um repositório GraphDB via SPARQL.
 
Foram implementadas as seguintes rotas:
 
* **Detalhe do Livro (`/livro/<id>`):** Query SPARQL com `SELECT DISTINCT` e múltiplos `OPTIONAL` para recuperar o título, tipo, autor, país, linhas temporais e eventos referidos pelo livro. O URI do livro é construído dinamicamente a partir do `id_livro` recebido na rota e filtrado com `FILTER(STR(?livro) = "...")`. As linhas temporais são agrupadas num dicionário por ID para evitar duplicações resultantes do produto cartesiano do SPARQL, e o tipo de linha é extraído com `split("#")[-1]`. Os eventos são acumulados num set `eventos_vistos` para garantir unicidade. O resultado é passado ao template `livro.html`.
 
* **Eventos Temporais (`/eventos`):** Query SPARQL com `GROUP_CONCAT` para agregar, numa única linha por evento, os IDs e títulos dos livros que o referenciam, separados por `;`. No Python, faz-se `split(";")` em cada campo e `zip()` para ligar os IDs aos respetivos títulos, formando uma lista de tuplos `(id, titulo)` passada ao template `eventos.html`, onde cada livro aparece como um link clicável.
 
## Resultados
 
**[app.py](./app.py)**
>*Aplicação Flask com as rotas `/livro/<id>` e `/eventos` implementadas.*
 
---
 
**[mquery.py](./mquery.py)**
>*Módulo auxiliar que encapsula a comunicação com o GraphDB via SPARQLWrapper, executando queries SPARQL e devolvendo os resultados em formato JSON.*
 
---
 
**[bib_temp.ttl](./bib_temp.ttl)**
>*Ontologia OWL/Turtle da Biblioteca Temporal, com instâncias de livros, autores, linhas temporais e eventos históricos e futuros.*
 
---
 
**[templates/lista.html](./templates/lista.html)**
>*Template para o catálogo de livros, com tabela de títulos, tipos, autores e países.*
 
---
 
**[templates/livro.html](./templates/livro.html)**
>*Template para o detalhe de um livro, com tabela de metadados e lista de eventos referidos.*
 
---
 
**[templates/eventos.html](./templates/eventos.html)**
>*Template para a listagem de eventos temporais, com os livros que os referenciam como tags clicáveis.*
 
---
 
**[templates/layout.html](./templates/layout.html)**
>*Template base com barra de navegação e rodapé, estendido pelos restantes templates.*
 
---
 
*Trabalho realizado no âmbito da UC de Representação e Processamento de Conhecimento na Web (RPCW) 2025/2026*

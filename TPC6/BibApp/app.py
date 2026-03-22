from flask import Flask, render_template, request, redirect, url_for
from mquery import exec_query
from datetime import datetime

app = Flask(__name__)

data_hora_local = datetime.now()
data_iso = data_hora_local.strftime("%Y-%m-%dT%H:%M:%S")

@app.route('/')
def index():
    q = """
        PREFIX : <http://example.org/biblioteca-temporal#>


        select ?livroID ?titulo ?tipoID ?nomeAutor ?pais where{
            ?livro a ?tipoLivro .
            FILTER(?tipoLivro in (:LivroHistorico, :LivroFiccional, :LivroParadoxal))
            OPTIONAL{ ?livro :titulo ?titulo .}
            ?livro :escritoPor ?autor .
            ?autor :nome ?nomeAutor ;
                    :paisOrigem ?pais .
            BIND(STRAFTER(STR(?livro), "#") AS ?livroID)
            BIND(STRAFTER(STR(?tipoLivro), "#") AS ?tipoID)
        } 
        order by ?titulo
    """
    
    res = exec_query(q)
    
    livros = []
    
    for l in res["results"]["bindings"]:
        livro = {
            "id": l["livroID"]["value"],
            "tipo": l["tipoID"]["value"],
            "autor": l["nomeAutor"]["value"],
            "pais": l["pais"]["value"]
        }
        
        if "titulo" in l:
            livro["titulo"] = l["titulo"]["value"]
            
        livros.append(livro)
    
    return render_template('lista.html', livros = livros)

@app.route('/livro/<id_livro>')
def rota_detalhe(id_livro):
    # Informação do livro (id, titulo, tipo, autor, pais, linha temporal*, eventos referidos pelo livro(id, nome, descrição))
    uri = f"http://example.org/biblioteca-temporal#{id_livro}"
    query = f"""
        PREFIX : <http://example.org/biblioteca-temporal#>
 
        SELECT DISTINCT ?titulo ?tipoID ?nomeAutor ?pais ?linhaID ?tipoLinha ?eventoID ?designacao ?descricao
        WHERE {{
            ?livro a ?tipoLivro .
            FILTER(STR(?livro) = "{uri}")
            OPTIONAL {{ ?livro :titulo ?titulo . }}
            ?livro :escritoPor ?autor .
            ?autor :nome ?nomeAutor ;
                   :paisOrigem ?pais .
            OPTIONAL {{
                ?livro :existeEm ?linha .
                BIND(STRAFTER(STR(?linha), "#") AS ?linhaID)
                OPTIONAL {{
                    ?linha a ?tipoLinha .
                    FILTER(?tipoLinha IN (:LinhaOriginal, :LinhaAlternativa))
                }}
            }}
            OPTIONAL {{
                ?livro :refereEvento ?evento .
                BIND(STRAFTER(STR(?evento), "#") AS ?eventoID)
                OPTIONAL {{ ?evento :designacao ?designacao . }}
                OPTIONAL {{ ?evento :descricao ?descricao . }}
            }}
            FILTER(?tipoLivro IN (:LivroHistorico, :LivroFiccional, :LivroParadoxal))
            BIND(STRAFTER(STR(?tipoLivro), "#") AS ?tipoID)
        }}
    """
    res = exec_query(query)
 
    if not res or not res["results"]["bindings"]:
        return "Livro não encontrado", 404
 
    l = res["results"]["bindings"][0]
    livro = {
        "id": id_livro,
        "titulo": l["titulo"]["value"] if "titulo" in l else id_livro,
        "tipo": l["tipoID"]["value"],
        "autor": l["nomeAutor"]["value"],
        "pais": l["pais"]["value"],
        "linhas": [],
        "eventos": []
    }
 
    linhas_dict = {}
    eventos_vistos = set()
    for row in res["results"]["bindings"]:
        if "linhaID" in row:
            lid = row["linhaID"]["value"]
            if lid not in linhas_dict:
                linhas_dict[lid] = {
                    "id": lid,
                    "tipo": None
                }
            if "tipoLinha" in row:
                linhas_dict[lid]["tipo"] = row["tipoLinha"]["value"].split("#")[-1]
 
        if "eventoID" in row and row["eventoID"]["value"] not in eventos_vistos:
            eventos_vistos.add(row["eventoID"]["value"])
            livro["eventos"].append({
                "id": row["eventoID"]["value"],
                "designacao": row["designacao"]["value"] if "designacao" in row else None,
                "descricao": row["descricao"]["value"] if "descricao" in row else None
            })
 
    livro["linhas"] = list(linhas_dict.values())
    return render_template('livro.html', livro=livro)



@app.route('/eventos')
def rota_eventos():
    # Tabela com id designação, descrição, lista de livros que referem o evento (id, título)
    # DICA: usar GROUP_CONCAT para obter a lista de livros numa única string e depois fazer split() no frontend
    query = """
        PREFIX : <http://example.org/biblioteca-temporal#>
 
        SELECT ?eventoID ?designacao ?descricao
               (GROUP_CONCAT(STRAFTER(STR(?livro), "#") ; SEPARATOR=";") AS ?livrosIDs)
               (GROUP_CONCAT(?titulo ; SEPARATOR=";") AS ?livrosTitulos)
        WHERE {
            ?livro :refereEvento ?evento .
            ?livro :titulo ?titulo .
            OPTIONAL { ?evento :designacao ?designacao . }
            OPTIONAL { ?evento :descricao ?descricao . }
            BIND(STRAFTER(STR(?evento), "#") AS ?eventoID)
        }
        GROUP BY ?eventoID ?designacao ?descricao
        ORDER BY ?designacao
    """
    
    res = exec_query(query)
    eventos = []
    for e in res["results"]["bindings"]:
        designacao = e["designacao"]["value"] if "designacao" in e else ""
        descricao  = e["descricao"]["value"]  if "descricao"  in e else ""
        livros_ids    = e["livrosIDs"]["value"].split(";")     if "livrosIDs"      in e else []
        livros_titulos = e["livrosTitulos"]["value"].split(";") if "livrosTitulos" in e else []

        evento = {
            "id":         e["eventoID"]["value"],
            "designacao": designacao,
            "descricao":  descricao,
            "livros":     list(zip(livros_ids, livros_titulos))
        }
        eventos.append(evento)

    return render_template('eventos.html', eventos=eventos)


@app.route('/linhas')
def rota_linhas():
    #TODO:
    # - Tipo da linha temporal
    # - Livros que nela existem(id, título(link), tipoLivro)
    query = """
        PREFIX : <http://example.org/biblioteca-temporal#>
 
        SELECT ?linhaID ?tipoLinha ?livroID ?titulo ?tipoLivro
        WHERE {
            ?livro a ?tipoLivroURI ;
                   :existeEm ?linha ;
                   :titulo ?titulo .
            ?linha a ?tipoLinhaURI .
            FILTER(?tipoLivroURI IN (:LivroHistorico, :LivroFiccional, :LivroParadoxal))
            FILTER(?tipoLinhaURI IN (:LinhaOriginal, :LinhaAlternativa))
            BIND(STRAFTER(STR(?linha),       "#") AS ?linhaID)
            BIND(STRAFTER(STR(?livro),       "#") AS ?livroID)
            BIND(STRAFTER(STR(?tipoLivroURI),"#") AS ?tipoLivro)
            BIND(STRAFTER(STR(?tipoLinhaURI),"#") AS ?tipoLinha)
        }
        ORDER BY ?linhaID ?titulo
    """
 
    res = exec_query(query)
    linhas_dict = {}

    for row in res["results"]["bindings"]:
        lid        = row["linhaID"]["value"]
        tipo_linha = row["tipoLinha"]["value"]
        livro_id   = row["livroID"]["value"]
        titulo     = row["titulo"]["value"]
        tipo_livro = row["tipoLivro"]["value"]
 
        if lid not in linhas_dict:
            linhas_dict[lid] = {
                "id": lid, 
                "tipo": tipo_linha, 
                "livros": {} 
            }
 
        livros_da_linha = linhas_dict[lid]["livros"]

        if livro_id not in livros_da_linha:
            livros_da_linha[livro_id] = {
                "id": livro_id, 
                "titulo": titulo, 
                "tipos": []
            }
            
        livros_da_linha[livro_id]["tipos"].append(tipo_livro)
 
    for linha in linhas_dict.values():
        linha["livros"] = list(linha["livros"].values())

    return render_template('linhas.html', linhas=list(linhas_dict.values()))

if __name__ == '__main__':
    app.run(debug=True)
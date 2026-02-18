# TPC2 • Continuar a Povoar a Ontologia de Cinema

**Data:** 11/02/2026

### Autor
**ID:** PG60267

**Nome:** Jéssica Cristina Lima da Cunha

<img src="../imgs/autor.jpg" width="150">

## Resumo

Este trabalho consistiu na continuação do desenvolvimento da ontologia de cinema iniciada em sala de aula. O objetivo principal foi consolidar os conceitos de modelação em OWL e a utilização de propriedades para descrever o domínio cinematográfico.

A partir do esboço base, foram realizadas as seguintes expansões:

* **Povoamento com "Madagascar 2":** Foi adicionado o filme `:F_Madagascar2`, associando-lhe os géneros `:G_Aventura` e `:G_Infantil`. Foram também definidas as suas personagens principais, nomeadamente `:Personagem_Alex`, `:Personagem_Marty`, `:Personagem_Melman` e `:Personagem_Gloria`. Estas instâncias foram relacionadas ao filme através da propriedade `:éPersonagem`.

* **Extensão com o filme "Interstellar":** Como filme selecionado do IMDB, foi detalhada a instância `:F_Interstellar`. Além  da ficha técnica, como `:duração` (169 min) e `:data` ("2014-11-07"), o filme foi associado aos géneros `:G_Aventura`, `:G_Drama` e `:G_Ficção`.  Mapeou-se o elenco, ligando os atores`:P_MatthewMcConaughey`, `:P_AnneHathaway`, `:P_JessicaChastain` e `:P_MichaelCaine` às respetivas personagens através da propriedade `:representa`. O filme foi vinculado ao seu realizador, `:P_ChristopherNolan`, através da relação `:foiRealizado`. Por último, ainda foi acrescentada a classe `:FilmeFicção`.


## Resultados

**[cinema.ttl](./cinema.ttl)**
>*Ontologia com o povoamento dos filmes Madagascar 2 e Interstellar.*

---

**[cinema_inferida.ttl](./cinema_inferida.ttl)**
>*Versão da ontologia com o conhecimento inferido pelo reasoner.*

---

*Trabalho realizado no âmbito da UC de Representação e Processamento de Conhecimento na Web (RPCW) 2025/2026*
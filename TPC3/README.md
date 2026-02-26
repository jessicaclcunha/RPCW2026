# TPC3 • GraphDB e SPARQL com a Ontologia do Polvo Filosófico

**Data:** 25/02/2026

### Autor
**ID:** PG60267

**Nome:** Jéssica Cristina Lima da Cunha

<img src="../imgs/autor.jpg" width="150">

## Resumo

O objetivo deste trabalho foi a exploração da ontologia [polvo_filosofico.ttl](polvo_filosofico.ttl) utilizando o GraphDB e a execução de queries SPARQL para extração de conhecimento.

## Resultados

###  Carregar a ontologia, resolvendo problemas se existirem

**Problemas encontrados:**
- A ontologia tem `:Pedido1` definido duas vezes. O GraphDB aceita isso (os triplos são simplesmente fundidos).
- O ingrediente polvo aparece duas vezes de forma diferente como `:PolvoIngrediente` e `:IngredientePolvo`.
- A ontologia define que a classe `:Polvo` não pode consumir pratos que contenham ingredientes da própria classe `:Polvo`. No entanto, o indivíduo `:Aristoteles` (um polvo) gera uma inconsistência ao comer o `:EnsopadoCanibal`, que contém polvo na receita.
- o RoboCozinheiro é subclasse tanto de `:Máquina` quanto de `:Cozinheiro` (que é subclasse de `:Funcionário`, subclasse de `:Pessoa`), ou seja, robô que é simultaneamente máquina e pessoa.

---

### Quem foram os clientes?

```sparql
PREFIX : <http://example.org/polvo-filosofico#>

SELECT ?cliente WHERE {
  ?cliente a :Cliente .
}
```

**Resposta:** Ana, Bruno, Carla, Daniel, Eva, Schrodinger

---

### Que pratos serve o restaurante?

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX : <http://example.org/polvo-filosofico#>

SELECT ?prato ?tipo WHERE {
  ?prato a ?tipo .
  ?tipo rdfs:subClassOf :Prato .
}
```

**Resposta:** SaladaExistencial, TofuMetafisico, BifeDeterminista, PeixeDoLivreArbitrio, PratoDoObservador, DilemaDoSer, EnsopadoCanibal, PratoDoDia

---

### Quais os ingredientes necessários à confeção dos pratos?

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX : <http://example.org/polvo-filosofico#>

SELECT ?prato ?ingrediente WHERE {
  ?prato :temIngrediente ?ingrediente .
}
```
**Resposta:**

| Prato | Ingredientes |
|---|---|
| SaladaExistencial | Alface, Tomate |
| TofuMetafisico | Tofu, Cogumelos |
| BifeDeterminista | CarneVaca |
| PeixeDoLivreArbitrio | Peixe |
| PratoDoObservador | Cogumelos, Peixe |
| DilemaDoSer | Tofu, CarneVaca |
| EnsopadoCanibal | IngredientePolvo |
| PratoDoDia | IngredientePolvo |

---

### Há funcionários que também sejam clientes?
```sparql

PREFIX : <http://example.org/polvo-filosofico#>

SELECT ?pessoa WHERE {
  ?pessoa a :Funcionario .
  ?pessoa a :Cliente .
}
```

**Resposta:** Schrödinger
---

*Trabalho realizado no âmbito da UC de Representação e Processamento de Conhecimento na Web (RPCW) 2025/2026*
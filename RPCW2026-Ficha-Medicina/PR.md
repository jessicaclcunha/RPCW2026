# Ficha • Ontologia Médica
**Data:** 23/03/2026

### Autor
**ID:** PG60267

**Nome:** Jéssica Cristina Lima da Cunha

<img src="../imgs/autor.jpg" width="150">

## Resumo

Este trabalho consistiu no povoamento de uma ontologia médica em OWL/Turtle a partir de datasets CSV e JSON, seguido do desenvolvimento de queries SPARQL.

A partir da ontologia base `medical.ttl`, foram realizadas as seguintes expansões:

* **Doenças e Sintomas:** A partir do ficheiro `Disease_Syntoms.csv` foram criadas instâncias de `:Disease` para cada doença e instâncias de `:Symptom` para cada sintoma, associando-os através da propriedade `:hasSymptom`. A ontologia foi guardada em `med_doencas.ttl`.

* **Descrições:** A partir do ficheiro `Disease_Description.csv` foi adicionada a propriedade `:description` a cada doença.

* **Tratamentos:** A partir do ficheiro `Disease_Treatment.csv` foram criadas instâncias de `:Treatment` e associadas a cada doença através da propriedade `:hasTreatment`. A ontologia foi guardada em `med_tratamentos.ttl`.

* **Doentes:** A partir do ficheiro `doentes.json` foram criadas 10000 instâncias de `:Patient`, cada uma com um id gerado automaticamente (`Patient_1`, `Patient_2`, ...), um nome e uma lista de sintomas via `:exhibitsSymptom`. A ontologia foi guardada em `med_doentes.ttl`.

* **Diagnóstico:** Foi criada uma query SPARQL CONSTRUCT que diagnostica a doença de cada doente, produzindo triplos da forma `:patientX :hasDisease :diseaseY`. A lógica usada é: um doente tem uma doença se exibir **todos** os seus sintomas. Os triplos são depois inseridos na ontologia com INSERT.


## Resultados

**[populate.py](./populate.py)**
>*Script Python que povoa a ontologia a partir dos datasets.*

---

**[med_doencas.ttl](./med_doencas.ttl)**
>*Ontologia com doenças, sintomas e descrições.*

---

**[med_tratamentos.ttl](./med_tratamentos.ttl)**
>*Ontologia anterior acrescida dos tratamentos.*

---

**[med_doentes.ttl](./med_doentes.ttl)**
>*Ontologia anterior acrescida dos doentes.*

---

**[sparql.txt](./sparql.txt)**
>*Queries SPARQL.*

---

*Trabalho realizado no âmbito da UC de Representação e Processamento de Conhecimento na Web (RPCW) 2025/2026*
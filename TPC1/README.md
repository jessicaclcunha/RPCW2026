# TPC1 • Ontologia de uma História

**Data:** 09/02/2026

### Autor
**ID:** PG60267

**Nome:** Jéssica Cristina Lima da Cunha

<img src="../imgs/autor.jpg" width="150">

## Resumo

Este trabalho teve como objetivo a criação de uma ontologia em **OWL** para modelar o conhecimento presente numa história sobre o ensino e aprendizagem de línguas na Universidade do Minho.

A ontologia desenvolvida modela o domínio do ensino de línguas através de seis classes principais: **Pessoa**, **Língua**, **Curso**, **Instituição**, **Cidade** e **País**. Foram definidas propriedades de dados como *temIdade*, *temHorário* e *éLecionadoEm*, e dez propriedades de objetos que estabelecem relações semânticas entre indivíduos. As principais relações incluem *falaLíngua* e *aprendeLíngua* (relacionam pessoas com línguas), *frequenta* e *leciona* (conectam pessoas a cursos), *estudaEm* e *docenteDe* (associam pessoas a instituições), *oriundoDe* (indica proveniência geográfica), *pertenceA* (relaciona instituições), e as propriedades simétricas *amigoDe* e *parceiroLinguisticoDe* (estabelecem relações bidirecionais entre pessoas).

A ontologia instancia 17 indivíduos que representam a narrativa, incluindo cinco pessoas (Eduardo, Ana, Carlos, Hanna e Helmut Ratz), quatro línguas (Português, Espanhol, Inglês e Alemão), dois cursos (Alemão e Biotecnologia), três instituições (Universidade do Minho, Centro de Línguas, Escola de Letras), e duas localizações (Porto e Alemanha).


## Resultados

| Ficheiro | Descrição |
|----------|-----------|
| [historia.ttl](./historia.ttl) | Ontologia completa da história em formato Turtle com todas as classes, propriedades e indivíduos |

---

*Trabalho realizado no âmbito da UC de Representação e Processamento de Conhecimento na Web (RPCW) 2025/2026*
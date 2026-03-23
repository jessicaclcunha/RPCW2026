import csv
import json
from rdflib import Graph, Namespace, RDF, OWL, RDFS, Literal
from rdflib.namespace import XSD

NS = Namespace("http://www.example.org/disease-ontology#")

g = Graph()
g.parse("medical.ttl", format="turtle")
g.bind("", NS)

def to_id(name):
    return name.strip().replace(" ", "_").replace("(", "").replace(")", "").replace("-", "_")


disease_symptoms = {}

with open("Disease_Syntoms.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        disease = row["Disease"].strip()
        symptoms = [v.strip() for k, v in row.items() if k.startswith("Symptom") and v.strip()]
        if disease not in disease_symptoms:
            disease_symptoms[disease] = set()
        disease_symptoms[disease].update(symptoms)

for disease, symptoms in disease_symptoms.items():
    d = NS[to_id(disease)]
    g.add((d, RDF.type, NS.Disease))
    for symptom in symptoms:
        s = NS[to_id(symptom)]
        g.add((s, RDF.type, NS.Symptom))
        g.add((d, NS.hasSymptom, s))


g.add((NS.description, RDF.type, OWL.DatatypeProperty))
g.add((NS.description, RDFS.domain, NS.Disease))
g.add((NS.description, RDFS.range, XSD.string))

with open("Disease_Description.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        d = NS[to_id(row["Disease"].strip())]
        g.add((d, NS.description, Literal(row["Description"].strip())))

g.serialize("med_doencas.ttl", format="turtle")
print("✓ med_doencas.ttl gerado")


with open("Disease_Treatment.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        d = NS[to_id(row["Disease"].strip())]
        for k in ["Precaution_1", "Precaution_2", "Precaution_3", "Precaution_4"]:
            val = row.get(k, "").strip()
            if val:
                t = NS[to_id(val)]
                g.add((t, RDF.type, NS.Treatment))
                g.add((d, NS.hasTreatment, t))

g.serialize("med_tratamentos.ttl", format="turtle")
print("✓ med_tratamentos.ttl gerado")


with open("doentes.json", encoding="utf-8") as f:
    doentes = json.load(f)

for idx, doente in enumerate(doentes, start=1):
    p = NS[f"Patient_{idx}"]
    g.add((p, RDF.type, NS.Patient))
    g.add((p, NS.name, Literal(doente["nome"].strip())))
    for symptom in doente["sintomas"]:
        s = NS[to_id(symptom)]
        g.add((s, RDF.type, NS.Symptom))
        g.add((p, NS.exhibitsSymptom, s))

g.serialize("med_doentes.ttl", format="turtle")
print("✓ med_doentes.ttl gerado")
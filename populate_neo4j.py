from py2neo import Graph, Node, Relationship
import csv

graph = Graph("bolt://localhost:7687", auth=("neo4j", "senha"))
graph.delete_all()

pontos = {}
with open("data/pontos.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        node = Node(row["tipo"], id=int(row["id"]), nome=row["nome"], localizacao=row["localizacao"])
        graph.create(node)
        pontos[row["id"]] = node

with open("data/conexoes.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        origem = pontos[row["origem"]]
        destino = pontos[row["destino"]]
        rel = Relationship(origem, "CONECTA_A", destino,
                           distancia=float(row["distancia_km"]),
                           tempo=float(row["tempo_min"]))
        graph.create(rel)

with open("data/alunos.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        aluno = Node("Aluno", id=int(row["id"]), nome=row["nome"])
        graph.create(aluno)
        rel = Relationship(aluno, "ESPERA_EM", pontos[row["ponto_id"]])
        graph.create(rel)

print("Banco de dados populado com sucesso!")

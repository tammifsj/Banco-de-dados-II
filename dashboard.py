import streamlit as st
from py2neo import Graph

st.set_page_config(page_title="Rotas Escolares", page_icon="🚍", layout="wide")
st.title("🚍 Sistema de Rotas de Transporte Escolar")

graph = Graph("bolt://localhost:7687", auth=("neo4j", "senha"))

st.sidebar.header("Escolha o ponto de embarque:")
pontos = [record["nome"] for record in graph.run("MATCH (p:PontoEmbarque) RETURN p.nome AS nome").data()]
ponto_origem = st.sidebar.selectbox("Ponto de partida:", pontos)

if st.button("Calcular menor rota até a escola"):
    query = f"""
    MATCH (inicio:PontoEmbarque {{nome:'{ponto_origem}'}}), (fim:Escola {{nome:'Escola Central'}})
    CALL gds.shortestPath.dijkstra.stream({{
      sourceNode: id(inicio),
      targetNode: id(fim),
      relationshipWeightProperty: 'tempo'
    }})
    YIELD totalCost
    RETURN totalCost;
    """
    result = graph.run(query).data()
    if result:
        st.success(f"🕒 Tempo estimado: {result[0]['totalCost']} minutos")
    else:
        st.warning("Nenhuma rota encontrada.")

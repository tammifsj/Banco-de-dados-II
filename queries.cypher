MATCH (inicio:PontoEmbarque {nome:'Ponto A'}), (fim:Escola {nome:'Escola Central'})
CALL gds.shortestPath.dijkstra.stream({
  sourceNode: id(inicio),
  targetNode: id(fim),
  relationshipWeightProperty: 'distancia_km'
})
YIELD totalCost
RETURN totalCost;

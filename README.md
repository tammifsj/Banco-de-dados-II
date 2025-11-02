# 🚍 Transporte Escolar com Banco de Grafos (Neo4j + Streamlit)

Este projeto demonstra como usar um **banco de dados orientado a grafos (Neo4j)** para otimizar rotas de transporte escolar, considerando **distância e tempo entre pontos de embarque e escolas**.

## ⚙️ Tecnologias
- **Neo4j** — Banco de dados orientado a grafos  
- **Cypher** — Linguagem de consultas de grafos  
- **Python + Streamlit + Py2Neo** — Interface e conexão

## 📊 Estrutura de Grafo
- **Nós:** `PontoEmbarque`, `Escola`, `Aluno`
- **Arestas:** `CONECTA_A`, `ESPERA_EM`

## 🚀 Execução
1. Inicie o servidor Neo4j localmente (`localhost:7687`)
2. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/transporte-escolar-grafos.git
   cd transporte-escolar-grafos
   ```
3. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Popule o banco:
   ```bash
   python scripts/populate_neo4j.py
   ```
5. Rode o app:
   ```bash
   streamlit run app/dashboard.py
   ```

## 💡 Exemplo de Consulta
```cypher
MATCH (p:PontoEmbarque)-[:CONECTA_A*]->(e:Escola)
RETURN p,e;
```

## 🧠 Autor
Trabalho acadêmico sobre **Bancos de Dados Orientados a Grafos** — tema: *Rotas de Transporte Escolar*.

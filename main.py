import os

# Estrutura de diretórios
structure = {
    "docs": {
        "index.md": "# Índice de Custo de Vida (ICV) da Bahia\n\nBem-vindo ao projeto do ICV!\n",
        "metodologia.md": "# Metodologia\n\nExplicação da coleta de dados, pipeline e estrutura.\n",
        "dashboard.md": "# Dashboard\n\n[Acesse o dashboard interativo](https://seudashboard.streamlit.app)\n",
        "publicacoes.md": "# Publicações\n\nLista de artigos, papers e links relevantes.\n",
        "categorias": {
            "alimentacao.md": "# Alimentação\n\nDetalhes dos custos com alimentação.\n",
            "habitacao.md": "# Habitação\n\nAnálise dos custos de moradia.\n",
            "transporte.md": "# Transporte\n\nCustos com transporte urbano e individual.\n"
        },
        "analises": {
            "graficos.md": "# Gráficos\n\nVisualizações de dados.\n",
            "previsoes.md": "# Previsões\n\nModelos preditivos aplicados.\n"
        }
    },
    "mkdocs.yml": """
site_name: ICV Bahia
theme:
  name: material
nav:
  - Início: index.md
  - Metodologia: metodologia.md
  - Categorias:
      - Alimentação: categorias/alimentacao.md
      - Habitação: categorias/habitacao.md
      - Transporte: categorias/transporte.md
  - Análises:
      - Gráficos: analises/graficos.md
      - Previsões: analises/previsoes.md
  - Dashboard: dashboard.md
  - Publicações: publicacoes.md
"""
}

def create_structure(base_path, struct):
    for name, content in struct.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)

project_path = "/mnt/data/icv-site"
os.makedirs(project_path, exist_ok=True)
create_structure(project_path, structure)

project_path

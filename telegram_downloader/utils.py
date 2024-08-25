import re
import json
import os

def nome_arquivo_seguro(nome):
    """Remove caracteres inválidos do nome do arquivo."""
    return re.sub(r'[\\/*?:"<>|]', "_", nome)

def salvar_json(dados, caminho):
    """Salva dados em um arquivo JSON."""
    with open(caminho, 'w') as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

def carregar_json(caminho):
    """Carrega dados de um arquivo JSON."""
    if os.path.exists(caminho):
        with open(caminho, 'r') as file:
            return json.load(file)
    return []

def criar_pasta_se_necessario(caminho):
    """Cria uma pasta se ela não existir."""
    os.makedirs(caminho, exist_ok=True)

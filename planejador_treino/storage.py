import json
from pathlib import Path

ARQUIVO = Path(__file__).parent / "treinos.json"


def carregar_treinos():
    if not ARQUIVO.exists():
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_treinos(treinos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(treinos, f, indent=4, ensure_ascii=False)

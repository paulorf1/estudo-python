import json
from pathlib import Path

ARQUIVO = Path(__file__).parent / "tarefas.json"


def carregar_tarefas():
    if not ARQUIVO.exists():
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

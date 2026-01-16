import json
from pathlib import Path

ARQUIVO = Path(__file__).parent / "chamados.json"


def carregar_chamados():
    if not ARQUIVO.exists():
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_chamados(chamados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(chamados, f, indent=4, ensure_ascii=False)

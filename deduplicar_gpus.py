import json

entrada = "gpus_simplificado.json"
saida = "gpus_final.json"

with open(entrada, encoding="utf-8") as f:
    gpus = json.load(f)

unicos = {}

for gpu in gpus:
    nome = gpu["nome"]
    score = gpu["score"]

    if nome not in unicos:
        unicos[nome] = gpu
    else:
        if score > unicos[nome]["score"]:
            unicos[nome] = gpu

gpus_final = list(unicos.values())

with open(saida, "w", encoding="utf-8") as f:
    json.dump(gpus_final, f, indent=4, ensure_ascii=False)

print(f"{len(gpus_final)} GPUs únicas salvas em {saida}")

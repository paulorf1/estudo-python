import json

entrada = "cpus_simplificado.json"
saida = "cpus_final.json"

with open(entrada, encoding="utf-8") as f:
    cpus = json.load(f)

unicos = {}

for cpu in cpus:
    nome = cpu["nome"]
    score = cpu["score"]

    if nome not in unicos:
        unicos[nome] = cpu
    else:
        if score > unicos[nome]["score"]:
            unicos[nome] = cpu

cpus_final = list(unicos.values())

with open(saida, "w", encoding="utf-8") as f:
    json.dump(cpus_final, f, indent=4, ensure_ascii=False)

print(f"{len(cpus_final)} CPUs únicas salvas em {saida}")

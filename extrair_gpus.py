import json

entrada = "video-card.json"
saida = "gpus_simplificado.json"

gpus_simplificado = []

with open(entrada, "r", encoding="utf-8") as f:
    gpus = json.load(f)

for gpu in gpus:
    nome = gpu.get("chipset") or gpu.get("name")

    memoria = gpu.get("memory")

    boost = gpu.get("boost_clock")
    base = gpu.get("core_clock")

    clock = boost if boost is not None else base

    if not nome or not memoria or not clock:
        continue

    score = int(memoria * clock)

    gpus_simplificado.append({
        "nome": nome,
        "score": score,
        "memoria": memoria,
        "clock": clock
    })

with open(saida, "w", encoding="utf-8") as f:
    json.dump(gpus_simplificado, f, indent=4, ensure_ascii=False)

print(f"{len(gpus_simplificado)} GPUs salvas em {saida}")

import json

entrada = "cpu.json"
saida = "cpus_simplificado.json"

cpus_simplificado = []

with open(entrada, "r", encoding="utf-8") as f:
    cpus = json.load(f)

for cpu in cpus:
    nome = cpu.get("name")
    cores = cpu.get("core_count")

    boost = cpu.get("boost_clock")
    base = cpu.get("core_clock")

    # escolher o melhor clock disponível
    clock = boost if boost is not None else base

    # validação de dados
    if not nome or not cores or not clock:
        continue

    score = int(cores * clock)

    cpus_simplificado.append({
        "nome": nome,
        "score": score,
        "cores": cores,
        "clock": clock
    })

with open(saida, "w", encoding="utf-8") as f:
    json.dump(cpus_simplificado, f, indent=4, ensure_ascii=False)

print(f"{len(cpus_simplificado)} CPUs salvas em {saida}")

import json

# ================== CONSTANTES ==================

FATOR_RESOLUCAO = {
    "HD": 1.4,
    "Full HD": 1.0,
    "Quad HD": 0.7,
    "4K": 0.45,
}

# Jogos com FPS de referência em FULL HD / ALTO
# Hardware de referência: RTX 3060 Ti + Ryzen 5 5600
JOGOS = [
    {"nome": "Cyberpunk 2077", "fps_ref": 75, "peso_gpu": 0.75},
    {"nome": "Red Dead Redemption 2", "fps_ref": 85, "peso_gpu": 0.7},
    {"nome": "Warzone", "fps_ref": 130, "peso_gpu": 0.65},
    {"nome": "GTA V", "fps_ref": 140, "peso_gpu": 0.55},
    {"nome": "Fortnite", "fps_ref": 180, "peso_gpu": 0.5},
    {"nome": "CS2", "fps_ref": 300, "peso_gpu": 0.4},
]

# ================== CLASSES ==================


class CPU:
    def __init__(self, nome: str, perf: float) -> None:
        self.nome = nome
        self.perf = perf

    def __str__(self) -> str:
        return self.nome


class GPU:
    def __init__(self, nome: str, perf: float) -> None:
        self.nome = nome
        self.perf = perf

    def __str__(self) -> str:
        return self.nome


class Build:
    def __init__(self, cpu: CPU, gpu: GPU, cpu_ref: CPU, gpu_ref: GPU) -> None:
        self.cpu = cpu
        self.gpu = gpu
        self.cpu_ref = cpu_ref
        self.gpu_ref = gpu_ref

    # ---- FPS POR JOGO / RESOLUÇÃO ----
    def fps_jogo(self, jogo, resolucao):
        peso_gpu = jogo["peso_gpu"]
        peso_cpu = 1 - peso_gpu

        fator_hw = (
            (self.gpu.perf / self.gpu_ref.perf) ** peso_gpu
            * (self.cpu.perf / self.cpu_ref.perf) ** peso_cpu
        )

        fps = jogo["fps_ref"] * fator_hw * FATOR_RESOLUCAO[resolucao]
        return max(5, int(fps))

    # ---- SCORE GAMER (MÉDIA DOS JOGOS EM FULL HD) ----
    def score_gamer(self):
        fps = [self.fps_jogo(j, "Full HD") for j in JOGOS]
        media = sum(fps) / len(fps)

        score = (media / 140) * 100  # 140 ≈ média da build referência
        return min(score, 150)

    # ---- RESOLUÇÃO RECOMENDADA (REALISTA) ----
    def resolucao_recomendada(self):
        for res in ["4K", "Quad HD", "Full HD", "HD"]:
            fps = [self.fps_jogo(j, res) for j in JOGOS]
            media = sum(fps) / len(fps)

            if media >= 60:
                return res

        return "Não recomendado"

    # ---- NÍVEL DA BUILD (LIMITADO PELO PIOR COMPONENTE) ----
    def nivel_build(self):
        score_cpu = (self.cpu.perf / self.cpu_ref.perf) * 100
        score_gpu = (self.gpu.perf / self.gpu_ref.perf) * 100

        score_final = min(score_cpu, score_gpu)

        if score_final >= 130:
            return "Entusiasta"
        elif score_final >= 100:
            return "High-end"
        elif score_final >= 70:
            return "Intermediária"
        elif score_final >= 45:
            return "Entrada"
        else:
            return "Muito fraca"

    # ---- GARGALO ----
    def gargalo(self):
        if self.gpu.perf > self.cpu.perf * 1.4:
            return "Gargalo na CPU"
        elif self.cpu.perf > self.gpu.perf * 1.4:
            return "Gargalo na GPU"
        else:
            return "Equilibrado"

    # ---- RESUMO ----
    def resumo(self):
        linhas = []
        res = self.resolucao_recomendada()

        linhas.append("=== RESULTADO DA SIMULAÇÃO ===")
        linhas.append(f"CPU: {self.cpu.nome}")
        linhas.append(f"GPU: {self.gpu.nome}")
        linhas.append(f"Nível da build: {self.nivel_build()}")
        linhas.append(f"Gargalo: {self.gargalo()}")
        linhas.append(f"Resolução recomendada: {res}")
        linhas.append(f"Score Gamer: {self.score_gamer():.1f}/100\n")
        linhas.append("FPS por jogo:")

        for j in JOGOS:
            r = res if res != "Não recomendado" else "Full HD"
            fps = self.fps_jogo(j, r)
            linhas.append(f" - {j['nome']}: {fps} FPS ({r})")

        return "\n".join(linhas)


# ================== CARREGAR DADOS ==================


def carregar_dados():
    with open("cpus_gamer.json", encoding="utf-8") as f:
        cpu_dados = json.load(f)

    with open("gpus_gamer.json", encoding="utf-8") as f:
        gpu_dados = json.load(f)

    cpus = [CPU(c["nome"], c["perf"]) for c in cpu_dados]
    gpus = [GPU(g["nome"], g["perf"]) for g in gpu_dados]

    # HARDWARE DE REFERÊNCIA (BASE DOS BENCHMARKS)
    cpu_ref = next(c for c in cpus if c.nome == "Ryzen 5 5600")
    gpu_ref = next(g for g in gpus if g.nome == "RTX 3060 Ti")

    print(f"{len(cpus)} CPUs carregadas.")
    print(f"{len(gpus)} GPUs carregadas.")
    print(f"Base de referência: {cpu_ref.nome} + {gpu_ref.nome}")

    return cpus, gpus, cpu_ref, gpu_ref


# ================== BUSCA ==================


def buscar(lista, termo):
    termo = termo.lower()
    return [x for x in lista if termo in x.nome.lower()]


# ================== SIMULAÇÃO ==================


def simular(cpus, gpus, cpu_ref, gpu_ref):
    termo_cpu = input("\nDigite parte do nome da CPU: ")
    resultados_cpu = buscar(cpus, termo_cpu)

    if not resultados_cpu:
        print("Nenhuma CPU encontrada.")
        return

    for i, c in enumerate(resultados_cpu, 1):
        print(f"{i}. {c.nome}")

    try:
        cpu = resultados_cpu[int(input("Escolha a CPU: ")) - 1]
    except:
        print("CPU inválida.")
        return

    termo_gpu = input("\nDigite parte do nome da GPU: ")
    resultados_gpu = buscar(gpus, termo_gpu)

    if not resultados_gpu:
        print("Nenhuma GPU encontrada.")
        return

    for i, g in enumerate(resultados_gpu, 1):
        print(f"{i}. {g.nome}")

    try:
        gpu = resultados_gpu[int(input("Escolha a GPU: ")) - 1]
    except:
        print("GPU inválida.")
        return

    build = Build(cpu, gpu, cpu_ref, gpu_ref)
    print()
    print(build.resumo())


# ================== MENU ==================


def main():
    cpus, gpus, cpu_ref, gpu_ref = carregar_dados()

    while True:
        print("\n=== PC BUILDER GAMER ===")
        print("1 - Simular build")
        print("0 - Sair")

        op = input("Opção: ").strip()

        if op == "1":
            simular(cpus, gpus, cpu_ref, gpu_ref)
        elif op == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()

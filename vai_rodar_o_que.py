# Simulação de desempenho de jogos com base em CPU, GPU e resolução.

import json  # Biblioteca para ler arquivos no formato JSON

# ================== CONSTANTES ==================

# Fatores que simulam a queda/aumento de FPS conforme a resolução
# Quanto maior a resolução, menor o multiplicador de FPS
FATOR_RESOLUCAO = {
    "HD": 1.4,        # Mais FPS por ter menos pixels
    "Full HD": 1.0,  # Base de referência
    "Quad HD": 0.7,  # Queda moderada de FPS
    "4K": 0.45,      # Queda grande de FPS
}

# Lista de jogos com:
# - fps_ref: FPS médio em Full HD / Alto na build de referência
# - peso_gpu: quanto o jogo depende da GPU (o resto depende da CPU)
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

# Representa uma CPU com nome e índice de performance


class CPU:
    def __init__(self, nome: str, perf: float) -> None:
        self.nome = nome      # Nome da CPU
        self.perf = perf      # Índice de desempenho relativo

    # Define como o objeto será exibido ao usar print()
    def __str__(self) -> str:
        return self.nome


# Representa uma GPU com nome e índice de performance
class GPU:
    def __init__(self, nome: str, perf: float) -> None:
        self.nome = nome      # Nome da GPU
        self.perf = perf      # Índice de desempenho relativo

    def __str__(self) -> str:
        return self.nome


# Representa a combinação CPU + GPU (a build do PC)
class Build:
    def __init__(self, cpu: CPU, gpu: GPU, cpu_ref: CPU, gpu_ref: GPU) -> None:
        self.cpu = cpu              # CPU escolhida pelo usuário
        self.gpu = gpu              # GPU escolhida pelo usuário
        self.cpu_ref = cpu_ref      # CPU de referência (benchmark base)
        self.gpu_ref = gpu_ref      # GPU de referência (benchmark base)

    # ---- FPS POR JOGO / RESOLUÇÃO ----
    def fps_jogo(self, jogo, resolucao):
        # Percentual de dependência da GPU para o jogo
        peso_gpu = jogo["peso_gpu"]

        # O restante do peso vai para a CPU
        peso_cpu = 1 - peso_gpu

        # Fator de desempenho relativo ao hardware de referência
        # Usa potência para suavizar a influência de CPU/GPU
        fator_hw = (
            (self.gpu.perf / self.gpu_ref.perf) ** peso_gpu
            * (self.cpu.perf / self.cpu_ref.perf) ** peso_cpu
        )

        # FPS final considerando hardware e resolução
        fps = jogo["fps_ref"] * fator_hw * FATOR_RESOLUCAO[resolucao]

        # Garante um mínimo de 5 FPS e converte para inteiro
        return max(5, int(fps))

    # ---- SCORE GAMER (MÉDIA DOS JOGOS EM FULL HD) ----
    def score_gamer(self):
        # Calcula o FPS em Full HD para todos os jogos
        fps = [self.fps_jogo(j, "Full HD") for j in JOGOS]

        # Média de FPS entre os jogos
        media = sum(fps) / len(fps)

        # Score relativo à build de referência (≈140 FPS médio)
        score = (media / 140) * 100

        # Limita o score máximo para evitar valores exagerados
        return min(score, 150)

    # ---- RESOLUÇÃO RECOMENDADA (REALISTA) ----
    def resolucao_recomendada(self):
        # Testa das resoluções mais pesadas para as mais leves
        for res in ["4K", "Quad HD", "Full HD", "HD"]:
            fps = [self.fps_jogo(j, res) for j in JOGOS]
            media = sum(fps) / len(fps)

            # Se a média for pelo menos 60 FPS, recomenda a resolução
            if media >= 60:
                return res

        # Se nem em HD atingir 60 FPS
        return "Não recomendado"

    # ---- NÍVEL DA BUILD (LIMITADO PELO PIOR COMPONENTE) ----
    def nivel_build(self):
        # Score percentual da CPU em relação à referência
        score_cpu = (self.cpu.perf / self.cpu_ref.perf) * 100

        # Score percentual da GPU em relação à referência
        score_gpu = (self.gpu.perf / self.gpu_ref.perf) * 100

        # A build é limitada pelo componente mais fraco
        score_final = min(score_cpu, score_gpu)

        # Classificação por faixas de desempenho
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
        # GPU muito mais forte que a CPU → gargalo na CPU
        if self.gpu.perf > self.cpu.perf * 1.4:
            return "Gargalo na CPU"

        # CPU muito mais forte que a GPU → gargalo na GPU
        elif self.cpu.perf > self.gpu.perf * 1.4:
            return "Gargalo na GPU"

        # Diferença aceitável → sistema equilibrado
        else:
            return "Equilibrado"

    # ---- RESUMO FINAL DA BUILD ----
    def resumo(self):
        linhas = []
        res = self.resolucao_recomendada()

        # Cabeçalho do relatório
        linhas.append("=== RESULTADO DA SIMULAÇÃO ===")
        linhas.append(f"CPU: {self.cpu.nome}")
        linhas.append(f"GPU: {self.gpu.nome}")
        linhas.append(f"Nível da build: {self.nivel_build()}")
        linhas.append(f"Gargalo: {self.gargalo()}")
        linhas.append(f"Resolução recomendada: {res}")
        linhas.append(f"Score Gamer: {self.score_gamer():.1f}/100\n")
        linhas.append("FPS por jogo:")

        # Mostra FPS de cada jogo na resolução recomendada
        for j in JOGOS:
            r = res if res != "Não recomendado" else "Full HD"
            fps = self.fps_jogo(j, r)
            linhas.append(f" - {j['nome']}: {fps} FPS ({r})")

        # Junta todas as linhas em uma única string
        return "\n".join(linhas)


# ================== CARREGAR DADOS ==================

def carregar_dados():
    # Abre o arquivo de CPUs e carrega o JSON em lista de dicionários
    with open("cpus_gamer.json", encoding="utf-8") as f:
        cpu_dados = json.load(f)

    # Abre o arquivo de GPUs e carrega o JSON em lista de dicionários
    with open("gpus_gamer.json", encoding="utf-8") as f:
        gpu_dados = json.load(f)

    # Converte dicionários em objetos CPU e GPU
    cpus = [CPU(c["nome"], c["perf"]) for c in cpu_dados]
    gpus = [GPU(g["nome"], g["perf"]) for g in gpu_dados]

    # HARDWARE DE REFERÊNCIA (BASE DOS BENCHMARKS)
    cpu_ref = next(c for c in cpus if c.nome == "Ryzen 5 5600")
    gpu_ref = next(g for g in gpus if g.nome == "RTX 3060 Ti")

    # Informações de carregamento
    print(f"{len(cpus)} CPUs carregadas.")
    print(f"{len(gpus)} GPUs carregadas.")
    print(f"Base de referência: {cpu_ref.nome} + {gpu_ref.nome}")

    return cpus, gpus, cpu_ref, gpu_ref


# ================== BUSCA ==================

def buscar(lista, termo):
    # Busca parcial e sem diferenciar maiúsculas/minúsculas
    termo = termo.lower()
    return [x for x in lista if termo in x.nome.lower()]


# ================== SIMULAÇÃO ==================

def simular(cpus, gpus, cpu_ref, gpu_ref):
    # Entrada do usuário para CPU
    termo_cpu = input("\nDigite parte do nome da CPU: ")
    resultados_cpu = buscar(cpus, termo_cpu)

    if not resultados_cpu:
        print("Nenhuma CPU encontrada.")
        return

    # Mostra opções encontradas
    for i, c in enumerate(resultados_cpu, 1):
        print(f"{i}. {c.nome}")

    # Escolha da CPU
    try:
        cpu = resultados_cpu[int(input("Escolha a CPU: ")) - 1]
    except:
        print("CPU inválida.")
        return

    # Entrada do usuário para GPU
    termo_gpu = input("\nDigite parte do nome da GPU: ")
    resultados_gpu = buscar(gpus, termo_gpu)

    if not resultados_gpu:
        print("Nenhuma GPU encontrada.")
        return

    # Mostra opções encontradas
    for i, g in enumerate(resultados_gpu, 1):
        print(f"{i}. {g.nome}")

    # Escolha da GPU
    try:
        gpu = resultados_gpu[int(input("Escolha a GPU: ")) - 1]
    except:
        print("GPU inválida.")
        return

    # Cria a build e mostra o resumo
    build = Build(cpu, gpu, cpu_ref, gpu_ref)
    print()
    print(build.resumo())


# ================== MENU PRINCIPAL ==================

def main():
    # Carrega dados ao iniciar o programa
    cpus, gpus, cpu_ref, gpu_ref = carregar_dados()

    # Loop do menu
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


# Ponto de entrada do programa
if __name__ == "__main__":
    main()

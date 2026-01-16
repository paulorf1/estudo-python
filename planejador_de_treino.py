energia = 100
forca = 10
vida = 100
lesao = False

print("Missão academia")
print("Você chegou para treinar!")

# Decisão 1 - Aquecimento

print("\n Você vai começar com: ")
print("1 - Aquecimento")
print("2 - Ir direto para o treino pesado: ")

opcao = input("Escolha: ")

if opcao == "1":
    print("Bom! Você se aqueceu.")
    energia -= 10
    forca += 2

else:
    print("Você pulou o aquecimento...")
    energia -= 5
    lesao = True

# Decisão 2 - Treino

if lesao:
    print("\nVocê está lesionado e não consegue treinar pesado.")
else:
    print("\n Agora você escolhe: ")
    print("1 - Treino de força")
    print("2 - Cardio intenso")

    opcao = input("Escolha: ")

    if opcao == "1":
        print("Treino pesado de força")
        energia -= 30
        forca += 5
        vida -= 25
    else:
        print("Cardio puxado!")
        energia -= 25
        forca += 2
        vida -= 10

# Decisão 3 - verificação de vida

if vida <= 0:
    print("você desmaiou no treino! Fim de jogo. ")
    exit()

print("\n Antes de ir embora você escolhe: ")
print("1 - Tomar suplemento")
print("2 - Ir embora direto")

opcao = input("Escolha: ")

if opcao == '1':
    print("Você tomou suplemento e recuperou desempenho!")
    vida += 15
    if vida > 100:
        vida = 100
    energia -= 10
    forca += 3
else:
    print("Você foi embora descansar.")


# Resultado final

print("\n === Resultado do dia === ")
print(f"Energia: {energia}")
print(f"Força: {forca}")

if lesao:
    print("Você se lesionou por falta de aquecimento ")

if energia <= 0:
    print("Você saiu totalmente exausto! ")

if forca >= 20 and not lesao:
    print("Excelente treino! Evolução máxima ")

elif forca >= 15:
    print("Bom treino! ")

else:
    print("treino fofo hoje...")

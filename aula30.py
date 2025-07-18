"""Add commentMore actions
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61 # representa a velocidade atual do carro
local_carro = 100 # representa a posição atual do carro

RADAR_1 = 60 # define a velocidade máxima permitida no Radar 1, variáveis em MAIÚSCULAS indica que são "constantes", não mudam durante execução
LOCAL_1 = 100 # a localização exata do radar
RADAR_RANGE = 1 # define a 'margem de alcance' do radar, o carro é considerado "no radar" se estiver dentro de 1 unidade de distância de LOCAL_1 (para mais ou para menos)

velocidade_carro_passou_radar_1 = velocidade > RADAR_1 #verifica se a velocidade do carro é maior que a velocidade permitida (60)
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE ) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) 
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1 # esta linha verifica se o carro está dentro da área de alcance do Radar 1

if velocidade_carro_passou_radar_1: # como velocidade_carro_passou_radar_1 é True, o print a seguir é exibido
    print(f'Velocidade carro passou do radar 1')

if carro_passou_radar_1: # como carro_passou_radar_1 é True, o print a seguir é exibido
    print(f'Carro passou radar 1')

if carro_multado_radar_1: # como carro_multado_radar_1 é True, o print a seguir é exibido
    print(f'Carro multado em radar 1')
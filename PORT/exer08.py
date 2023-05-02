tempo_gasto = float(input("Qual o tempo despendido em horas? \n")) 
velocidade_media = float(input("Qual a velocidade média neste tempo? \n"))
distancia = tempo_gasto * velocidade_media
litro_gasto = distancia / 12
print(f"A quantidade de combustível gasto é: {litro_gasto}")
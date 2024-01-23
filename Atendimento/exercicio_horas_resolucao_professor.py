partida = input("partida (HH:MM:ss): ")
hora_partida, minutos_partida, segundos_partida = partida.split(":")
hora_partida = int(hora_partida) * 3600
if hora_partida == 0:
    hora_partida = 24 * 3600
minutos_partida = int(minutos_partida) * 60
segundos_partida = int(segundos_partida)
chegada = input("chegada (HH:MM:ss): ")
hora_chegada, minutos_chegada, segundos_chegada = chegada.split(":")
hora_chegada = int(hora_chegada) * 3600
if hora_chegada == 0:
    hora_chegada = 24 * 3600
minutos_chegada = int(minutos_chegada) * 60
segundos_chegada = int(segundos_chegada)
horas_resultados = (hora_chegada - hora_partida)
minutos_resultado = (minutos_chegada - minutos_partida)
segundos_resultado = segundos_chegada - segundos_partida
print(f"{horas_resultados / 3600:.0f}:{minutos_resultado / 60:.0f}:{segundos_resultado:.0f}")

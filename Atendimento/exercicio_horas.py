from datetime import date, timedelta, time
partida = input("Hora partida (HH:MM:ss): ")
hora_partida, minutos_partida, segundos_partida = partida.split(":")
chegada = input("Hora chegada (HH:MM:ss): ")
hora_chegada, minutos_chegada, segundos_chegada = chegada.split(":")

resultado_partida = time(hour=int(hora_partida), minute=int(minutos_partida), second=int(segundos_partida))
resultado_chegada = time(hour=int(hora_chegada), minute=int(minutos_chegada), second=int(segundos_chegada))

print(timedelta(hours=resultado_chegada.hour, minutes=resultado_chegada.minute, seconds=resultado_chegada.second) -
      timedelta(hours=resultado_partida.hour, minutes=resultado_partida.minute, seconds=resultado_partida.second))

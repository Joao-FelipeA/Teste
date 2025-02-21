import datetime 
import random

def horario_local():
    hora_agora = datetime.datetime.now()
    return hora_agora

hora = horario_local()
sequencia_aleatoria = random.sample(["a", "b", "c", "d", "e","f", "g", "h", "i", "j", "k", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], k=7 )

sequencia_unida = ''.join(sequencia_aleatoria)


print(f"O seu codigo de rastreio é {sequencia_unida} e o horario da envio foi às {hora}")
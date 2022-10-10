from datetime import datetime

class Honour:

    """ Crie uma classe para representar um horario (hora, minuto e segundo). Implemente os
    métodos para fazer as operações de incremento (de segundos) no horário e diferença
entre dois horarios """

    def __init__(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def soma_segundo(self, segundos):
        time = f'{self._hours}:{self._minutes}:{self._seconds}'
        hora = datetime.strptime(time, "%H:%M:%S")
        soma = datetime.strptime(segundos, "%H:%M:%S")
        conta = hora + soma
        return conta

    @staticmethod
    def dif_honour(h1, h2):
        f1 = datetime.strptime(h1, "%H:%M:%S")
        f2 = datetime.strptime(h2, "%H:%M:%S")
        dif = f2 - f1
        return dif




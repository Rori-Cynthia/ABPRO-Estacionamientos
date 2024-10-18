class TiempoInvalidoError(Exception):
    def __init__(self, message="Las horas de permanencia deben ser mayor a 0"):
        self.message = message
        super().__init__(self.message)


class VehiculoNoEncontradoError(Exception):
    def __init__(self, message="El vehiculo indicado no está en el estacionamiento"):
        self.message = message
        super().__init__(self.message)
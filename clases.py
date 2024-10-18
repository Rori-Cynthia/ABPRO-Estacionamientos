from dataclasses import dataclass
from exceptions import TiempoInvalidoError, VehiculoNoEncontradoError

@dataclass
class Vehiculo():
    placa: str
    marca: str

    def __str__(self):
        return f"Vehiculo marca {self.marca} - Placa {self.placa}"


@dataclass   
class Automovil(Vehiculo):
    tarifa_por_hora: float = 2.0

    def calcular_tarifa(self, tiempo_permanencia: int):
        tarifa = tiempo_permanencia * self.tarifa_por_hora
        return tarifa
    

@dataclass
class Motocicleta(Vehiculo):
    tarifa_por_hora: float = 1.0

    def calcular_tarifa(self, tiempo_permanencia: int):
        tarifa = tiempo_permanencia * self.tarifa_por_hora
        return tarifa


class Estacionamiento:
    vehiculos: list[Vehiculo]

    def __init__(self):
        self.vehiculos = []

    def registrar_vehiculo(self, nuevo_vehiculo: Vehiculo):
        self.vehiculos.append(nuevo_vehiculo)

    def calcular_tarifa(self, vehiculo: Vehiculo, tiempo_permanencia: int):
        if vehiculo not in self.vehiculos:
            raise VehiculoNoEncontradoError()
        if tiempo_permanencia <= 0:
            raise TiempoInvalidoError()
        tarifa_total = vehiculo.calcular_tarifa(tiempo_permanencia)
        return tarifa_total
    

@dataclass 
class Recibo():
    vehiculo: Vehiculo
    tiempo: int
    total: float

    def __str__(self):
        return f"Recibo:\n{str(self.vehiculo)}\nTiempo: {self.tiempo} horas\nTotal a pagar: ${self.total}"

try:
    # Crear instancia de Automóvil
    auto = Automovil(placa="ABC123", marca="Toyota", tarifa_por_hora=2)
    # Registrar automóvil en el estacionamiento
    estacionamiento = Estacionamiento()
    estacionamiento.registrar_vehiculo(auto)
    # Calcular tarifa para un tiempo válido
    tiempo = 3 # Horas
    tarifa = estacionamiento.calcular_tarifa(auto, tiempo)
    print(f"Tarifa calculada: {tarifa}")
    # Generar recibo
    recibo = Recibo(vehiculo=auto, tiempo=tiempo, total=tarifa)
    print(recibo)
except TiempoInvalidoError as e:
    print(f"Error: {e}")
except VehiculoNoEncontradoError as e:
    print(f"Error: {e}")
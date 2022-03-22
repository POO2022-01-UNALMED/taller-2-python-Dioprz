class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        expected_colors = ['rojo', 'verde', 'amarillo', 'negro', 'blanco']
        if color in expected_colors:
            self.color = color

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        númeroAsientos = 0
        for i in self.asientos:
            if type(i) == type(Asiento('negro',100,123):
                númeroAsientos += 1
        return númeroAsientos

    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        for i in self.asientos:
            if type(i) == type(Asiento('negro',100,123)):
                if i.registro != self.registro:
                    return "Las piezas no son originales"
        return "Auto original"

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        valid_type = ['electrico', 'gasolina']
        if tipo in valid_type:
            self.tipo = tipo

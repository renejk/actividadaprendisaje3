from cliente import Cliente
from pago import Pago
from producto import Producto


class Factura:
    _numero: int
    _nit: str
    _razon_social: str
    _cliente: Cliente
    _detalles: list[Producto]
    _pagos: list[Pago]  

    # constructor sin parametros
    def __init__(self):
        self._numero = 0
        self._nit = ""
        self._razon_social = ""
        self._cliente = Cliente()
        self._detalles = []
        self._pagos = []

    def __init__(self, numero, nit, razon_social, cliente,detalles):
        self._numero = numero
        self._nit = nit
        self._razon_social = razon_social
        self._cliente = cliente
        self._detalles = detalles
        self._pagos = []

  

    def imprimir(self):
        print("-" * 90)
        print(f"Factura No: {self.numero}             NIT: {self.nit}      Razón Social: {self.razon_social}     ")
        print("-" * 90)
        print(f"Identificacion: {self.cliente.id}        Tipo: {self.cliente.tipo}        Direccion: {self.cliente.direccion}        Telefono: {self.cliente.telefono}")
        print(f"Nombre: {self.cliente.nombre}")
        print(f"Direccion: {self.cliente.direccion}")
        print(f"Telefono: {self.cliente.telefono}")
        print("-" * 90)
        print(f"Código | Detalle                        | Valor       | Unidad| Subtotal")
        print("-" * 90)
        for detalle in self.detalles:
            print(f"{detalle.codigo:6} | {detalle.detalle:<30} | ${detalle.precio:<10.2f} | {detalle.cantidad:<5} | ${detalle.calcular_subtotal():<10.2f}")
        print("-" * 90)
        print(f"Total                                                           ${self.calcular_total():<10.2f}")

        for pago in self.pagos:
            print(pago.mostrar_pago())

    def calcular_total(self):
        total = 0
        for detalle in self.detalles:
            total += detalle.calcular_subtotal()
        return total
    
    def agregar_pago(self, pago):
        self.pagos.append(pago)

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        self._numero = value

    @property
    def nit(self):
        return self._nit

    @nit.setter
    def nit(self, value):
        self._nit = value

    @property
    def razon_social(self):
        return self._razon_social

    @razon_social.setter
    def razon_social(self, value):
        self._razon_social = value

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, value):
        self._cliente = value

    @property
    def detalles(self):
        return self._detalles

    @detalles.setter
    def detalles(self, value):
        self._detalles = value

    

    @property
    def pagos(self):
        return self._pagos

    @pagos.setter
    def pagos(self, value):
        self._pagos = value

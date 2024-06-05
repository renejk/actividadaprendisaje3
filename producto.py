class Producto:
    _codigo: int
    _detalle: str
    _precio: float
    _cantidad: int
    _subtotal: float

    # constructor sin parametros
    def __init__(self):
        self._codigo = 0
        self._detalle = ""
        self._precio = 0
        self._cantidad = 0
        self._subtotal = 0

    # constructor con parametros
    def __init__(self, codigo, nombre, precio, cantidad):
        self._codigo = codigo
        self._detalle = nombre
        self._precio = precio
        self._cantidad = cantidad
        self._subtotal = precio * cantidad

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @property
    def detalle(self):
        return self._detalle

    @detalle.setter
    def detalle(self, value):
        self._detalle = value

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        self._precio = value

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, value):
        self._cantidad = value

    @property
    def subtotal(self):
        return self._subtotal

    @subtotal.setter
    def subtotal(self, value):
        self._subtotal = value

    def calcular_subtotal(self):
        return self.precio * self.cantidad

    


    
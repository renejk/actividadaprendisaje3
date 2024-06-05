class Pago:
    _monto: float
    _fecha: str
    _tipo: str
    def __init__(self, monto, fecha, tipo):
        self._monto = monto
        self._fecha = fecha
        self._tipo = tipo
        

    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, value):
        self._monto = value

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        self._fecha = value

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value


   
    def mostrar_pago(self):
        return f"Pago: Tipo: {self.tipo}, Fecha: {self.fecha}, Valor: ${self.monto}"

   



class PagoDebito(Pago):
    _cuenta_debito: str
    def __init__(self, monto, fecha, cuenta_debito):
        super().__init__(monto, fecha, "Tarjeta de Debito")
        self._cuenta_debito = cuenta_debito
        


    @property
    def cuenta_debito(self):
        return self._cuenta_debito

    @cuenta_debito.setter
    def cuenta_debito(self, value):
        self._cuenta_debito = value
    
    def mostrar_pago(self):
        return f"Pago: Tipo: {self.tipo}, Fecha: {self.fecha}, Valor: ${self.monto}, Cuenta: {self.cuenta_debito}"


class PagoCredito(Pago):
    _cuenta_credito: str
    _cuotas: int
    _codigo_seguridad: int
    def __init__(self, monto, fecha, cuenta_credito, cuotas, codigo_seguridad):
        super().__init__(monto, fecha, "Tarjeta de Credito")
        self._cuenta_credito = cuenta_credito
        self._cuotas = cuotas
        self._codigo_seguridad = codigo_seguridad

    @property
    def cuenta_credito(self):
        return self._cuenta_credito

    @cuenta_credito.setter
    def cuenta_credito(self, value):
        self._cuenta_credito = value

    @property
    def cuotas(self):
        return self._cuotas

    @cuotas.setter
    def cuotas(self, value):
        self._cuotas = value

    @property
    def codigo_seguridad(self):
        return self._codigo_seguridad

    @codigo_seguridad.setter
    def codigo_seguridad(self, value):
        self._codigo_seguridad = value

    def mostrar_pago(self):
        return f"Pago: Tipo: {self.tipo}, Fecha: {self.fecha}, Valor: ${self.monto}, Cuenta: {self.cuenta_credito}, Cuotas: {self.cuotas}, Codigo de Seguridad: {self.codigo_seguridad}"


class PagoEfectivo(Pago):
  
    def __init__(self, monto, fecha):
        super().__init__(monto, fecha, "Efectivo")

    def mostrar_pago(self):
        return f"Pago: Tipo: {self.tipo}, Fecha: {self.fecha}, Valor: ${self.monto}"
     
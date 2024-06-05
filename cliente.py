class Cliente:
    _id: int
    _nombre: str
    _direccion: str
    _telefono: str
    _tipo: str

    # constructor sin parametros
    def __init__(self):
        self._id = 0
        self._nombre = ""
        self._direccion = ""
        self._telefono = ""
        self._tipo = ""

    # constructor con parametros
    def __init__(self, id, nombre, direccion, telefono, tipo):
        self._id = id
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._tipo = tipo

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, value):
        self._direccion = value

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, value):
        self._telefono = value

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value

class Comprador:
    def __init__(self, cpf, name, email, id=None):
        self.cpf = cpf
        self.name = name
        self.email = email
        self.id = id

    def BuscarCompradores():
        pass

@property
def cpf(self):
    return self.__cpf

@cpf.setter
def cpf(self, valor):
    if valor is None or not valor.strip():
        raise ValueError("Não pode ser nulo ou em branco")

    self.__cpf = valor



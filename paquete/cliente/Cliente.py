class Cliente():
    contadorId = 0

    def __init__(self, nombre, email, telefono):
        Cliente.contadorId += 1
        self.__id = Cliente.contadorId
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono

    def __str__(self):
        return f"Cliente: {self.__nombre}\nID: {self.__id}"

    def getDatos(self):
        print(f"El cliente {self.__nombre} con ID: {self.__id} tiene la siguiente informacion: \nEmail: {self.__email} \nTelefono: {self.__telefono}")

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setEmail(self, email):
        self.__email = email

    def setTelefono(self, telefono):
        self.__telefono = telefono





from cliente import Cliente

Cliente1 = Cliente.Cliente("Panchito", "cliente@coder.com", "55135")
print(Cliente1)
Cliente1.getDatos()

Cliente1.setNombre("Pancho")
Cliente1.setEmail("panchito@coder.com")
Cliente1.setTelefono("5513542468")
Cliente1.getDatos()

Cliente2 = Cliente.Cliente("Juan", "juanito@coder.com", "1234567890")
Cliente2.getDatos()
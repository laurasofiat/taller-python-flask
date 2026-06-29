#PROGRAMACION ORIENTADA A OBJETOS POO --------------------------------------------------------------------------

class persona: #clase persona
    def __init__(self, edad, nombre, apellido):  #contruye
        self.edad = edad #se define variable edad
        self.nombre = nombre
        self.apellido = apellido

    def info(self): #funcion info
        return f"{self.edad}, {self.nombre}, {self.apellido}" #devuelve en impresion edad y nombre

class producto: #clase producto
    def __init__(self, nomp, preciop): #contruye
        self.nomp = nomp 
        self.preciop = preciop

    def info(self): #funcion info
        return f"{self.nomp}, {self.preciop}" #devuelve nombre del proucto y precio del producto


class empleado(persona):
    def __init__(self, edad, nombre, apellido, horario, cargo, salario):
        super().__init__(edad, nombre, apellido)
        self.horario = horario
        self.cargo = cargo
        self.salario = salario
 
    def realizar_venta(self):
        return f"El empleado {self.nombre} ha realizado una venta"
 
    def atender_clientes(self):
        return f"El empleado {self.nombre} está atendiendo clientes"
 
    def info(self):
        return f"{self.edad}, {self.nombre}, {self.apellido}, {self.horario}, {self.cargo}, {self.salario}"
 
 
class administrador(persona):
    def __init__(self, edad, nombre, apellido):
        super().__init__(edad, nombre, apellido)
 
    def organizar_roles(self):
        return f"El administrador {self.nombre} ha organizado los roles"
 
    def atender_clientes(self):
        return f"El administrador {self.nombre} está atendiendo clientes"
 
    def info(self):
        return f"{self.edad}, {self.nombre}, {self.apellido}"
 
 
class cliente(persona):
    def __init__(self, edad, nombre, apellido, direccion, telefono, cedula, codigo_cliente):
        super().__init__(edad, nombre, apellido)
        self.direccion = direccion
        self.telefono = telefono
        self.cedula = cedula
        self.codigo_cliente = codigo_cliente
 
    def realizar_compra(self):
        return f"El cliente {self.nombre} ha realizado una compra"
 
    def info(self):
        return f"{self.edad}, {self.nombre}, {self.apellido}, {self.direccion}, {self.telefono}, {self.cedula}, {self.codigo_cliente}"
 
 
class venta:
    def __init__(self, hora_venta, dia_venta, mes_venta, ano_venta, cantidad_vendida):
        self.hora_venta = hora_venta
        self.dia_venta = dia_venta
        self.mes_venta = mes_venta
        self.ano_venta = ano_venta
        self.cantidad_vendida = cantidad_vendida
 
    def calcular_total(self):
        return "La venta ha calculado el total"
 
    def generar_factura(self):
        return "La venta ha generado la factura"
 
    def info(self):
        return f"{self.hora_venta}, {self.dia_venta}, {self.mes_venta}, {self.ano_venta}, {self.cantidad_vendida}"
 
 
class inventario:
    def __init__(self, lista_prenda_ropa):
        self.lista_prenda_ropa = lista_prenda_ropa
 
    def generar_reporte(self):
        return "El inventario ha generado un reporte"
 
    def info(self):
        return f"{self.lista_prenda_ropa}"
 
 
class factura:
    def __init__(self, cliente, venta, producto):
        self.cliente = cliente
        self.venta = venta
        self.producto = producto
 
    def prueba_factura(self):
        return "La factura se generó"
 
    def info(self):
        return f"{self.cliente.info()}, {self.venta.info()}, {self.producto.info()}"
 
 
# datos definidos-----------------------------------------------------------------
 
mi_empleado = empleado(30, "Carlos", "Ramirez", "8am-5pm", "Vendedor", 1500000)
mi_administrador = administrador(45, "Laura", "Gomez")
mi_cliente = cliente(25, "Juan", "Perez", "Calle 123", "3001234567", "1020304050", "C001")
mi_producto = producto("Camiseta", 45000)
mi_venta = venta("10:30", 29, "Junio", 2026, 3)
mi_inventario = inventario(["Camiseta", "Pantalon", "Chaqueta"])
mi_factura = factura(mi_cliente, mi_venta, mi_producto)
 
# impresiones-----------------------------

print(f"Empleado: \n {mi_empleado.info()} \n {mi_empleado.realizar_venta()} \n {mi_empleado.atender_clientes()}")
 
print(f"Administrador: \n {mi_administrador.info()} \n {mi_administrador.organizar_roles()} \n {mi_administrador.atender_clientes()}")
 
print(f"Cliente: \n {mi_cliente.info()} \n {mi_cliente.realizar_compra()}")
 
print(f"Producto: \n {mi_producto.info()}")
 
print(f"Veneta: \n {mi_venta.info()} \n {mi_venta.calcular_total()} \n {mi_venta.generar_factura()}")
 
print(f"Inventario: \n {mi_inventario.info()} \n {mi_inventario.generar_reporte()}")
 
print(f"Factura: \n {mi_factura.info()} \n {mi_factura.prueba_factura()}")



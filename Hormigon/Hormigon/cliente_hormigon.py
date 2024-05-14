import sqlite3

class ClienteHormigon:
    def __init__(self, nombre, apellido, telefono, direccion_obra, localidad, km_planta_obra):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion_obra = direccion_obra
        self.localidad = localidad
        self.km_planta_obra = km_planta_obra

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nTeléfono: {self.telefono}\nDirección de obra: {self.direccion_obra}\nLocalidad: {self.localidad}\nKilómetros de la planta a la obra: {self.km_planta_obra}"
    
    
    def guardar_en_bd(self):
        conexion = sqlite3.connect('clientes.db')
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO clientes VALUES (?, ?, ?, ?, ?, ?)',
                       (self.nombre, self.apellido, self.telefono, self.direccion_obra, self.localidad, self.km_planta_obra))
        conexion.commit()
        conexion.close()

    @staticmethod
    def obtener_clientes():
        conexion = sqlite3.connect('clientes.db')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM clientes')
        clientes = cursor.fetchall()
        conexion.close()
        return clientes
    
    

# 1)Crear un Detector de palíndromos. Un palíndromo es una palabra o frase que se lee igual
# de derecho y del revés Ej anita lava la tina, neuquen, etc

# def esPalindromo(palabra:str) -> bool:
#     return True if palabra.lower() == palabra[::-1].lower() else False

# print(esPalindromo('ana'))





# 2)Dada una cadena que contiene solo los caracteres "(" y ")", implementa una función
# que determina si los paréntesis están correctamente balanceados. Un conjunto de
# paréntesis está equilibrado si:
    
# ● Cada paréntesis de apertura tiene un paréntesis de cierre correspondiente.
# ● Los paréntesis de apertura se cierran en el orden correcto.

# def parentBalanceados(cadena:str) -> bool:
#     if '(' and ')' in cadena:
#         if '(' in cadena[0] and cadena.endswith(')'):
#             return True
#         return False
#     return False

# print(parentBalanceados('()'))



# 3)Una oficina de atención al cliente tiene una cola de personas esperando para ser
# atendidas. Implementa un programa que:
# ● Agregue clientes a la cola cuando lleguen.
# ● Atienda a los clientes en el orden en que llegaron.
# ● Permite consultar cuántos clientes quedan en la cola.

# class Cola:
#     def __init__(self):
#         self.clientes = []
    
#     def agregar_cliente(self, cliente:str):
#         try:
#             self.clientes.append(cliente.capitalize())
#             print(f'{cliente.capitalize()} agregado a la fila ✔')
#         except TypeError as e:
#             print(f'{e}: el nombre no es una cadena')
            
#     def cantidad_clientes(self):
#         print(f'\nCantidad de clientes en la fila {len(self.clientes)}, el primero en ser atendido será {self.clientes[0]}')
        
# cola_negocio = Cola()

# cola_negocio.agregar_cliente('Tiziano')
# cola_negocio.agregar_cliente('pEpe')
# cola_negocio.agregar_cliente('kukelme')

# cola_negocio.cantidad_clientes()




# 4)En un cine, se dispone de 70 butacas distribuidas en 7 filas con 10 columnas cada una. El
# objetivo es desarrollar un sistema de turnero que permita visualizar un mapa interactivo de
# las butacas, mostrando cuáles están vacías y cuáles han sido reservadas .
# Al momento de reservar un asiento , el sistema debe registrar el nombre y el teléfono del
# cliente, y marcar el asiento como ocupado o reservado en el mapa. Además, se debe
# proporcionar la funcionalidad de consultar la información del cliente que ha reservado un
# lugar específico, permitiéndole ver sus datos de contacto .


class Cine:
    def __init__(self, filas=7, columnas=10):
        self.filas = filas
        self.columnas = columnas
        self.asientos = [[{'reservado': False, 'cliente': None} for _ in range(columnas)] for _ in range(filas)]
    
    def mostrar_mapa(self):
        for fila in self.asientos:
            print(" ".join(['R' if asiento['reservado'] else 'V' for asiento in fila]))
    
    def reservar_asiento(self, fila, columna, nombre, telefono):
        if not self.asientos[fila][columna]['reservado']:
            self.asientos[fila][columna] = {'reservado': True, 'cliente': {'nombre': nombre, 'telefono': telefono}}
            print(f"Se ha reservado el asiento ({fila+1},{columna+1}) para {nombre}.")
        else:
            print(f"El asiento ({fila+1},{columna+1}) ya está reservado.")
    
    def consultar_reserva(self, fila, columna):
        asiento = self.asientos[fila][columna]
        if asiento['reservado']:
            cliente = asiento['cliente']
            print(f"Asiento reservado por {cliente['nombre']}. Teléfono: {cliente['telefono']}")
        else:
            print(f"El asiento ({fila+1},{columna+1}) está vacío.")

# Ejemplo de uso
cine = Cine()
cine.mostrar_mapa()
cine.reservar_asiento(0, 1, 'Juan Pérez', '123456789')
cine.mostrar_mapa()
cine.consultar_reserva(0, 1)

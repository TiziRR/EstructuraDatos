class Alumno:
    def __init__(self, nombre: str, edad: int, fecha_nacimiento: str, matricula: int):
        self.nombre = nombre.capitalize()
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.matricula = matricula
        self.cuota_mensual = self.matricula + 1000
        
    def __str__(self):
        descuento = 3000 * 15 / 100
        return f'\n{'=' * 34}\n{'=' * 8} Datos de ingreso {'=' * 8}\n{'=' * 34}\nNombre completo: {self.nombre}\nFecha de Nacimiento y edad: {self.fecha_nacimiento} ({self.edad})\nPosee titulo?: {True}\nMatricula: {self.matricula}\nCuota mensual: {self.cuota_mensual}\nArancel mensual materia: Python I: {3000}\nArancel mensual con descuento: {3000 - descuento}'

class Notas(Alumno):
    def __init__(self, nombre, primer_nota, segunda_nota):
        Alumno.__init__(self, nombre, edad, fecha_nacimiento, matricula)
        self.primer_nota = primer_nota
        self.segunda_nota = segunda_nota
        
    def __str__(self):
        __promedio = (self.primer_nota + self.segunda_nota) / 2
        
        __mejora = ''
        if self.primer_nota > self.segunda_nota:
            __mejora = 'Empeoró su desempeño'
        elif self.primer_nota == self.segunda_nota:
            __mejora = 'Mantuvo la nota'
        else:
            __mejora = 'Mejoró su desempeño'
        
        __promociono = ''
        if __promedio >= 7:
            __promociono = 'Promocionó la materia'
        elif __promedio >= 4:
            __promociono = 'Debe rendir examén final'
        else:
            __promociono = 'Debe recursar'
            
        return f'\n{'=' * 25}\n{'=' * 8} {self.nombre} {'=' * 8}\n{'=' * 25}\n\nEl promedio de las notas es: {__promedio}\n{'Aprobó el segundo parcial' if self.segunda_nota > 7 else 'Desaprobó el segundo parcial'}\nProgreso del 1er al 2do parcial: {__mejora}\n{__promociono}'

class Aulas(Alumno):
    def __init__(self, dia: int, turno: str, cant_materias: int, vehiculo: str):
        Alumno.__init__(self, nombre, edad, fecha_nacimiento, matricula)
        self.dia = dia
        self.turno = turno.capitalize()
        self.cant_materias = cant_materias
        self.vehiculo = vehiculo.capitalize()
    
    def aula(self):
        return 'Aula: A-315' if self.dia % 2 == 0 else 'Aula: A-300'

    def descuento(self):
        if self.turno == 'Tarde' and self.cant_materias >= 3:
            desc_tarde = self.cuota_mensual - (self.cuota_mensual * 0.25)
            return f'El valor de la cuota es: {desc_tarde}'
        else:
            desc_otro = self.cuota_mensual - (self.cuota_mensual * 0.25)
            return f'El valor de la cuota es: {desc_otro}'

    def estacionamiento(self):
        if self.vehiculo == 'Auto' or self.vehiculo == 'Moto':
            return f'El costo del estacionamiento para {self.vehiculo} es: 300'
        else:
            return f'El costo del estacionamiento para {self.vehiculo} es: 50'

    def __str__(self):
        return f'\n{self.aula()}\n{self.descuento()}\n{self.estacionamiento()}'


print(f"\n{'=' * 55}")
print(f"{'=' * 8} Universidad de Python - Inscripciones {'=' * 8}")
print(f"{'=' * 55}")

nombre = input('\nIngrese su nombre completo: ')

contador_err = 0
while True:
    edad = int(input('Ingrese su edad: '))
    if edad < 18:
        print('Edad invalida ❌')
        contador_err += 1
    else:
        print(f'Edad válida ✔\nUsted se equivocó {contador_err} veces')
        break

fecha_nacimiento = input('Ingrese su fecha de nacimiento: ')
matricula = int(input('Ingrese monto de la matricula: '))

Alumno1 = Alumno(nombre, edad, fecha_nacimiento, matricula)

print(Alumno1)

nota_uno = int(input('\nIngresar la nota del primer parcial: '))
nota_dos = int(input('Ingresar la nota del segundo parcial: '))
notas = Notas(Alumno1.nombre, nota_uno, nota_dos)

print(notas)

dia = int(input('\nIngrese el día teniendo en cuenta que el 1 es el Lunes y el 6 el sábado: '))
turno = input('Ingrese el turno: ')
cant_materias = int(input('Ingrese la cantidad de materias: '))
vehiculo = input('Ingrese el vehiculo en el que ingresa (Auto, Moto o Bicicleta): ')

print(f'\n{'=' * 20} Listado de Aulas {'=' * 20}')
for i in range(7):
    if i == 0:
        print(f'Día\tAula')
    elif i % 2 == 0:
        print(f'{i}\tA-315')
    else:
        print(f'{i}\tA-300')

aula1 = Aulas(dia, turno, cant_materias, vehiculo)

print(aula1)

print(f'\n{'=' * 20} Promedio de notas {'=' * 20}')
notas = []
rango = 5
for _ in range(rango):
    nota = int(input('Ingresar notas: '))
    notas.append(nota)
    resultado = sum(notas) / 5
print(f'El promedio de las notas es: {resultado}')

print(f'\n{'=' * 20} Costo del Comedor {'=' * 20}')
for ind in range(7):
    if ind == 0:
        print(f'Día\tCosto')
    else:
        print(f'{ind}\t${1250 * ind}')

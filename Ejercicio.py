# Esta clase representa un ejercicio individual y contiene información básica sobre el tipo de ejercicio, la duración y otros detalles.
class Ejercicio():
    def __init__(self, nombre, grupo_muscular, nivel_dificultad, repeticiones, series):
        self.nombre = nombre
        self.grupo_muscular = grupo_muscular
        self.nivel_dificultad = nivel_dificultad
        self.repeticiones = repeticiones
        self.series = series

    def mostrar_informacion(self):
        print('############################')
        print("NOMBRE: " + self.nombre)
        print("GRUPO MUSCULAR: " + self.grupo_muscular)
        print("NIVEL DE DIFICULTAD: " + self.nivel_dificultad)
        print("REPETICIONES: " + str(self.repeticiones))
        print("SERIES: " + str(self.series))
        print('############################')
        print("\n")

    # Evaluar la dificultad
    def es_apto_para(self, nivel_usuario):
        niveles = ["Principiante", "Intermedio", "Avanzado"]
        if niveles.index(nivel_usuario) >= niveles.index(self.nivel_dificultad):
            return True
        return False

    # Incrementar repeticiones y/o series
    def incrementar_intensidad(self, incremento_repeticiones=0, incremento_series=0):
        self.repeticiones += incremento_repeticiones
        self.series += incremento_series


    
ejercicio1 = Ejercicio("Flexiones", "Pectorales", "Intermedio", 10, 3)
ejercicio2 = Ejercicio("Sentadillas", "Piernas", "Principiante", 15, 3)
ejercicio3 = Ejercicio("Plancha", "Abdominales", "Avanzado", 1, 3)
ejercicio4 = Ejercicio("Dominadas", "Espalda", "Avanzado", 10, 3)
ejercicio5 = Ejercicio("Curl de Bíceps", "Bíceps", "Intermedio", 10, 3)
ejercicio6 = Ejercicio("Press de banca", "Pectorales", "Avanzado", 12, 4)
ejercicio7 = Ejercicio("Fondos de triceps", "Tríceps", "Intermedio", 12, 3)
ejercicio8 = Ejercicio("Remo con barra", "Espalda", "Avanzado", 10, 4)
ejercicio9 = Ejercicio("Extensión de pierna", "Cuádriceps", "Principiante", 15, 3)
ejercicio10 = Ejercicio("Curl de pierna", "Isquiotibiales", "Principiante", 15, 3)
ejercicio11 = Ejercicio("Elevaciones laterales", "Hombros", "Intermedio", 12, 3)
ejercicio12 = Ejercicio("Press militar", "Hombros", "Avanzado", 10, 4)
ejercicio13 = Ejercicio("Crunch abdominal", "Abdominales", "Principiante", 20, 3)
ejercicio14 = Ejercicio("Burpees", "Cuerpo completo", "Avanzado", 15, 4)
ejercicio15 = Ejercicio("Escaladores", "Abdominales", "Intermedio", 20, 3)
ejercicio16 = Ejercicio("Sentadilla búlgara", "Piernas", "Intermedio", 12, 3)
ejercicio17 = Ejercicio("Peso muerto", "Espalda baja", "Avanzado", 10, 3)
ejercicio18 = Ejercicio("Zancadas", "Piernas", "Intermedio", 12, 3)
ejercicio19 = Ejercicio("Press de hombro con mancuernas", "Hombros", "Intermedio", 10, 3)
ejercicio20 = Ejercicio("Russian Twist", "Abdominales", "Intermedio", 20, 3)

todos_ejercicios = [ejercicio1, ejercicio2, ejercicio3, ejercicio4, ejercicio5, ejercicio6, ejercicio7, ejercicio8, ejercicio9, ejercicio10, ejercicio11, ejercicio12, ejercicio13, ejercicio14, ejercicio15, ejercicio16, ejercicio17, ejercicio18, ejercicio19, ejercicio20]

for ejercicio in todos_ejercicios:
    ejercicio.mostrar_informacion()

# Evaluar la dificultad
print("Apto para principiante?: ", ejercicio1.es_apto_para('Principiante'))
print('Apto para intermedio?: ', ejercicio1.es_apto_para('Intermedio'))
print('Apto para avanzado?: ', ejercicio1.es_apto_para('Avanzado'))

# Incrementar intensidad
print("\n########################\nEjercicio sin cambiar:")
ejercicio1.mostrar_informacion()

ejercicio1.incrementar_intensidad(incremento_repeticiones=2, incremento_series=1)

print("########################\nEjercicio cambiado:")
ejercicio1.mostrar_informacion()
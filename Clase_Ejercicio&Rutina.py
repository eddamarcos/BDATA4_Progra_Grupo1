
class Ejercicio():
    def __init__(self, nombre_ejercicio, grupo_muscular, nivel_dificultad, repeticiones, series):
        self.nombre_ejercicio = nombre_ejercicio
        self.grupo_muscular = grupo_muscular
        self.nivel_dificultad = nivel_dificultad
        self.repeticiones = repeticiones
        self.series = series

    def mostrar_informacion(self):
     
        print("NOMBRE: " + self.nombre_ejercicio)
        print("GRUPO MUSCULAR: " + self.grupo_muscular)
        print("NIVEL DE DIFICULTAD: " + self.nivel_dificultad)
        print("REPETICIONES: " + str(self.repeticiones))
        print("SERIES: " + str(self.series))
       
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


class Rutina(Ejercicio):

    def __init__(self, nombre_rutina, grupo_muscular, nivel_dificultad, repeticiones, series, objetivo, nivel_rutina):
        # Llamada a __init__ de la clase base (Ejercicio)
        super().__init__(nombre_rutina, grupo_muscular, nivel_dificultad, repeticiones, series)

        # Atributos de Rutina  
        self.objetivo = objetivo
        self.nivel_rutina = nivel_rutina
    

        self.lista_ejercicios = []

    def agregar_ejercicio(self, ejercicio):
   
        self.lista_ejercicios.append(ejercicio)

    def remover_ejercicio(self, nombre):

        for ejercicio_ in self.lista_ejercicios:
            if ejercicio_.nombre_ejercicio == nombre:
                self.lista_ejercicios.remove(ejercicio_)
                break
        else:
            print("Ese ejercicio no se encuentra en la rutina.")

    def mostrar_rutina(self):
 
        print('############################')
        print(f"     ** RUTINA: {self.nombre_ejercicio} **")
        print('----------------------------')
        print(f"   Objetivo: {self.objetivo}")
        print(f"   Nivel de la Rutina: {self.nivel_rutina}")
        print('----------------------------')
        print("   Ejercicios en la rutina:")
        print('============================')
        for ejercicio in self.lista_ejercicios:
            ejercicio.mostrar_informacion()

        print('############################\n')


# Crear una rutina como un tipo de Ejercicio
rutina = Rutina(
    nombre_rutina="Rutina de Fuerza", 
    grupo_muscular="Cuerpo completo", 
    nivel_dificultad="Intermedio", 
    repeticiones=0,  # Estos pueden quedar en 0 ya que no los usaremos directamente
    series=0, 
    objetivo="Ganar masa muscular", 
    nivel_rutina="Intermedio"
)

# Crear algunos ejercicios
ejercicio1 = Ejercicio("Flexiones", "Pectorales", "Intermedio", 10, 3)
ejercicio2 = Ejercicio("Sentadillas", "Piernas", "Principiante", 15, 3)

# Agregar ejercicios a la rutina
rutina.agregar_ejercicio(ejercicio1)
rutina.agregar_ejercicio(ejercicio2)

# Mostrar la rutina completa con los ejercicios
rutina.mostrar_rutina()

# Prueba de remover un ejercicio y mostrar la rutina actualizada
rutina.remover_ejercicio("Sentadillas")
rutina.mostrar_rutina()

class Exercise():
    def __init__(self, exercise_name, grupo_muscular, nivel_dificultad, repeticiones, series):
        self.exercise_name = exercise_name
        self.grupo_muscular = grupo_muscular
        self.nivel_dificultad = nivel_dificultad
        self.repeticiones = repeticiones
        self.series = series

    def mostrar_informacion(self):
     
        print("NOMBRE: " + self.exercise_name)
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


    
ejercicio1 = Exercise("Flexiones", "Pectorales", "Intermedio", 10, 3)
ejercicio2 = Exercise("Sentadillas", "Piernas", "Principiante", 15, 3)
ejercicio3 = Exercise("Plancha", "Abdominales", "Avanzado", 1, 3)
ejercicio4 = Exercise("Dominadas", "Espalda", "Avanzado", 10, 3)
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

class Routine(Exercise):
    """
    Represents a workout routine composed of multiple exercises targeting a muscle group
    with a specific objective and difficulty level.
    """

    def __init__(self, routine_name, muscle_group, difficulty_level, repetitions, sets, goal, routine_level):
        # Calls the __init__ method of the base class (Exercise)
        super().__init__(routine_name, muscle_group, difficulty_level, repetitions, sets)

        # Routine attributes
        self.goal = goal
        self.routine_level = routine_level

        self.exercise_list = []

    def add_exercise(self, exercise):
        """
        Adds an exercise to the routine.

        Args:
            exercise (Exercise): The exercise to add to the routine.
        """
        self.exercise_list.append(exercise)

    def remove_exercise(self, name):
        """
        Removes an exercise from the routine by name.

        Args:
            name (str): The name of the exercise to remove.

        If the exercise is not found, displays an informative message.
        """
        for exercise_ in self.exercise_list:
            if exercise_.exercise_name == name:
                self.exercise_list.remove(exercise_)
                break
        else:
            print("This exercise is not in the routine.")

    def show_routine(self):
        """
        Displays the complete routine, including its goal, difficulty level,
        and a list of exercises.
        """
        print('############################')
        print(f"     ** ROUTINE: {self.exercise_name} **")
        print('----------------------------')
        print(f"   Goal: {self.goal}")
        print(f"   Routine Level: {self.routine_level}")
        print('----------------------------')
        print("   Exercises in the routine:")
        print('============================')
        for exercise in self.exercise_list:
            exercise.show_info()

        print('############################\n')


# Create a routine as a type of Exercise
routine = Routine(
    routine_name="Strength Routine", 
    muscle_group="Full Body", 
    difficulty_level="Intermediate", 
    repetitions=0,  # These can remain 0 as they will not be used directly
    sets=0, 
    goal="Gain muscle mass", 
    routine_level="Intermediate"
)

# Create some exercises
exercise1 = Exercise("Push-ups", "Chest", "Intermediate", 10, 3)
exercise2 = Exercise("Squats", "Legs", "Beginner", 15, 3)

# Add exercises to the routine
routine.add_exercise(exercise1)
routine.add_exercise(exercise2)

# Display the complete routine with exercises
routine.show_routine()

# Test removing an exercise and displaying the updated routine
routine.remove_exercise("Squats")
routine.show_routine()

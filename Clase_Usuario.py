class Usuario:
    def __init__(self, nombre, altura, peso, edad, genero, nivel_condicion_fisica="Principiante", objetivo="Mantenimiento"):
        """Crea un objeto de tipo Usuario con una serie de atributos como el nombre, altura, peso, edad, género, nivel de condición física y objetivo.

        Args:
            nombre (str): Nombre del usuario.
            altura (float): Altura en metros.
            peso (float): Peso en kilogramos.
            edad (int): Edad en años.
            genero (str): Género del usuario. Puede ser 'mujer' o 'hombre'.
            nivel_condicion_fisica (str, optional): Nivel de condición física del usuario. Puede ser 'Principiante', 'Intermedio' o 'Avanzado'. Defaults to "Principiante".
            objetivo (str, optional): El objetivo del usuario. Puede ser 'Perder peso', 'Ganar músculo' o 'Mantenimiento'. Defaults to "Mantenimiento".
        """
        self.nombre = nombre 
        self.altura = altura
        self.peso = peso
        self.edad = edad
        self.genero = genero.lower()
        self.nivel_condicion_fisica = nivel_condicion_fisica
        self.objetivo = objetivo

        self.actividad = None
        self.calorias_quemadas = None

        niveles_validos = ["Principiante", "Intermedio", "Avanzado"]
        objetivos_validos = ["Perder peso", "Ganar músculo", "Mantenimiento"]
        generos_validos = ["mujer", "hombre"]

        # Validación del nivel de condición física
        if nivel_condicion_fisica not in niveles_validos:
            raise ValueError(f"Nivel de condición física no es válido. Debe ser uno de: {niveles_validos}")
        if objetivo not in objetivos_validos:
            raise ValueError(f"Objetivo no válido. Debe ser uno de: {objetivos_validos}")
        if genero not in generos_validos:
            raise ValueError(f"Género no válido. Debe ser uno de: {generos_validos}")
    
    # Calcular el índice de masa corporal
    def calcular_imc(self):
        """Calcula el índice de masa corporal (IMC) del usuario.

        Returns:
            float: Indice de masa corporal del usuario.
        """
        indice_masa_corporal = round(self.peso / (self.altura ** 2), 2)
        return indice_masa_corporal
    
    # Calcular el índice de la grasa corporal
    def calcular_grasa_corporal(self):
        """Calcula el índice de grasa corporal del usuario.

        Returns:
            float: El indice de grasa corporal en porcentaje.
        """
        imc = self.calcular_imc()
        
        if self.genero == 'hombre':
            grasa_corportal_hom = 1.20 * imc + 0.23 * self.edad - 16.2
            return round(grasa_corportal_hom,2)
        elif self.genero == 'mujer':
            grasa_corporal_muj = 1.20 * imc + 0.23 * self.edad - 5.4
            return round(grasa_corporal_muj, 2)
        else:
            raise ValueError("Género no reconocido.")
        

    # Calcular la cantidad de calorías quemadas según duración, tipo y peso    
    def calorias_actividad(self, duracion, actividad):
        """Calcula la cantidad de calorías quemadas durante una actividad física.

        Args:
            duracion (float): Duración de la actividad en minutos.
            actividad (str): Nombre de la actividad física.

        Raises:
            ValueError: _description_
        """
        peso = self.peso

        # METs estimados
        met_values = {"flexiones": 4.0, "sentadillas": 5.0, "plancha": 4.0, "dominadas": 8.0, "curl de bíceps": 3.5, "press de banca": 6.0, "fondos de triceps": 6.5, "remo con barra": 7.0,
        "extensión de pierna": 3.0, "curl de pierna": 3.0, "elevaciones laterales": 3.0, "press militar": 6.5, "crunch abdominal": 3.5, "burpees": 8.0, "escaladores": 6.5, 
        "sentadilla búlgara": 5.5, "peso muerto": 7.5, "zancadas": 5.5, "press de hombro con mancuernas": 6.0, "russian twist": 4.0}
        
        met = met_values.get(actividad.lower())
        if met:
            self.actividad = actividad
            self.calorias_quemadas = met * peso * (duracion / 60)
        else:
            raise ValueError("Actividad no reconocida.")
        
    # funcion para mostrar toda la info de usuario
    def mostrar_info(self):
        """Muestra toda la información del usuario en pantalla.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Altura: {self.altura} m")
        print(f"Peso: {self.peso} kg")
        print(f"Edad: {self.edad} años")
        print(f"Género: {self.genero}")
        print(f"Nivel de condición física: {self.nivel_condicion_fisica}")
        print(f"Objetivo: {self.objetivo}")
        print(f"Índice de masa corporal: {self.calcular_imc()}")
        print(f"Grasa corporal: {self.calcular_grasa_corporal()} %")
        
        if self.calorias_quemadas is not None:
            print(f"Calorías quemadas realizando {self.actividad}: {self.calorias_quemadas:.2f} kcal")
        else:
            print("Las calorías quemadas aún no han sido calculadas.")


# Crear una instancia de Usuario
usuario = Usuario(nombre="Marta", altura=1.57, peso=43, edad=21, genero="mujer")

# Actualizar datos personales
usuario.nombre = "María"

# Calculos del usuario
imc = usuario.calcular_imc()

# Calculos grasa corporal
gr_corporal = usuario.calcular_grasa_corporal()

# Calculos de quema de calorias
# calorias = usuario.calorias_actividad(30, "a")
calorias = usuario.calorias_actividad(30, "burpees")

# Mostrar info del usuario
usuario.mostrar_info()
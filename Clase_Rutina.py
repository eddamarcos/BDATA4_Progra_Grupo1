class Ejercicio:
    def __init__(self, nombre, duracion=10, calorias_por_minuto=5.0):
        self.nombre = nombre
        self.duracion = duracion
        self.calorias_por_minuto = calorias_por_minuto

class Rutina():

    def __init__(self, nombre_rutina, objetivo, nivel):
        self.nombre_rutina = nombre_rutina
        self.objetivo = objetivo
        self.nivel = nivel


        self.lista_ejercicios =  []


    def agregar_ejercicio(self, nombre):

        ejercicio = Ejercicio(nombre) 
        self.lista_ejercicios.append(ejercicio)
    
    def remover_ejercicio(self, nombre):
        
        for ejercicio_ in self.lista_ejercicios:
            if ejercicio_.nombre == nombre:
                self.lista_ejercicios.remove(ejercicio_)
                break
            else:
                print("Ese ejercicio no se encuentra en la rutina.")

    def mostrar_rutina(self):
        
        print(f"Rutina: {self.nombre_rutina}")
        print(f"Objetivo: {self.objetivo}")
        print(f"Nivel: {self.nivel}")
        print("Ejercicios:")
        for ejercicio in self.lista_ejercicios:
            print(f" - {ejercicio.nombre} ")

rutina_test = Rutina(
    nombre_rutina="Entrenamiento Completo",
    objetivo="Mejorar la fuerza y la resistencia",
    nivel="Intermedio"
)

rutina_test.agregar_ejercicio("Burpees")
rutina_test.remover_ejercicio("Flexiones")
rutina_test.mostrar_rutina()
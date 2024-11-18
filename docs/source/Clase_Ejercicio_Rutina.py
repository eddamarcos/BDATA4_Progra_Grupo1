class Exercise:
    """
    Class representing an individual exercise, containing basic information about the exercise type, difficulty, and other details.
    
    Contains the following attributes:
    - exercise_name: Exercise name
    - muscle_group: Muscle group targeted by the exercise
    - difficulty_level: Difficulty level of the exercise (Beginner, Intermediate, Advanced)
    - repetitions: Number of repetitions per set
    - sets: Number of sets of the exercise

    Contains the following methods:
    - show_information: Displays the information about the exercise
    - is_suitable_for: Evaluates if the exercise is suitable for a user with a given difficulty level
    - increase_intensity: Increases the number of repetitions and/or sets of the exercise
    """
    def __init__(self, exercise_name, muscle_group, difficulty_level, repetitions, sets):
        """Method to initialize an exercise with the necessary attributes.

        Args:
            exercise_name (str): Name of the exercise
            muscle_group (str): Involved muscle group
            difficulty_level (str): Difficulty level of the exercise
            repetitions (int): Number of repetitions
            sets (int): Number of sets
        """
        self.exercise_name = exercise_name
        self.muscle_group = muscle_group
        self.difficulty_level = difficulty_level
        self.repetitions = repetitions
        self.sets = sets

    def show_information(self):
        """
        Method that displays the information about the exercise.
        """
        print('############################')
        print("NAME: " + self.exercise_name)
        print("MUSCLE GROUP: " + self.muscle_group)
        print("DIFFICULTY LEVEL: " + self.difficulty_level)
        print("REPETITIONS: " + str(self.repetitions))
        print("SETS: " + str(self.sets))
        print('############################')
        print("\n")

    def is_suitable_for(self, user_level):
        """
        Method to evaluate if the exercise is suitable for a user with a given difficulty level.

        Args:
            user_level (str): User's knowledge level (Beginner, Intermediate, Advanced)

        Returns:
            Boolean: Returns true if the user can perform the exercise given their level, false otherwise.
        """
        levels = ["Beginner", "Intermediate", "Advanced"]
        if levels.index(user_level) >= levels.index(self.difficulty_level):
            return True
        return False

    def increase_intensity(self, repetitions_increase, sets_increase):
        """
        Method to increase the number of repetitions and/or sets of the exercise.

        Args:
            repetitions_increase (int): The number of repetitions to add to the initial value.
            sets_increase (int): The number of sets to add to the initial value.
        """
        self.repetitions += repetitions_increase
        self.sets += sets_increase

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
            exercise.show_information()

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

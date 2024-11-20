from Class_exercise_routine import Exercise, Routine 
from Class_user import User 

# CLASS EXERCISE AND ROUTINE

# Create the first exercise
exercise_1 = Exercise(
    exercise_name = "Push-up", 
    muscle_group = "Chest", 
    difficulty_level = "Intermediate", 
    repetitions = 15, 
    sets = 3
)

exercise_2 = Exercise(
    exercise_name="Squats", 
    muscle_group = "Legs", 
    difficulty_level = "Beginner", 
    repetitions = 15, 
    sets = 3)

# Show information about the first exercise
print('############################\n        EXERCISE 1')
exercise_1.show_information()

print('Is exercise 1 suitable for beginners?')
print(exercise_1.is_suitable_for('Beginner'), '\n')

print('Is exercise 1 suitable for intermediate?')
print(exercise_1.is_suitable_for('Intermediate'), '\n')

exercise_1.increase_intensity(repetitions_increase = 2, sets_increase = 1)

print('############################\n    EXERCISE 1 (Updated)')
exercise_1.show_information()

# Create a routine as a type of Exercise
routine = Routine(
    routine_name="Strength Routine", 
    muscle_group="Full Body", 
    difficulty_level="Intermediate", 
    repetitions=0,  
    sets=0, 
    goal="Gain muscle mass", 
    routine_level="Intermediate"
)

# Add exercises to the routine
routine.add_exercise(exercise_1)
routine.add_exercise(exercise_2)

# Display the complete routine with exercises
routine.show_routine()

# Test removing an exercise and displaying the updated routine
routine.remove_exercise("Squats")

print('\n    Routine (Updated)')
routine.show_routine()

# CLASS USER
print('\nUser information:\n')

# Create an instance 
user = User(name="Marta", height=1.57, weight=43, age=21, gender="female")

# Update personal data
user.name = "Maria"

# User calculations
bmi = user.calculate_bmi()

# Body fat calculations
body_fat = user.calculate_body_fat()

# Calories burned calculations
calories = user.calories_activity(30, "push-ups")
calories = user.calories_activity(30, "squats")

# Display user information
user.show_info()
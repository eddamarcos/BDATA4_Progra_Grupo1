class User:
    def __init__(self, name, height, weight, age, gender, fitness_level="Beginner", goal="Maintenance"):
        """Creates a User object with attributes such as name, height, weight, age, gender, fitness level, and goal.

        Args:
            name (str): User's name.
            height (float): Height in meters.
            weight (float): Weight in kilograms.
            age (int): Age in years.
            gender (str): Gender of the user. Can be 'female' or 'male'.
            fitness_level (str, optional): Fitness level of the user. Can be 'Beginner', 'Intermediate', or 'Advanced'. Defaults to "Beginner".
            goal (str, optional): The user's goal. Can be 'Lose weight', 'Gain muscle', or 'Maintenance'. Defaults to "Maintenance".
        """
        self.name = name 
        self.height = height
        self.weight = weight
        self.age = age
        self.gender = gender.lower()
        self.fitness_level = fitness_level
        self.goal = goal

        self.activity = None
        self.calories_burned = None

        valid_levels = ["Beginner", "Intermediate", "Advanced"]
        valid_goals = ["Lose weight", "Gain muscle", "Maintenance"]
        valid_genders = ["female", "male"]

        # Validate fitness level
        if fitness_level not in valid_levels:
            raise ValueError(f"Fitness level is not valid. It must be one of: {valid_levels}")
        if goal not in valid_goals:
            raise ValueError(f"Goal is not valid. It must be one of: {valid_goals}")
        if gender not in valid_genders:
            raise ValueError(f"Gender is not valid. It must be one of: {valid_genders}")
    
    # Calculate the body mass index (BMI)
    def calculate_bmi(self):
        """Calculates the user's body mass index (BMI).

        Returns:
            float: User's body mass index.
        """
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi
    
    # Calculate the body fat percentage
    def calculate_body_fat(self):
        """Calculates the user's body fat percentage.

        Returns:
            float: The body fat percentage.
        """
        bmi = self.calculate_bmi()
        
        if self.gender == 'male':
            body_fat_male = 1.20 * bmi + 0.23 * self.age - 16.2
            return round(body_fat_male, 2)
        elif self.gender == 'female':
            body_fat_female = 1.20 * bmi + 0.23 * self.age - 5.4
            return round(body_fat_female, 2)
        else:
            raise ValueError("Unrecognized gender.")
        

    # Calculate the number of calories burned based on duration, activity, and weight    
    def calories_activity(self, duration, activity):
        """Calculates the number of calories burned during a physical activity.

        Args:
            duration (float): Duration of the activity in minutes.
            activity (str): Name of the physical activity.

        Raises:
            ValueError: _description_
        """
        weight = self.weight

        # Estimated MET values
        met_values = {"push-ups": 4.0, "squats": 5.0, "plank": 4.0, "pull-ups": 8.0, "bicep curl": 3.5, "bench press": 6.0, "triceps dips": 6.5, "barbell row": 7.0,
        "leg extension": 3.0, "leg curl": 3.0, "lateral raises": 3.0, "military press": 6.5, "ab crunch": 3.5, "burpees": 8.0, "mountain climbers": 6.5, 
        "bulgarian squat": 5.5, "deadlift": 7.5, "lunges": 5.5, "dumbbell shoulder press": 6.0, "russian twist": 4.0}
        
        met = met_values.get(activity.lower())
        if met:
            self.activity = activity
            self.calories_burned = met * weight * (duration / 60)
        else:
            raise ValueError("Unrecognized activity.")
        
    # Function to display all user information
    def show_info(self):
        """Displays all user information on the screen.
        """
        print(f"Name: {self.name}")
        print(f"Height: {self.height} m")
        print(f"Weight: {self.weight} kg")
        print(f"Age: {self.age} years")
        print(f"Gender: {self.gender}")
        print(f"Fitness level: {self.fitness_level}")
        print(f"Goal: {self.goal}")
        print(f"Body mass index: {self.calculate_bmi()}")
        print(f"Body fat: {self.calculate_body_fat()} %")
        
        if self.calories_burned is not None:
            print(f"Calories burned doing {self.activity}: {self.calories_burned:.2f} kcal")
        else:
            print("Calories burned have not been calculated yet.")


# Create an instance of User
user = User(name="Marta", height=1.57, weight=43, age=21, gender="female")

# Update personal data
user.name = "Maria"

# User calculations
bmi = user.calculate_bmi()

# Body fat calculations
body_fat = user.calculate_body_fat()

# Calories burned calculations
# calories = user.calories_activity(30, "a")
calories = user.calories_activity(30, "burpees")

# Display user information
user.show_info()
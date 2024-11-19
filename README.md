# Plan your Workout

The project consists of a kind of digital assistant to help people get in shape and track their progress. The idea is that the user can enter their basic information (such as height, weight, age, etc.) and choose a goal, whether it is to lose weight, gain muscle, or maintain it. From there, the program calculates things like body mass index and body fat percentage, and suggests exercise routines tailored to what you want to achieve and your experience level. It also estimates the calories burned according to the routine followed. In short, it is a tool to help you stay active and see progress toward health and fitness goals.

The classes used for this process are the class called “User”, which contains information about the user and the class called “Routine”, which inherits from the “Exercise” class. The “Exercise” class contains information about physical exercises and the “Routine” class returns combinations (with their respective repetitions) of those exercises. The generation of the routine will be based on the data entered by the user and its objective to be achieved.
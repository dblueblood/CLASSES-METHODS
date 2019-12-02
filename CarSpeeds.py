"""
Author: Ayo Asekun
Date Created: Dec 1st, 2019
Last Date Modified: Dec 1st, 2019
Program Description: Creating a Class Profile for Cars
Psuedocode:
<START PROGRAM>
Inputs: Car Profile Information
        - MAKE
        - MODEL
        - TOP SPEED

Process: User inputs information as directed by Program
         For manipulating & displaying Data provided, Methods created to increase, decrease & display current Top Speed
                            ***see comments by methods in code below for more info.***
        Method to increase & display speed - Called x5
        Method to decrease & display speed - Called x5
        Method to display current  speed   - Called x1

Output: Using provided information from user:
        Program displays output as follows
                ====PROFILE====
            Car Make  | xxxxxxxxx
            Car Model | xxxxxxxxx
            Car Speed | xxxxxxxxx
            Car Speed called 5x; each previous call increased by a given constant
            Car Speed called 5x; each previous call decreased by a given constant
            Car Speed called to display current top speed
<END PROGRAM>
"""

class Car:
    def __init__(self):
        self.make = input("Make of Car: ")
        self.model = input("Car Model: ")
        self.spd = int(input("Top Speed: "))
        self.speed = str(self.spd)                                   # Converts integer value to a String input

    """
    Below shows a number of created methods required for current program's functionality
    Profile(): Main Method for Profile creation; Used to call the function to create a New Profile 
               into a program directory
       Push(): The method that calls on attributes from desired profile and positively alters already provided info
               on speed, using a given constant
       Pull(): The method that calls on attributes from desired profile and negatively alters already provided info 
               on speed, using a given constant
    The above methods of "Push & Pull" can only be used to modify mutable data of already saved profiles in the 
    directory accessible by the program and be called upon.
    """
    def Profile(self):
        return "====PROFILE====\n" + "Car Make  | " + self.make + "\nCar Model | " + self.model + "\nCar Speed | 0 - " \
               + self.speed + "MPH"

    def Push(self):
        # Class Method performing a speed increase & returning adjusted speed of car profile
        print("==Increasing Top Speed of " + self.make + " by 5MPH==")
        self.spd = int(self.speed)                                   # Converts String input to an integer value
        self.spd += 5
        self.speed = str(self.spd)                                   # Converts integer value to a String input
        return "New Top Speed " + self.speed + "MPH\n"

    def Pull(self):
        # Class Method performing a speed decrease & returning adjusted speed of car profile
        print("==Decreasing Top Speed of " + self.make + " by 5MPH==")
        self.spd = int(self.speed)                                   # Converts String input to an integer value
        self.spd -= 5
        self.speed = str(self.spd)                                   # Converts integer value to a String input
        return "New Top Speed " + self.speed + "MPH\n"

    def Stay(self):
        # Class Method returning current speed of car profile
        print("=||=Current Top Speed of " + self.make + "=||=")
        return self.speed + "MPH\n"


Profile_1 = Car()
print("============================")
print(Profile_1.Profile())
for i in range(5):
    print(Profile_1.Push())
for i in range(5):
    print(Profile_1.Pull())
print(Profile_1.Stay())

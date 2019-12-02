"""
Author: Ayo Asekun
Date Created: Dec 1st, 2019
Last Date Modified: Dec 1st, 2019
Program Description: Pet Profile
Psuedocode:
<START PROGRAM>
Inputs: Car Profile Information
        NAME OF ANIMAL
        TYPE OF ANIMAL
        AGE OF ANIMAL

Process: User inputs information as directed by Program
         To display Data provided, Method created to present profile of saved pet data

Output: Using provided information from user:
        Program displays output as follows
                 + + PROFILE + +
            PET NAME    - xxxxxxxxxx
            TYPE OF PET - xxxxxxxxx
            PET AGE     - xx
<END PROGRAM>
"""
class Pets:
    def __init__(self):
        self.name = input("Name of Pet: ")
        self.animal_type = input("Type of animal: ")
        self.yr = int(input("Age of Animal[YRS]: "))
        if self.yr not in range(1, 100):
            print("Invalid format")

        self.age = str(self.yr)

    def Profile(self):
        return "+ + PROFILE + +\n" + "PET NAME    - " + self.name + "\nTYPE OF PET - " + self.animal_type +\
               "\nPET AGE     - " + self.age + "yr(s)"


Profile_1 = Pets()
print("============================")
print(Profile_1.Profile())

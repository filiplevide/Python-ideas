def main_tracker():
    add_another_workout = True
    total = 0
    while(add_another_workout):
        sets = int(input("How many sets did you do? "))
        reps = int(input("How many reps did you do? "))
        weight = int(input("How heavy did you lift? (KG) "))

        another_exercice = input("Do you want to add another exercise? Y/N ")
        volume += sets * reps * weight
        total += volume
        print(f"Volume for this exercise: {volume}")
        print(f"Current total weight lifted: {total}")

        if another_exercice.upper() == "N":
            print(f"Total weight lifted: {total}")
            return total
main_tracker()
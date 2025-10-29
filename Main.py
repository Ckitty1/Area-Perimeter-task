'''
Author: Luke Low
Title: Area perimeter calculator
Date: 29/10/25
Version 1.0
'''

def ask(dimension):
    error = "That is not a valid number. Please enter a number more than zero next time."

    while True:
        try:
            response = float(input(f"Please enter the {dimension}: "))
            
            if response > 0:
                break

            else: 
                print(error)
            
        except ValueError:
            print(error)

    return(response)

# Main program

print("\nWelcome to my area & perimeter calculator !!\n")

keep_going = ""

while keep_going == "":

    width = ask("width")
    height = ask("height")

    area = width*height
    print(f"\nThe area is {area} squre units.")

    perimeter = 2*width + 2*height
    print(f"The perimeter is {perimeter} units.")

    keep_going = input("\nWould you like to do another calculation? If yes, press <enter>, if no, press any other key. ")
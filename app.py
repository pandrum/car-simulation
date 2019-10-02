import sys
import re

# herpa derpa
class Car:
    def __init__(self, x, y, heading):
        self.x = int(x)
        self.y = int(y)
        self.heading = heading

    # Prints out information about the car.
    def getCarInfo(self):
        print("Car is currently at: " + str(self.x) +
              "X and " + str(self.y) + "Y." + " - heading: " + self.heading)

    # Used to check the roomsize to see if the car hits a wall.
    def detectCollison(self):
        if (self.x >= room.room_x or self.y >= room.room_y or self.x <= 0 or self.y <= 0):
            sys.exit("Error! The car hit a wall. Ending position of the car is: " +
                     str(self.x) + "X and " +
                     str(self.y) + "Y.")

    # Moves the car in the simulated room. detectCollsion is called after each move the check if the car has hit a wall.
    def moveCar(self):
        print("Car is starting at " + str(self.x) +
              "X and " + str(self.y) + "Y")
        for direction in input_directions:
            # Move forward
            if (direction == 'F' and self.heading == 'N'):
                self.y += 1
                self.detectCollison()
            elif (direction == 'F' and self.heading == 'S'):
                self.y -= 1
                self.detectCollison()
            elif (direction == 'F' and self.heading == 'W'):
                self.x -= 1
                self.detectCollison()
            elif (direction == 'F' and self.heading == 'E'):
                self.x += 1
                self.detectCollison()

            # Move backwards
            elif (direction == 'B' and self.heading == 'N'):
                self.y -= 1
                self.detectCollison()
            elif (direction == 'B' and self.heading == 'S'):
                self.y += 1
                self.detectCollison()
            elif (direction == 'B' and self.heading == 'W'):
                self.x += 1
                self.detectCollison()
            elif (direction == 'B' and self.heading == 'E'):
                self.x -= 1
                self.detectCollison()

            # Turn left
            elif (direction == 'L' and self.heading == 'N'):
                self.heading = 'W'
                self.detectCollison()
            elif (direction == 'L' and self.heading == 'S'):
                self.heading = 'E'
                self.detectCollison()
            elif (direction == 'L' and self.heading == 'W'):
                self.heading = 'S'
                self.detectCollison()
            elif (direction == 'L' and self.heading == 'E'):
                self.heading = 'N'
                self.detectCollison()

            # Turn right
            elif (direction == 'R' and self.heading == 'N'):
                self.heading = 'E'
                self.detectCollison()
            elif (direction == 'R' and self.heading == 'S'):
                self.heading = 'W'
                self.detectCollison()
            elif (direction == 'R' and self.heading == 'W'):
                self.heading = 'N'
                self.detectCollison()
            elif (direction == 'R' and self.heading == 'E'):
                self.heading = 'S'
                self.detectCollison()

            self.getCarInfo()

        print("Success!")
        print("Ending position of the car is: " +
              str(self.x) + "X and " +
              str(self.y) + "Y.")
        print("The cars final heading is " + self.heading + ".")


class Room:
    def __init__(self, room_x, room_y):
        self.room_x = int(room_x)
        self.room_y = int(room_y)

    def getRoomInfo(self):
        print("Room X is: " + self.room_x)
        print("Room Y is: " + self.room_y)


# Ask the user for the size of the room.
while True:
    try:
        input_room_x, input_room_y = (input(
            "Enter two integers to determine the size of the room. Use space as a separator: ")).split()
        if (input_room_x.isdigit() and input_room_y.isdigit()):
            print("Roomsize: " + input_room_x + " " + input_room_y)
            break
        else:
            print("Use only integers please!")
            continue
    except ValueError:
        print("Please enter two digits followed by a space!")
        continue
    else:
        break

# Ask the user for the start coordinates for the car.
# TODO check if user inputs start coordinates that are bigger than the room itself.
while True:
    try:
        input_start_x, input_start_y, input_heading = input(
            "Enter the starting position using two integers and enter the letter 'N', 'S', 'W' or 'E' to determine heading of the car. Use capital letters. Use space as a separator: ").split()
        allowed = re.findall("[NSWE]", input_heading)
        if (input_start_x.isdigit() and input_start_y.isdigit and allowed):
            break
        else:
            print(
                "Use two integers for the starting location of the car and 1 letter for the heading! Use only 'N', 'S', 'W' or 'E'")
            continue

    except (ValueError):
        print(
            "Please enter all the information!")
        continue
    else:
        break

# Ask the user for the directions for the car.
while True:
    print("'F' to move the car forward" +
          "\n'B' to move the car backward" +
          "\n'L' to steer the car to the left" +
          "\n'R' to steer the car to the right")
    input_directions = []
    input_directions = input(
        "Enter one or more of the following characters above in a series to move the car in the room. Example: 'FFBFFLR' ")
    input_directions = input_directions.upper()
    # Verify that only 'FBLR' are used to enter directions.
    allowed = re.findall("[FBLR]", input_directions)
    if (allowed):
        break
    else:
        print("Please enter 'F' 'B' 'L' or 'R'. ")
        continue

# Instantiate objects from the classes.
room = Room(input_room_x, input_room_y)
car = Car(input_start_x, input_start_y, input_heading)

# Run the simulation
car.moveCar()

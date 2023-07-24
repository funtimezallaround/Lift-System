# A PROGRAM TO MIMIC THE COMPLEX MULTI-LIFT AND MULTI-FLOOR LIFT SYSTEM.
# TO MIMIC REAL-WORLD DATA MOST VALUES WILL BE GENERATED RANDOMLY

import random


class Lift:

    def __init__(self, floor_count):

        self.floor_list = list(x for x in range(floor_count))

        # AVERAGE LIFT SPEED IS BETWEEN 1 AND 2.5 m/s
        # AVERAGE DISTANCE BETWEEN 2 FLOORS IS ~3m
        self.top_speed = .5  # top speed is in floors per second
        self.delay = 2  # delay is the short delay from closing & opening the lift doors

        # LIFT ATTRIBUTES WHICH WILL ALWAYS HAVE A VALUE:
        self.current_floor = None
        self.idle = True
        self.distance_from_call = 0
        self.eta_to_call = 0

        # LIFT ATTRIBUTES WHICH MAY NOT HAVE A VALUE:
        self.direction = None
        self.destination_floor = None
        self.distance_from_dest = 0
        self.eta_to_dest = 0
        self.pass_floors = list()

    # HOW TO DISPLAY LIFT'S INFORMATION:
    def __str__(self):
        # ALWAYS PRINT OUT THE FOLLOWING 2 ATTRIBUTES:
        out = f"""
current floor: floor {self.current_floor}
is idle?: {self.idle}
            """
        # ONLY DISPLAY THE FOLLOWING 5 ATTRIBUTES IF LIFT IS NOT IDLE:
        if (not self.idle):
            out += f"""
destination floor: floor {self.destination_floor}
direction: {self.direction}
distance from destination floor: {self.distance_from_dest} floors
ETA to destination: {self.eta_to_dest} seconds
passing floors: {self.pass_floors}
                """
        # ALWAYS PRINT OUT THE FOLLOWING 2 ATTRIBUTES:
        out += f"""
distance from call floor: {self.distance_from_call} floors
ETA to call floor: {self.eta_to_call} seconds
            """
        return out

    # CALLING A LIFT:
    def initialise(self, call_floor, direction):

        # GENERATE RANDOM VALUES FOR LIFT'S FLOOR AND WHETHER THEY ARE IDLE:
        self.current_floor = random.choice(self.floor_list)
        self.idle = random.choice([True, False])

        # CALCULATE THE DISTANCE TO THE CALL FLOOR FROM THE CURRENT FLOOR:
        self.distance_from_call = abs(call_floor - self.current_floor)

        # IF LIFT IS NOT IDLE:
        if not self.idle:

            # GEENRATE RANDOM VALUE FOR LIFT'S DESTINATION FLOOR:
            self.destination_floor = random.choice(self.floor_list)

            # SET THE DIRECTION OF THE LIFT AND CREATE A LIST OF THE FLOORS THAT THE LIFT WILL PASS:
            # list of floors the lift will pass includes the destination floor and excludes the current floor
            if (self.destination_floor > self.current_floor):
                self.direction = "UP"
                self.pass_floors = self.floor_list[self.current_floor+1:(
                    1+self.destination_floor)]
            elif (self.destination_floor < self.current_floor):
                self.direction = "DOWN"
                self.pass_floors = self.floor_list[(
                    self.destination_floor):self.current_floor]

            # SET THE DISTANCE TO THE DESTINATION FLOOR FROM THE CURRENT FLOOR AND THE ETA TO THE DESTINATION:
            self.distance_from_dest = abs(
                self.destination_floor - self. current_floor)
            self.eta_to_dest = self.distance_from_dest / self.top_speed + self.delay

        # CALCULATE THE ETA TO THE CALL FLOOR:
        if self.idle or call_floor == self.destination_floor or (call_floor in self.pass_floors and direction == self.direction):
            self.eta_to_call = self.distance_from_call / self.top_speed + self.delay
        else:
            self.distance_from_call = abs(call_floor - self.destination_floor)
            self.eta_to_call = self.eta_to_dest + (self.distance_from_call /
                                                   self.top_speed) + self.delay
# END OF LIFT CLASS


# GET THE NUBMER OF FLOORS FROM THE USER:
floor_count = 0
valid = False
while (not valid):
    valid = True
    try:
        floor_count = int(input("Please input the number of floors: "))
    except:
        print("Error")
        valid = False

# GET THE NUMBER OF LIFTS FROM THE USER:
lift_count = 0
valid = False
while (not valid):
    valid = True
    try:
        lift_count = int(input("Please input the number of lifts: "))
    except:
        print("Error")
        valid = False

# CREATE A LIST TO CONTAIN ALL THE LIFTS IN THE SYSTEM:
list_of_lifts = [Lift(floor_count) for x in range(lift_count)]

# GET THE CALL FLOOR AND DIRECTION FROM THE USER:
call_floor = -1
direction = ""
valid = False
while (not valid):
    valid = True
    try:
        call_floor = int(
            input("At which floor would you like to call the lift: "))

        if call_floor < 0 or call_floor >= floor_count:
            print("floor out of bounds")
            valid = False

        if call_floor == 0:
            direction = "UP"
        elif call_floor == floor_count-1:
            direction = "DOWN"
        else:
            opt = int(
                input("Which direction do you want to go:\n[1] UP\n[2] DOWN\n"))
            if opt == 1:
                direction = "UP"
            elif opt == 2:
                direction = "DOWN"
            else:
                print("Invalid option")
                valid = False

    except:
        print("Error")
        valid = False

# INITAILISE ALL THE LIFTS IN THE SYSTEM:
[lift.initialise(call_floor, direction) for lift in list_of_lifts]

# PRINT OUT ALL THE LIFTS IN THE SYSTEM:
[print(f"\nLIFT {x}:{list_of_lifts[x]}")
 for x in range(len(list_of_lifts))]

# EVALUATE THE LIFTS
best_lift = Lift(floor_count)
min_eta = 4*floor_count  # largest possible eta is 4 x (floor_count -1)
for lift in list_of_lifts:
    if lift.eta_to_call < min_eta:
        best_lift = lift
        min_eta = lift.eta_to_call
    elif lift.eta_to_call == min_eta and (lift.idle and not best_lift.idle):
        best_lift = lift
    # IF LIFT HAS A LOWER ETA, OR THE SAME ETA AND IS IDLE, IT IS SELECTED AS THE BEST LIFT

# GET THE INDEX OF THE BEST LIFT IN THE LIST OF LIFTS:
best_lift_index = list_of_lifts.index(best_lift)

# PRINT OUT WHICH LIFT IS BEING SENT:
print(f"SENDING LIFT {best_lift_index} TO THE CALL FLOOR:\n{best_lift}")

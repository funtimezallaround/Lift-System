# Lift-System
## A program which selects the best lift to respond to a call

This program evaluates best lift to send to answer a call request.

- The program aims to reduce as much as possible the time spent waiting for the lift to arrive. 
- The user is prompted for the number of floors, and the number of lifts in this system. 
- The speed of the lifts is taken to be 1 floor every 2 seconds, and the time taken for the lift to open the doors is 2 seconds
- To reduce the ammount of input the user must provide, lift attributes, such as the current floor, and whether its idle or not, are generated randomly

The lift selected is the lift with the lowest ETA to the call floor. The ETA is calculated as follows:
  - If the lift is idle, the ETA to the call floor is how long it will take to get to the call floor and open its doors.
  - If the lift is not idle, but the lift will pass by the call floor[^1], the ETA to the call floor is how long it will take to get to the call floor and open its doors.
  - If the lift is not idle, and the lift will not pass by the call floor, the ETA to the call floor is how long the lift will take to get to its destination and open its doors + how long the lift will take to get to the call floor from the destination floor and open its doors

[1]: If the lift is at the call floor and is not idle, then this lift doese not fall into this category, since it is too late to stop the lift at this floor

This program is my first project using Python. While I tried my best, some inefficiencies are present.

Program's limitations:
  - 

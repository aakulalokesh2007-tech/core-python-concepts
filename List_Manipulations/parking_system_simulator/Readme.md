🚗 Parking Lot Capacity Simulator : 
🟢 Easy / 🟡 Medium (Interactive Implementation)
Topics: Array/List Manipulation, State Tracking, Input Validation, 
Simulation🎯 OverviewThis project is an interactive terminal application that simulates a dynamic parking lot management system. 
Based on the core logic of LeetCode #1603 (Design Parking System), this script initializes a parking lot with a set number of spots for Big, Medium, and Small vehicles. 
It then processes a queue of arriving cars, instantly calculating whether each car can successfully park based on real-time capacity.
⚙️ How It Works (The Logic)
Instead of using complex and nested if/else statements for every single car type, this script uses Index Mapping for high efficiency:
State Initialization: 
The parking lot's capacity is stored in a mutable list: capacity = [big, medium, small].
Dynamic Processing: When a car arrives, the user inputs a code (1 for Big, 2 for Medium, 3 for Small).
Index Mapping: The script subtracts 1 from the car's code to perfectly match the list's index (e.g., Car Type 1 checks capacity[0]).
State Update: If the space is greater than 0, the car parks (True), and the capacity is reduced by 1. 
If it equals 0, the car is turned away (False).
⏱️ Complexity AnalysisTime Complexity: $O(N)$Where $N$ is the total number of arriving cars.
The algorithm processes each arriving car exactly once in constant time.
Space Complexity: $O(N)$We store the outcome (True or False) of each car in a dynamically growing results list to output at the end of the simulation.
🛠️ Core Python Concepts DemonstratedRobust Error Handling:
Utilizes try/except blocks to prevent the program from crashing if a user accidentally types a letter instead of a number.
Infinite Loops & Control Flow: Masterful use of while True: loops combined with break and continue statements to ensure clean data entry.
List Mutability: Actively modifying list data in place as the state of the parking lot changes.Dynamic String Formatting: 
Utilizing f-strings (f"...") to provide real-time, context-aware prompts to the user based on the remaining capacity.

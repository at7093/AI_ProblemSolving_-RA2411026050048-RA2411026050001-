Problem Description :
This project implements a solution for the Map Coloring Problem, a classic AI task categorized under Constraint Satisfaction Problems (CSP).The goal is to assign colors to various regions on a map such that no 
two adjacent regions share the same color. The system allows users to define regions, set adjacency relationships, and select from a limited palette of colors (typically 3 or 4) via an interactive interface.

<img width="975" height="387" alt="image" src="https://github.com/user-attachments/assets/d4ad9416-5eb5-4cce-a4ae-00ab51598027" />
<img width="995" height="411" alt="image" src="https://github.com/user-attachments/assets/f63b8f3c-c9ec-4e30-9b53-dbd934eeb52c" />





Algorithm Used: CSP Backtracking SearchThe system utilizes a Backtracking Algorithm to solve the CSP. The logic follows these steps:Variable Selection: The algorithm selects an unassigned region (variable) from 
the map.Domain Assignment: It attempts to assign a color (domain value) from the available list (e.g., Red, Green, Blue).Constraint Check: The algorithm checks if the assigned color violates the primary 
constraint: no adjacent region can have the same color.Recursion & Backtracking: If the assignment is valid, it moves to the next region. If a conflict arises and no colors are left to try, it backtracks to
the previous region and tries a different color

Sample Input/Output :
<img width="319" height="449" alt="image" src="https://github.com/user-attachments/assets/e1787674-542c-46af-a5d3-14acce932128" />
<img width="714" height="797" alt="image" src="https://github.com/user-attachments/assets/ef1936b0-bda1-488d-885e-c0deb5d387c1" />



Execution Steps
To run the interactive web interface, follow these steps:

Clone the Repository:

Bash
git clone https://github.com/YourUsername/AI_ProblemSolving_<RegisterNumber>.git
Install Dependencies:

Bash
pip install streamlit networkx matplotlib
Run the Application:

Bash
streamlit run app.py

Interact: Input your regions and their neighbors in the GUI to visualize the coloring result.

Problem Description :
This project implements a solution for the Map Coloring Problem, a classic AI task categorized under Constraint Satisfaction Problems (CSP).The goal is to assign colors to various regions on a map such that no 
two adjacent regions share the same color. The system allows users to define regions, set adjacency relationships, and select from a limited palette of colors (typically 3 or 4) via an interactive interface.

<img width="818" height="317" alt="image" src="https://github.com/user-attachments/assets/f89733d5-70f6-4d71-aa18-935987621d60" />
<img width="816" height="330" alt="image" src="https://github.com/user-attachments/assets/9db166f3-a68b-49ce-85f2-fc577d7ff064" />



Algorithm Used: CSP Backtracking SearchThe system utilizes a Backtracking Algorithm to solve the CSP. The logic follows these steps:Variable Selection: The algorithm selects an unassigned region (variable) from 
the map.Domain Assignment: It attempts to assign a color (domain value) from the available list (e.g., Red, Green, Blue).Constraint Check: The algorithm checks if the assigned color violates the primary 
constraint: no adjacent region can have the same color.Recursion & Backtracking: If the assignment is valid, it moves to the next region. If a conflict arises and no colors are left to try, it backtracks to
the previous region and tries a different color

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

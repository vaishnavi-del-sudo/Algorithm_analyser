# Vityarthi_project-25bai10120-CSA-
# ALGORITHM ANALYSER 

Developed an AI search algorithm comparison tool implementing BFS, DFS, A*, Best First Search, and Hill Climbing to analyze traversal cost, efficiency, and optimal path selection.

This program is used to suggest the least cost providing algorithm. It takes in a graph/ tree as input and analyses it based on algorithms (BFS, DFS, Hill Climbing, A*, Best First Search) and gives out the cost of each and the least cost algorithm. 

# Features

    Supports multiple search algorithms:

        * Breadth First Search (BFS)
        * Depth First Search (DFS)
        * A* Algorithm
        * Best First Search (Greedy)
        * Hill Climbing

    Compares:

        * Path found by each algorithm
        * Total cost of the path
        * Efficiency of traversal
        * Identifies the **best algorithm** based on minimum cost


# Algorithms Overview
     4.1 Breadth First Search (BFS)

        * Explores nodes level by level ( breadth wise)
        * Guarantees shortest path in terms of steps
        * Does not consider heuristic cost

     4.2 Depth First Search (DFS)

        * Explores deeply into one branch before backtracking ( depth wise)
        * Does not guarantee optimal solution

     4.3 A* Algorithm

        * Uses function:
          f(n) = g(n) + h(n)
        * Combines actual cost and heuristic
        * Guarantees optimal solution if heuristic is accurate

     4.4 Best First Search

        * Uses heuristic function only
          f(n)=h(n)
        * Selects node closest to goal
        * Faster but not always optimal

     4.5 Hill Climbing

        * Greedy approach
        * Moves to best neighboring node
        * May get stuck in local maxima, ridge problem and plateau problem.

# Input Format

Users can define the graph using edge lists:
Enter nodes separated by space(eg: A B C): S A B C D E F G H I J K 
Enter neighbors for S as 'neighbor weight' pairs, separated by commas (e.g., B 1, C 3):  A 4, B 10 , C 11
Enter neighbors for A as 'neighbor weight' pairs, separated by commas (e.g., B 1, C 3): B 8, D 5
Enter neighbors for B as 'neighbor weight' pairs, separated by commas (e.g., B 1, C 3): D 15
Enter neighbors for C as 'neighbor weight' pairs, separated by commas (e.g., B 1, C 3): D 8 , F 2 , E 20
Enter neighbors for D as 'neighbor weight' pairs, separated by commas (e.g., B 1, C 3): H 16, I 20, F 1
Enter neighbors for E as 'neighbor weight' pairs, separated by commas (e.g., B 1, C 3): G 19
Enter neighbors for F as 'neighbor weight' pairs, separated by commas (e.g., B 1, C 3): G 13
Enter neighbors for G as 'neighbor weight' pairs, separated by commas (e.g., B 1, C 3):
Enter neighbors for H as 'neighbor weight' pairs, separated by commas (e.g., B 1, C 3): I 1, J 2
Enter neighbors for I as 'neighbor weight' pairs, separated by commas (e.g., B 1, C 3): J 5, K 13, G 5
Enter neighbors for J as 'neighbor weight' pairs, separated by commas (e.g., B 1, C 3): K 7
Enter neighbors for K as 'neighbor weight' pairs, separated by commas (e.g., B 1, C 3): G 16
Enter heuristic for S: 7
Enter heuristic for A: 8
Enter heuristic for B: 6
Enter heuristic for D: 5
Enter heuristic for E: 3
Enter heuristic for H: 7
Enter heuristic for I: 4
Enter heuristic for J: 5
Enter heuristic for K: 3
Enter start node: S
Enter goal node: G

# Sample Output
BFS: Path = ['S', 'C', 'F', 'G'], Cost = 26
DFS: Path = ['S', 'A', 'B', 'D', 'H', 'I', 'J', 'K', 'G'], Cost = 72
A*: Path = ['S', 'A', 'D', 'F', 'G'], Cost = 23
Best First: Path = ['S', 'C', 'E', 'G'], Cost = 50
Hill Climbing: Path = ['S', 'C', 'F', 'G'], Cost = 26

🏆 Best Algorithm: A* with cost 23


#  Future Enhancements

* Graph visualization using NetworkX
* GUI interface (Tkinter / Streamlit)
* Step-by-step algorithm animation
* AO* algorithm support (AND-OR graphs)
* Performance metrics (time, nodes explored)

#  Author

Vaishnavi Yadav


This project is open-source and available for learning and educational purposes.


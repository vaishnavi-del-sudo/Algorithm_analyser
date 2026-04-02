# Algorithm_analyser
This program creates a chatbot that answers questions related to state search tree algorithms like DFS, BFS, A *, Hill Climb, Best First Search, AO* algorithms. It takes in information from wikipedia and answers the questions asked by the user.
AlgoWiki AI
An Intelligent Algorithm Chatbot

Author: Hansil Bharatkumar Patel
Project Type: Artificial Intelligence & Machine Learning

Overview

AlgoWiki AI is a lightweight, web-based chatbot designed to provide quick and concise explanations of common search algorithms. It uses the Wikipedia API to fetch real-time summaries and presents them through an interactive chat interface.

This project demonstrates how APIs and simple UI frameworks can be combined to build an effective educational tool without relying on heavy machine learning models.

 Objectives
Develop an interactive chatbot for algorithm-related queries
Integrate real-time data retrieval using Wikipedia API
Provide concise and accurate algorithm summaries
Design a clean and user-friendly interface
Demonstrate usage of APIs and Python UI frameworks
 
 Supported Algorithms
Breadth-First Search (BFS)
Depth-First Search (DFS)
A* Search
AO* Algorithm
Hill Climbing
Best-First Search

 System Architecture
1. User Interface (UI)
Built using Streamlit
Accepts user queries
Displays chatbot responses and chat history
2. Chatbot Logic Layer
Processes user input
Matches keywords with predefined mappings
Calls Wikipedia API
3. Data Source
Wikipedia API for real-time summaries

    Technologies Used
Technology	Purpose
Python	Core programming language
Streamlit	Web interface development
wikipedia-api	Fetching data from Wikipedia
HTML/CSS	UI styling

 Methodology
User Input
User enters a query (e.g., "What is BFS?")
Query Processing
Convert input to lowercase
Match keywords
Algorithm Mapping
{
 "bfs": "Breadth-first search",
 "dfs": "Depth-first search"
}
Wikipedia Fetch
Retrieve summary using Wikipedia API
Extract first 2 lines
Response Display
Show response in chat format
Store in session history

Features
Interactive chatbot interface
Real-time Wikipedia data retrieval
Session-based chat history
Predefined algorithm recognition
Clean and simple UI

Advantages
Beginner-friendly
Lightweight and fast
No heavy ML models required
Real-time information
Easily extendable

 
 Future Enhancements
Add more algorithms (Dijkstra, Greedy, Minimax)
Integrate NLP for better understanding
Add voice input/output
Include visualizations and diagrams
Provide detailed explanations
Deploy on cloud platforms
Add multi-language support

 Testing
Input	Expected Output
What is BFS?	Summary of BFS
Explain DFS	Summary of DFS
A* algorithm	Summary
Random query	Default response

 Results
Successfully retrieves summaries from Wikipedia
Displays responses in chat format
Maintains conversation history
Provides quick and accurate information

 Conclusion

AlgoWiki AI is a simple yet effective chatbot that helps users understand fundamental algorithms. By integrating Wikipedia with a Streamlit interface, it offers instant access to knowledge without complex AI models.

 References
Wikipedia API Documentation
Streamlit Documentation
Python Documentation




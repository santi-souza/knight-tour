#!/usr/bin/env python
# This shebang line ensures the script is run with the correct Python interpreter.

"""
This script solves the knight's shortest path problem on a chessboard.
It uses Breadth-First Search (BFS) to find the shortest path from a start to an end position.
"""

import argparse
import json
import logging
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import graphviz

# Logging Setup (show info messages, including timestamp, log level, and message)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Utility Functions
def is_valid(x_coord, y_coord):
    """
    Check if a position (x_coord, y_coord) is valid on an 8x8 chessboard.
    """
    return 0 <= x_coord < 8 and 0 <= y_coord < 8

def to_algebraic(x_coord, y_coord):
    """
    Convert grid coordinates (x_coord, y_coord) into chessboard algebraic notation.
    Example: (0, 0) -> 'a1'
    """
    return f"{chr(y_coord + ord('a'))}{x_coord + 1}"

def from_algebraic(pos):
    """
    Convert a position in algebraic notation (like 'a1') into grid coordinates (x_coord, y_coord).
    Example: 'a1' -> (0, 0)
    """
    return int(pos[1]) - 1, ord(pos[0]) - ord('a')

# KnightPathFinder Class
class KnightPathFinder:
    """
    Class that implements the knight's pathfinding algorithm using BFS.
    """
    def __init__(self):
        """
        Initialize the KnightPathFinder object. The knight moves in 8 possible directions.
        """
        self.knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                             (-2, -1), (-1, -2), (1, -2), (2, -1)]

    def find_shortest_paths(self, start, end):
        """
        Optimized BFS to find all shortest paths from start to end for a knight's tour.
        """
        from collections import defaultdict

        queue = deque([(start, [start])])  # Store tuples of (current position, path)
        shortest_paths = []
        visited = defaultdict(lambda: float('inf'))  # Tracks shortest path length to each node
        min_length = float('inf')  # To track the minimum length of paths found

        while queue:
            current, path = queue.popleft()
            
            # Stop exploring if the path is longer than the shortest already found
            if len(path) > min_length:
                continue

            # If we reach the destination
            if current == end:
                if len(path) < min_length:
                    shortest_paths = [path]  # Reset with new shortest path
                    min_length = len(path)
                elif len(path) == min_length:
                    shortest_paths.append(path)
                continue

            # Explore neighbors
            for delta_x, delta_y in self.knight_moves:
                new_pos = (current[0] + delta_x, current[1] + delta_y)
                if is_valid(new_pos[0], new_pos[1]):
                    # Only consider the move if it leads to a shorter path
                    if len(path) + 1 <= visited[new_pos]:
                        visited[new_pos] = len(path) + 1
                        queue.append((new_pos, path + [new_pos]))

        return shortest_paths

    def generate_graph(self, paths, filename="knight_paths"):
        """
        Generate a single Graphviz DOT file representing multiple knight paths.
        All paths will be shown in the same graph, and only one file will be saved.
        """
        dot = graphviz.Digraph("KnightPaths_Combined")
        
        # Create nodes for each position on the chessboard
        for i in range(8):
            for j in range(8):
                dot.node(f"{i},{j}", label=to_algebraic(i, j), shape="circle")
        
        # Add edges for each path to the same graph
        for path in paths:
            for i in range(len(path) - 1):
                start, end = path[i], path[i + 1]
                dot.edge(f"{start[0]},{start[1]}", f"{end[0]},{end[1]}")
        
        # Render and save the graph with a single filename (no cleanup flag here)
        dot.render(filename, format="png", cleanup=True)
        logging.info("Combined graph saved as %s.png", filename)

    def visualize_path(self, path):
        """
        Visualize the knight's paths and arrows on the chessboard.
        """
        board = [[-1 for _ in range(8)] for _ in range(8)]
        for step, (x_coord, y_coord) in enumerate(path):
            board[x_coord][y_coord] = step
        self.visualize_board(board)

    def visualize_board(self, paths):
        """
        Visualize the chessboard with all paths.
        """
        board = [[-1 for _ in range(8)] for _ in range(8)]  # Start with an empty board
        for path_index, path in enumerate(paths):
            for step, (x_coord, y_coord) in enumerate(path):
                board[x_coord][y_coord] = step + (path_index * 100)  # Differentiate steps across paths

        # Create a plot
        plt.clf()  # Clear any previous figure to avoid overlap
        _, axis = plt.subplots(figsize=(8, 8))
        
        # Set board colors (light and dark squares)
        colors = [[(i + j) % 2 for j in range(8)] for i in range(8)]
        cmap = mcolors.ListedColormap(["#f0d9b5", "#b58863"])
        axis.imshow(colors, cmap=cmap, origin="upper")

        # Overlay the moves from each path
        for x_coord in range(8):
            for y_coord in range(8):
                move = board[x_coord][y_coord]
                if move != -1:
                    # We use the `move` value to color the step and display it differently for each path
                    axis.text(y_coord, x_coord, str(move % 100), color="black", ha="center", va="center", 
                            fontsize=12, fontweight="bold")
                    
        # Add arrows for paths
        for path_index, path in enumerate(paths):
            for step in range(len(path) - 1):
                start = path[step]
                end = path[step + 1]
                axis.annotate("",
                            xy=(end[1] + 0.5, end[0] + 0.5),  # End point (x, y)
                            xytext=(start[1] + 0.5, start[0] + 0.5),  # Start point (x, y)
                            arrowprops=dict(facecolor="black", arrowstyle="->", lw=0.5),
                            fontsize=8)

        axis.set_xticks([x_coord + 0.5 for x_coord in range(8)])
        axis.set_yticks([y_coord + 0.5 for y_coord in range(8)])
        axis.set_xticklabels(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
        axis.set_yticklabels(['8', '7', '6', '5', '4', '3', '2', '1'])
        axis.grid(False)
        plt.title("Knight's Path", fontsize=16, fontweight="bold")
        plt.show()

def main():
    """
    Main function to run the knight's pathfinding program.
    """
    parser = argparse.ArgumentParser(description="Solve Knight's shortest path problem.")
    parser.add_argument("--start", type=str, help="Start position (e.g., a1)", required=False)
    parser.add_argument("--end", type=str, help="End position (e.g., h8)", required=False)
    parser.add_argument("--config", type=str, help="Path to JSON config file", default=None)
    args = parser.parse_args()

    # Check if a config file is provided
    if args.config:
        try:
            with open(args.config, "r", encoding="utf-8") as config_file:
                config = json.load(config_file)
                args.start = config.get("start")
                args.end = config.get("end")
                if not args.start or not args.end:
                    raise ValueError("Config file must contain 'start' and 'end' positions.")
        except (FileNotFoundError, json.JSONDecodeError, ValueError) as error:
            logging.error("Error reading config file: %s", error)
            return

    # If no config file, ensure positions are provided or ask for them
    if not args.start or not args.end:
        print("Enter chess positions using algebraic notation (e.g., a1, h8).")
        args.start = input("Enter the start position: ").strip()
        args.end = input("Enter the end position: ").strip()

    # Validate input positions
    try:
        start = from_algebraic(args.start)
        end = from_algebraic(args.end)
    except (IndexError, ValueError):
        logging.error("Invalid position format. Use algebraic notation (e.g., a1, h8).")
        return

    logging.info("Finding shortest paths from %s to %s...", args.start, args.end)

    # Initialize pathfinder and find shortest paths
    pathfinder = KnightPathFinder()
    shortest_paths = pathfinder.find_shortest_paths(start, end)
    logging.info("Found %d shortest path(s).", len(shortest_paths))

    # Print each path as text
    for path in shortest_paths:
        print(f"Path: {' -> '.join([to_algebraic(x, y) for x, y in path])}")

    # Generate a single combined graph with all paths
    pathfinder.generate_graph(shortest_paths)
    
    # Visualize all the shortest paths on the same board
    pathfinder.visualize_board(shortest_paths)

if __name__ == "__main__":
    main()

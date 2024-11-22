# **Knight's Tour Problem - Development Notes**

## **Introduction**
The Knight's Tour problem involves moving a knight across a chessboard such that it visits every square exactly once. This Python script implements a solution using **Breadth-First Search (BFS)**, ensuring that all minimum-length paths from the starting to the ending position are found. The program includes various options for execution, such as through configuration files, command-line arguments, or interactive mode.

## **Extensions and Future Enhancements**

### **1. Heuristic Optimization: Warnsdorff's Rule**
The script can be enhanced with **Warnsdorff's Rule**, a heuristic that prioritizes moves with fewer onward options. This helps improve the algorithm’s efficiency by reducing unnecessary recursive calls, which makes it faster in finding solutions.

### **2. Generalization**
The algorithm can be generalized to support:
- **Custom board sizes**: Support for chessboards of dimensions other than 8x8 (e.g., NxM).
- **Arbitrary start/end positions**: Allow users to provide any start and end position, with validation to ensure feasibility.

### **3. Visualization**
For a better user experience, consider:
- **Matplotlib** or **Pygame** for animated visualizations of the knight's movement across the chessboard.
- An **interactive chessboard** where users can explore different paths and board configurations.

### **4. AI and Machine Learning Integration**
- **Reinforcement Learning** could be used to predict optimal knight paths.
- Generate training data from the current script, enabling further research on **automated pathfinding** techniques.

### **5. Obstacles and Dynamic Boards**
- Implement obstacles or restricted squares on the board to simulate real-world constraints.
- Modify the algorithm to navigate dynamically around these obstacles.

### **6. Cloud Deployment**
- Deploy the solution as a **REST API** using Flask or FastAPI.
- Allow users to input their board configurations remotely and receive solutions as JSON or visual representations.

## **Summary**
The current script is a solid foundation for solving the Knight's Tour problem. By adding features like heuristic optimization, visualization, machine learning, and cloud deployment, this project can be transformed into a powerful tool for learning, research, and experimentation.

---

# **Knight's Tour Problem - How to Run**

This project solves the Knight's Tour problem on an 8x8 chessboard, calculating the shortest paths for the knight between a starting and ending position using **Breadth-First Search (BFS)**.

## **Requirements**

To run the project, you’ll need Python 3.x and the following libraries:

- matplotlib
- graphviz

### **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## **Types of Run**

The program provides **three different ways to run** depending on your preferences and use case. Here are the types:

### 1. **Using Docker (Recommended for Consistency)**

Docker ensures that the project runs in an isolated environment, making it easier to deploy across systems.

- **Build the Docker image**:

  ```bash
  docker build -t knight_tour .
  ```

- **Run the Docker container**:

  ```bash
  docker run --rm knight_tour
  ```

This will execute the program inside a Docker container.

---

### 2. **Using `config.json` (for Automatic Configuration)**

You can provide a configuration file (`config.json`) that specifies the start and end positions, simplifying the process.

Example `config.json`:
```json
{
  "start": "a1",
  "end": "h8"
}
```

Run the script with:

```bash
python knight_tour.py --config config.json
```

This method is ideal when you want to specify the configuration ahead of time without manually entering the positions each time.

---

### 3. **Using Command Line (Manual Input)**

If you prefer to specify the start and end positions directly via the command line, use this method:

```bash
python knight_tour.py --start a1 --end h8
```

Simply replace `a1` and `h8` with your desired positions.

---

### 4. **Interactive Mode (No Arguments)**

If you want to run the program interactively without using any command-line arguments or configuration files, use this method. The program will prompt you for input:

```bash
python knight_tour.py
```

You will be asked to input chess positions using algebraic notation, like this:

```
Chessboard size: 8x8
Enter chess positions using algebraic notation (e.g., a1, h8).
Enter the start position: a1
Enter the end position: h8
```






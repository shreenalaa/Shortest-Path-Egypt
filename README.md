
# 🗺️ Shortest Path Finder using Dijkstra Algorithm (Python)

A Python implementation of **Dijkstra’s Algorithm** to find the **shortest path between Egyptian cities** using a weighted graph representation.
The project reads city connections from a file and computes the shortest distance and optimal path between two locations.

This project is designed for **educational purposes**, especially for learning:

* Graph theory
* Shortest path algorithms
* Priority queues
* Real-world geographic modeling

---

## ✨ Features

* 📌 Real-world city graph (Egyptian cities)
* 🧠 Dijkstra algorithm implementation
* ⚡ Efficient shortest-path calculation using `heapq`
* 🔁 Undirected weighted graph
* 🗺️ Path reconstruction (not only distance)
* 📂 File-based graph loading
* 🧪 Easy testing and modification

---

## 🏗️ Project Structure

```
shortest-path-egypt/
│
├── main.py
├── cities.txt
└── README.md
```

---

## ⚙️ Requirements

* Python 3.x
* No external libraries required
  (`heapq` is built-in)

---

## 📄 cities.txt Format

Each line represents a road between two cities:

```
City1 City2 Distance
```

### Example:

```
Cairo Giza 10
Cairo Benha 45
Giza Fayoum 100
Giza BeniSuef 135
...
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧠 How It Works

### 1️⃣ Graph Construction

The graph is built from `cities.txt` as an **undirected weighted graph**:

```
City -> [(Neighbor, Distance), ...]
```

---

### 2️⃣ Dijkstra Algorithm

The algorithm:

* Uses a **priority queue (min-heap)**
* Always expands the shortest known distance
* Tracks visited nodes
* Builds the path dynamically

---

## 🧩 Example Output

### Input:

```python
distance, path = dijkstra(graph, "Cairo", "Aswan")
```

### Output:

```
Shortest Distance: 1250
Path:
Cairo -> Giza -> BeniSuef -> Minya -> Assiut -> Sohag -> Qena -> Luxor -> Aswan
```

---

## 🎯 Use Cases

* Data Structures & Algorithms courses
* AI pathfinding basics
* Graph theory education
* Smart navigation systems simulation
* Route optimization
* Transportation modeling
* GIS systems learning
* Educational AI projects

---

## 🚀 Future Enhancements

* GUI visualization (Tkinter / PyQt)
* Map visualization
* A* algorithm implementation
* Bidirectional Dijkstra
* Multi-source shortest path
* Distance heuristics
* CSV import/export
* Real map integration
* Graph plotting
* REST API version

---

## 👩‍💻 Author

**Shereen Alaa**
Machine Learning Engineer
AI & Educational Software Developer

---

## 📄 License

Open-source for educational and academic use.

---

## 🧠 Algorithms Used

* Dijkstra Algorithm
* Graph Representation
* Priority Queue (Min Heap)
* Path Reconstruction
* Greedy Strategy




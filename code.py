import heapq
{
 'Cairo': [('Giza',10), ('Benha',45)],
 'Giza': [('Cairo',10), ('Fayoum',100), ('BeniSuef',135)],
 'Benha': [('Cairo',45), ('Tanta',65), ('Mansoura',110)],
 'Tanta': [('Benha',65), ('Alex',120)],
 'Alex': [('Tanta',120), ('MarsaMatrouh',290)],
 'MarsaMatrouh': [('Alex',290)],
 'Mansoura': [('Benha',110), ('Damietta',70)],
 'Damietta': [('Mansoura',70)],
 'Fayoum': [('Giza',100), ('Minya',160)],
 'BeniSuef': [('Giza',135), ('Minya',140)],
 'Minya': [('Fayoum',160), ('BeniSuef',140), ('Assiut',150)],
 'Assiut': [('Minya',150), ('Sohag',95)],
 'Sohag': [('Assiut',95), ('Qena',90)],
 'Qena': [('Sohag',90), ('Luxor',70)],
 'Luxor': [('Qena',70), ('Aswan',215)],
 'Aswan': [('Luxor',215)]
}

def build_graph(filename):
    graph = {}

    with open(filename, "r") as file:
        for line in file:
            city1, city2, distance = line.split()
            distance = int(distance)

            if city1 not in graph:
                graph[city1] = []
            if city2 not in graph:
                graph[city2] = []

            # Undirected graph (road goes both ways)
            graph[city1].append((city2, distance))
            graph[city2].append((city1, distance))

    return graph

def dijkstra(graph, start, end):
    priority_queue = [(0, start, [])]
    visited = set()

    while priority_queue:
        current_distance, current_city, path = heapq.heappop(priority_queue)

        if current_city in visited:
            continue

        visited.add(current_city)
        path = path + [current_city]

        if current_city == end:
            return current_distance, path

        for neighbor, weight in graph[current_city]:
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (current_distance + weight, neighbor, path)
                )

    return float("inf"), []

graph = build_graph("cities.txt")
distance, path = dijkstra(graph, "Cairo", "Aswan")

print("Shortest Distance:", distance)
print("Path:")
print(" -> ".join(path))


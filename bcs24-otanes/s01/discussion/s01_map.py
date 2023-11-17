graph = {}

#Calling this method will add values in the variable graph dictionary (Line 1).
def add_edge(from_node, to_node, distance):
    graph.setdefault(from_node, {})[to_node] = distance

#Utilizes the depth-first search algorithm to find all paths. All possible paths will be stored in variable paths list (Line 40).
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

#Will calculate the total distance of all routes in a path.
def calculate_distance(route):
    distance = 0
    for i in range(len(route) - 1):
        distance += graph[route[i]][route[i+1]]
    return distance

#Arguments used for the parameters in function add_edge (Line 4).
add_edge("Home", "Store A", 5)
add_edge("Home", "Store B", 7)
add_edge("Home", "Intersection", 10)
add_edge("Store A", "Home", 5)
add_edge("Store A", "Store B", 2)
add_edge("Store B", "School", 2)
add_edge("Intersection", "School", 5)
add_edge("School", "Intersection", 5)

#Storage all the possible paths found from function find_all_paths (Line 8) in a list.
paths = find_all_paths(graph, "Home", "School")

routes_total_distances = []

#Add every distance of every possible routes to the routes_total_distances.
for path in paths:
    routes_total_distances.append(calculate_distance(path))

#Print all possible paths and their corresponding distances.
print("\nAll possible path/s: ")
for i, path in enumerate(paths):
    print(f"Path: {path} Distance: {routes_total_distances[i]}")

min_value = min(routes_total_distances)
min_indices = []

#Add the index of the min_value to the min_indices. Addresses indices with identical values.
for i, distance in enumerate(routes_total_distances):
    if distance == min_value:
        min_indices.append(i)
    
#The values inside min_indices are used to print the values in specific indices in paths list and routes_total_distances list.
print("\nShortest path/s: ")
for i in min_indices:
    if 0 <= i < len(paths) and 0 <= i < len(routes_total_distances):
        path = paths[i]
        distance = routes_total_distances[i]
        print(f"Path: {path} Distance: {distance}")

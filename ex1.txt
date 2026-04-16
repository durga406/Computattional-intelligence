class Graph:
    def __init__(self):
        self.adj = {}

    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = []
            print("Node added")
        else:
            print("Node already exists")

    def delete_node(self, node):
        if node in self.adj:
            for i in self.adj:
                self.adj[i] = [x for x in self.adj[i] if x[0] != node]
            del self.adj[node]
            print("Node deleted")
        else:
            print("Node not found")

    def add_edge(self, n1, n2, cost):
        if n1 in self.adj and n2 in self.adj:
            self.adj[n1].append((n2, cost))
            self.adj[n2].append((n1, cost))
            print("Edge added")
        else:
            print("Both nodes must exist")

    def delete_edge(self, n1, n2):
        if n1 in self.adj and n2 in self.adj:
            self.adj[n1] = [x for x in self.adj[n1] if x[0] != n2]
            self.adj[n2] = [x for x in self.adj[n2] if x[0] != n1]
            print("Edge deleted")
        else:
            print("Nodes not found")

    def display(self):
        print("\nAdjacency List:")
        for i in self.adj:
            print(i, "->", self.adj[i])

def bfs(graph, start, goal):
    if start not in graph.adj or goal not in graph.adj:
        print("Start or Goal node not found")
        return
    visited = []
    fringe = [start]
    print("\n--- BFS Traversal (Ignoring Costs) ---")
    while fringe:
        current = fringe.pop(0)
        print("\nDequeue:", current)
        if current not in visited:
            visited.append(current)
            if current == goal:
                print("Goal node found!")
                print("Final Visited Order:", visited)
                return
            for neighbor, _ in graph.adj[current]:
                if neighbor not in visited and neighbor not in fringe:
                    fringe.append(neighbor)
            print("Fringe:", fringe)
    print("\nGoal not found")

def dfs(graph, start, goal):
    if start not in graph.adj or goal not in graph.adj:
        print("Start or Goal node not found")
        return
    visited = []
    stack = [start]
    print("\n--- DFS Traversal (Ignoring Costs) ---")
    while stack:
        current = stack.pop()
        print("Pop:", current)
        if current not in visited:
            visited.append(current)
            if current == goal:
                print("Goal found!")
                print("Visited order:", visited)
                return
            neighbors = [n for n, _ in graph.adj[current] if n not in visited]
            stack.extend(reversed(neighbors))
            print("Stack:", stack)
    print("\nGoal not found")

def ucs(graph, start, goal):
    if start not in graph.adj or goal not in graph.adj:
        print("Start or Goal node not found")
        return
    visited = {}
    fringe = [(0, start)]
    print("\n--- UCS Traversal (Using Costs) ---")
    while fringe:
        fringe.sort()
        cost, current = fringe.pop(0)
        print("\nSelected Node:", current, "with cumulative cost:", cost)

        if current in visited and visited[current] <= cost:
            continue
        visited[current] = cost

        if current == goal:
            print("Goal found!")
            print("Final Visited Costs:", visited)
            return

        for neighbor, weight in graph.adj[current]:
            new_cost = cost + weight
            fringe.append((new_cost, neighbor))
        print("Fringe:", fringe)
    print("\nGoal not found")

graph = Graph()
n = int(input("Enter number of nodes: "))
for _ in range(n):
    graph.add_node(input("Enter node: "))

e = int(input("Enter number of edges: "))
for _ in range(e):
    n1 = input("Enter node 1: ")
    n2 = input("Enter node 2: ")
    cost = int(input("Enter cost: "))
    graph.add_edge(n1, n2, cost)

while True:
    print("\n1. Add Node\n2. Delete Node\n3. Add Edge\n4. Delete Edge\n5. Display Graph\n6. BFS\n7. DFS\n8. UCS\n9. Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        graph.add_node(input("Enter node: "))
    elif ch == 2:
        graph.delete_node(input("Enter node: "))
    elif ch == 3:
        n1, n2 = input("Enter node 1: "), input("Enter node 2: ")
        cost = int(input("Enter cost: "))
        graph.add_edge(n1, n2, cost)
    elif ch == 4:
        graph.delete_edge(input("Enter node 1: "), input("Enter node 2: "))
    elif ch == 5:
        graph.display()
    elif ch == 6:
        bfs(graph, input("Start: "), input("Goal: "))
    elif ch == 7:
        dfs(graph, input("Start: "), input("Goal: "))
    elif ch == 8:
        ucs(graph, input("Start: "), input("Goal: "))
    elif ch == 9:
        break


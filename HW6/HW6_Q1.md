```python
# Name: Ayan Tuladhar


from queue import Queue

# The following list dictionary represents table for Dijsktra's and Breadth First Search Calculation.
# a, b, c, d and e represents nodes.

Dijsktra_Calculation = {
                   'A': {'B': 4, 'C': 2},
                   'B': {'C': 3, 'D': 2, 'E': 3},
                   'C': {'B': 1, 'D': 4, 'E': 5},
                   'E': {'D': 1},
                   'D': {}
                        }

Undirected = {
                   'A': ['B', 'C'],
                   'B': ['C', 'D', 'E'],
                   'C': ['B', 'D', 'E'],
                   'E': ['D'],
                   'D': []
                        }

# The following represents Dijkstra's Algorithm for undirected graph.
# It visits all the neighbour nodes at present depth prior to moving on to the nodes at next depth level.
# It stacks the first explored node and contrast DFS as last visit.
# It traverse the node first and then queue them.


def Undirected_graph(output, begin_vertex, end_vertex):
    if begin_vertex in output and end_vertex in output:
        traversed = {}
        short_distance = {}
        for keys in output:
            traversed[keys] = False
            short_distance[keys] = []
        begin_queue = Queue()
        traversed[begin_vertex] = True
        for items in output[begin_vertex]:
            begin_queue.put(items)
            traversed[items] = True
            short_distance[items].append(begin_vertex)
            short_distance[items].append(items)
        while not begin_queue.empty():
            recent_vertex = begin_queue.get()
            for items in output[recent_vertex]:
                if not traversed[items]:
                    traversed[items] = True
                    begin_queue.put(items)
                    for a in short_distance[recent_vertex]:
                        short_distance[items].append(a)
                    short_distance[items].append(items)
        if short_distance[end_vertex] != []:
            print("The shortest distance from\t" + begin_vertex + "\tto\t" + end_vertex + "\t=")
            print(short_distance[end_vertex])
            print("")
        else:
            print("The vertex does not exist from " + begin_vertex + " to " + end_vertex)
            print("Therefore the result = ∞, infinity")
    else:
        print("No Vertex exist")

# The following program implements Dijsktra's algorithm which is an iterative algorithm that provides us with
# The shortest path from one node to all other nodes.
# This program calculates each weight carries while traversing through the nodes by starting at a particular vertex-
# to find the shortest distances or minimum cost..



def Dijsktras_Algorithm(output, begin_vertex, end_vertex):
    if begin_vertex in output and end_vertex in output:
        short_distance = {}
        weight = {}
        for keys in output.keys():
            weight[keys] = 5555555
            short_distance[keys] = []
        begin_queue = Queue()
        for items in output[begin_vertex].keys():
            begin_queue.put(items)
            short_distance[items].append(begin_vertex)
            short_distance[items].append(items)
            weight[items] = output[begin_vertex][items]
        while not begin_queue.empty():
            vertices = begin_queue.get()
            for items, calculate in output[vertices].items():
                if calculate + weight[vertices] < weight[items]:
                    begin_queue.put(items)
                    short_distance[items] = []
                    weight[items] = calculate + weight[vertices]
                    for b in short_distance[vertices]:
                        short_distance[items].append(b)
                    short_distance[items].append(items)
        if short_distance[end_vertex] != []:
            print("The total weight cost =  " + str(weight[end_vertex]))
            print("The shortest distance from\t{'" + end_vertex + "': '" + begin_vertex + "'}\t=")
            print(short_distance[end_vertex])
            print("")
        else:
            print("The vertex does not exist from " + end_vertex + " : " + begin_vertex)
            print("Therefore the result = ∞, infinity")
    else:
        print("No Vertex exist")

# The following displays the graph of Dijsktra's Algorithm.


print("")
print("The following output represents the Dijsktra Algorithm.")
print("The following diagram represents directed graph.")
print("Each vertices contains weight. For example, vertex from C to E contains two weight.")
print("")
print("             \u21B1[B]----2------\u2192[D]")
print("            / |\u2191\          \u21B1  \u2191")
print("           /  || \        /   |")
print("          /   ||  \      /    |")
print("         /    ||   \    /     |")
print("        /     |1    \  4      |")
print("       /      ||     \/       |")
print("      4       3|     /3       1")
print("     /        ||    /  \      |")
print("    /         ||   /    \     |")
print("   /          ||  /      \    |")
print("  /           \u2193| /        \   |")

print(" [A]----2----\u2192[C]---2----\u2192 \u21B3 [E]")
print("")
print("")
print("Node(A) is added to Visited. Weight:0\n")
print("\t\tRelaxed: vertex[B]: OLD:Infinity, NEW: 4, Paths: {'B': 'A'}\n")
print("\t\tRelaxed: vertex[C]: OLD:Infinity, NEW: 2, Paths: {'B': 'A', 'C': 'A'}\n")
print("The calculation for distance from A to C: ")
Dijsktras_Algorithm(Dijsktra_Calculation, 'A', 'C')
print("NODE(C) is added to Visited. Weight: 2\n")
print("\t\tRelaxed: vertex[D]: OLD: Infinity, NEW: 6, Paths: {'B': 'A', 'C': 'A', 'D': 'C'}\n")
print("\t\tRelaxed: vertex[E]: OLD: Infinity, NEW: 7, Paths: {'B': 'A', 'C': 'A','D': 'C','E': 'C'}\n")
print("\t\tRelaxed: vertex[B]: OLD:4, NEW: 3, Paths: {'B':'C', 'C':'A', 'D': 'C', 'E': 'C'}\n")
print("The calculation for distance from A to B: ")
Dijsktras_Algorithm(Dijsktra_Calculation, 'A', 'B')
print("Node(B) is added to Visited. Weight:3\n")
print("\t\tNo edge relaxation is needed for edge, C\n")
print("\t\tRelaxed: vertex[E]: OLD:7, NEW: 6, Paths: {'B': 'C', 'C': 'A', 'D': 'C', 'E': 'B'}\n")
print("\t\tRelaxed: vertex[D]: OLD:6, NEW: 5, Paths: {'B': 'C', 'C': 'A', 'D': 'B', 'E': 'B'}\n")
print("The calculation for distance from A to D: ")
Dijsktras_Algorithm(Dijsktra_Calculation, 'A', 'D')
print("Node(D) is added to Visited. Weight:5\n")
print("\t\tNo unvisited outgoing edges from this node, D\n")
print("The calculation for distance from A to E: ")
Dijsktras_Algorithm(Dijsktra_Calculation, 'A', 'E')
print("Node(E) is added to Visited. Weight:6\n")
print("\t\tNo edge relaxation is needed for edge, D\n")
print("The calculation for distance from D to A: ")
Dijsktras_Algorithm(Dijsktra_Calculation, 'D', 'A')
print("")
print("Final: ({'A': 0, 'B': 3, 'C': 2, 'D': 5, 'E': 6}, {'C': 'A', 'B': 'C', 'D': 'B', 'E': 'B'})")


# The following displays the graph of Undirected Graph.




print("")
print("The following output represents the Undirected Graph.")
print("")
print("             [B]-----------[D]")
print("            / |\          /  |")
print("           /  | \        /   |")
print("          /   |  \      /    |")
print("         /    |   \    /     |")
print("        /     |    \  /      |")
print("       /      |     \/       |")
print("      /       |     /\       |")
print("     /        |    /  \      |")
print("    /         |   /    \     |")
print("   /          |  /      \    |")
print("  /           | /        \   |")
print(" /            |/          \  |")
print("[A]-----------[C]----------[E]")
print("")
print("")





print("The calculation for distance from A to B: ")
Undirected_graph(Undirected, 'A', 'B')
print("The calculation for distance from A to C: ")
Undirected_graph(Undirected, 'A', 'C')
print("The calculation for distance from A to D: ")
Undirected_graph(Undirected, 'A', 'D')
print("The calculation for distance from A to E: ")
Undirected_graph(Undirected, 'A', 'C')
print("The calculation for distance from B to C: ")
Undirected_graph(Undirected, 'B', 'C')
print("The calculation for distance from B to D: ")
Undirected_graph(Undirected, 'B', 'D')
print("The calculation for distance from B to E:")
Undirected_graph(Undirected, 'B', 'E')
print("The calculation for distance from C to D:")
Undirected_graph(Undirected, 'C', 'D')

```

    
    The following output represents the Dijsktra Algorithm.
    The following diagram represents directed graph.
    Each vertices contains weight. For example, vertex from C to E contains two weight.
    
                 ↱[B]----2------→[D]
                / |↑\          ↱  ↑
               /  || \        /   |
              /   ||  \      /    |
             /    ||   \    /     |
            /     |1    \  4      |
           /      ||     \/       |
          4       3|     /3       1
         /        ||    /  \      |
        /         ||   /    \     |
       /          ||  /      \    |
      /           ↓| /        \   |
     [A]----2----→[C]---2----→ ↳ [E]
    
    
    Node(A) is added to Visited. Weight:0
    
    		Relaxed: vertex[B]: OLD:Infinity, NEW: 4, Paths: {'B': 'A'}
    
    		Relaxed: vertex[C]: OLD:Infinity, NEW: 2, Paths: {'B': 'A', 'C': 'A'}
    
    The calculation for distance from A to C: 
    The total weight cost =  2
    The shortest distance from	{'C': 'A'}	=
    ['A', 'C']
    
    NODE(C) is added to Visited. Weight: 2
    
    		Relaxed: vertex[D]: OLD: Infinity, NEW: 6, Paths: {'B': 'A', 'C': 'A', 'D': 'C'}
    
    		Relaxed: vertex[E]: OLD: Infinity, NEW: 7, Paths: {'B': 'A', 'C': 'A','D': 'C','E': 'C'}
    
    		Relaxed: vertex[B]: OLD:4, NEW: 3, Paths: {'B':'C', 'C':'A', 'D': 'C', 'E': 'C'}
    
    The calculation for distance from A to B: 
    The total weight cost =  3
    The shortest distance from	{'B': 'A'}	=
    ['A', 'C', 'B']
    
    Node(B) is added to Visited. Weight:3
    
    		No edge relaxation is needed for edge, C
    
    		Relaxed: vertex[E]: OLD:7, NEW: 6, Paths: {'B': 'C', 'C': 'A', 'D': 'C', 'E': 'B'}
    
    		Relaxed: vertex[D]: OLD:6, NEW: 5, Paths: {'B': 'C', 'C': 'A', 'D': 'B', 'E': 'B'}
    
    The calculation for distance from A to D: 
    The total weight cost =  5
    The shortest distance from	{'D': 'A'}	=
    ['A', 'C', 'B', 'D']
    
    Node(D) is added to Visited. Weight:5
    
    		No unvisited outgoing edges from this node, D
    
    The calculation for distance from A to E: 
    The total weight cost =  6
    The shortest distance from	{'E': 'A'}	=
    ['A', 'C', 'B', 'E']
    
    Node(E) is added to Visited. Weight:6
    
    		No edge relaxation is needed for edge, D
    
    The calculation for distance from D to A: 
    The vertex does not exist from A : D
    Therefore the result = ∞, infinity
    
    Final: ({'A': 0, 'B': 3, 'C': 2, 'D': 5, 'E': 6}, {'C': 'A', 'B': 'C', 'D': 'B', 'E': 'B'})
    
    The following output represents the Undirected Graph.
    
                 [B]-----------[D]
                / |\          /  |
               /  | \        /   |
              /   |  \      /    |
             /    |   \    /     |
            /     |    \  /      |
           /      |     \/       |
          /       |     /\       |
         /        |    /  \      |
        /         |   /    \     |
       /          |  /      \    |
      /           | /        \   |
     /            |/          \  |
    [A]-----------[C]----------[E]
    
    
    The calculation for distance from A to B: 
    The shortest distance from	A	to	B	=
    ['A', 'B']
    
    The calculation for distance from A to C: 
    The shortest distance from	A	to	C	=
    ['A', 'C']
    
    The calculation for distance from A to D: 
    The shortest distance from	A	to	D	=
    ['A', 'B', 'D']
    
    The calculation for distance from A to E: 
    The shortest distance from	A	to	C	=
    ['A', 'C']
    
    The calculation for distance from B to C: 
    The shortest distance from	B	to	C	=
    ['B', 'C']
    
    The calculation for distance from B to D: 
    The shortest distance from	B	to	D	=
    ['B', 'D']
    
    The calculation for distance from B to E:
    The shortest distance from	B	to	E	=
    ['B', 'E']
    
    The calculation for distance from C to D:
    The shortest distance from	C	to	D	=
    ['C', 'D']
    
    


```python

```

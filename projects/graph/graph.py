"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        pass  # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.

        Memorize:
        Create an empty queue and enqueue the starting vertex ID
        Create an empty Set to store veisited vertices
        while the queue is not empty...
            Dequeue the first vertex
            If that vertex has not be visited...
                Mark it as visited
                Then add all of its neighbors to the back of the queue
        """
        # create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        # Create an empty Set to store veisited vertices
        visited = set()
        # while the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # If that vertex has not be visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        Memorize:
        Create an empty stack and push the starting vertex ID
        Create an empty Set to store veisited vertices
        while the stack is not empty...
            Pop the first vertex
            If that vertex has not be visited...
                Mark it as visited
                Then add all of its neighbors to the back of the queue
        """
        # Create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex)
        # Create an empty Set to store veisited vertices
        visited = set()
        # while the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If that vertex has not be visited...
            while v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()

        def dft_rec(s, v):
            if v not in visited:
                print(v)
                visited.add(v)
            else:
                return
            for neighbor in self.vertices[v]:
                s.push(neighbor)
            if s.size() > 0:
                while s.size() > 0:
                    v = s.pop()
                    if v is not None:
                        dft_rec(s, v)
            return

        v = s.pop()
        dft_rec(s, v)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue((starting_vertex,))
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            p = q.dequeue()
            # Grab the last vertex from the PATH
            v = p[len(p)-1]
            # If that vertex has not been visited...
            if v not in visited:
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN PATH
                    return list(p)
                # Mark it as visited...
                visited.add(v)
                # Then add A PATH to its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    # COPY THE PATH
                    cp = p + (neighbor,)
                    # APPEND THE NEIGHBOR TO THE BACK
                    q.enqueue(cp)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push((starting_vertex,))
        visited = set()
        while s.size() > 0:
            p = s.pop()
            v = p[len(p)-1]
            while v not in visited:
                if v == destination_vertex:
                    return list(p)
                visited.add(v)
                for neighbor in self.vertices[v]:
                    cp = p + (neighbor,)
                    s.push(cp)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        s = Stack()
        s.push((starting_vertex,))
        path_found = False
        visited = set()

        def dft_rec(s, v, p):
            nonlocal path_found
            if v == destination_vertex or path_found:
                path_found = True
                return p
            else:
                if v not in visited:
                    visited.add(v)
                else:
                    return None
                for neighbor in self.vertices[v]:
                    cp = p + (neighbor,)
                    s.push(cp)
                if s.size() > 0:
                    while s.size() > 0:
                        p = s.pop()
                        v = p[len(p)-1]
                        if v is not None:
                            return dft_rec(s, v, p)
            return None

        p = s.pop()
        v = p[len(p)-1]
        result = dft_rec(s, v, p)
        if result is None:
            return None
        else:
            return list(result)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

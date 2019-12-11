from util import Stack, Queue 

def earliest_ancestor(ancestors, starting_node):

	nodes_temp = set()
	nodes = {}

	for item in ancestors:
		for val in item:
			nodes_temp.add(val)

	for item in nodes_temp:
		nodes[item] = set()

	for item in ancestors:
		if item[0] in nodes_temp and item[1] in nodes_temp:
			nodes[item[0]].add(item[1])

	q = Queue()
	q.enqueue( [starting_node] )
	visited = set()
	routes = []
	longest_route = []
	long_route_length = 0
	ancestor_parents = []
	oldest_ancestor = 0

	while q.size() > 0:
		p = q.dequeue()
		v = p[-1]
		if v not in visited:
			visited.add(v)
			for i in range(1,len(nodes)+1):
				if v in nodes[i]:
					cp = p.copy()
					cp.append(i)
					q.enqueue(cp)
					routes.append(cp)
	if len(routes) > 0:
		longest_route = max(routes, key=len)
		long_route_length = len(longest_route)
	else:
		return -1

	new_routes = list(filter(lambda arr: len(arr) == long_route_length, routes))

	if len(new_routes) > 1:
		for el in new_routes:
			ancestor_parents.append(el[-1])
		oldest_ancestor = min(ancestor_parents)
	elif len(new_routes) == 1:
		oldest_ancestor = new_routes[0][-1]
	else:
		oldest_ancestor = -1

	return oldest_ancestor


# ancenstor_arr = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(ancenstor_arr, 6))


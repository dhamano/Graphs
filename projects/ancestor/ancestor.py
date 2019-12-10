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
			# nodes[item[1]].add(item[0])
	# print(nodes)

	q = Queue()
	q.enqueue( [starting_node] )
	visited = set()
	routes = []
	count = 0
	longest_route = 0
	long_route_length = 0
	ancestor_parents = []
	oldest_ancestor = 0

	while q.size() > 0:
		count += 1
		p = q.dequeue()
		v = p[-1]
		# print(f"count: {count} | v: {v}")
		if v not in visited:
			visited.add(v)
			# find parent
			# print(nodes)
			for i in range(1,len(nodes)+1):
				if v in nodes[i]:
					# print(f"nodes[{i}]: {nodes[i]}")
					cp = p.copy()
					# print(f"cp: {cp}")
					cp.append(i)
					# print(f"cp appended: {cp}")
					q.enqueue(cp)
					routes.append(cp)
	if len(routes) > 0:
		longest_route = max(routes, key=len)
		long_route_length = len(longest_route)
	else :
		return -1

	# print(f"long_route_length: {long_route_length}")

	new_routes = list(filter(lambda arr: len(arr) == long_route_length, routes))
	# print(new_routes)

	if len(new_routes) > 1:
		for el in new_routes:
			ancestor_parents.append(el[-1])
			# print(f'ancestor_parents: {ancestor_parents}')
		oldest_ancestor = min(ancestor_parents)
		# print(f'ancestor_parents: {ancestor_parents} | oldest_ancestor: {oldest_ancestor}')
	elif len(new_routes) == 1:
		oldest_ancestor = new_routes[0][-1]
	else:
		oldest_ancestor = -1

	return oldest_ancestor




# print(earliest_ancestor([[1,3], [2,3], [3,6], [5,6], [5,7], [4,5], [4,8], [8,9], [11,8], [10,1]], 6))
ancenstor_arr = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(ancenstor_arr, 2))


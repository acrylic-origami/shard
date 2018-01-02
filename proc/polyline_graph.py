import sys

with open(sys.argv[1], 'r') as f:
	polylines = list(f)
	point_set = set()
	for line in polylines:
		for point in line.strip().split(" "):
			point_set.add(point)
	
	point_set = list(point_set)
	adj_list = [[] for i in range(len(point_set))]
	for line in polylines:
		points = line.strip().split(" ")
		for i in range(1, len(points)):
			left = point_set.index(points[i - 1])
			right = point_set.index(points[i])
			adj_list[left].append(str(right))
			adj_list[right].append(str(left))
	
	for i in range(len(point_set)):
		# pass
		print("[[%s],[%s]]," % (point_set[i], ",".join(adj_list[i])))
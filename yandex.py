import json

def jsonsumm(data):
	pass
	xset = []
	output = []
	xmax = 0
	ymax = 0

	for item in data:
		xset.append(item["x"])

		if item["x"]>xmax:
			xmax = item["x"]
		if item["y"]>ymax:
			ymax = item["y"]

	xset = list(set(xset))
	matrix = [[0 for x in xrange(ymax)] for x in xrange(xmax)]

	for item in data:
		x = item["x"]-1
		y = item["y"]-1
		matrix[x][y] = item["value"]

	for x in xset:
		if (sum(matrix[x-1]) - matrix[x-1][ymax -1]) == matrix[x-1][ymax -1]:
			template = {}
			template["x"] = x
			template["correct"] = 1
			output.append(template)
		else:
			template = {}
			template["x"] = x
			template["correct"] = 0
			output.append(template)

	return output

def process(json_string):
	return json.dumps(jsonsumm(json.loads(json_string)))
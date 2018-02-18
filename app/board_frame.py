'''
The BoardFrame class stores the data from the board at each move request
'''


class BoardFrame:

	def __init__(self, data):
		portedRequest = {}
		portedRequest['food'] = []
		portedRequest['snakes'] = []
		request = data

		for food in request['food']['data']:
			food_coord = [food['x'], food['y']]

			portedRequest['food'].append(food_coord)

		for snake in request['snakes']['data']:
			port_snake = {}
			port_snake['coords'] = []
			for point in snake['body']['data']:
				port_snake['coords'].append([point['x'], point['y']])
			portedRequest['snakes'].append(port_snake)
		us = request['you']
		ourSnake = {}
		ourSnake['coords'] = []
		for point in us['body']['data']:
			ourSnake['coords'].append([point['x'], point['y']])

		ourSnake['name'] = us['name']
		ourSnake['taunt'] = us['taunt']
		ourSnake['length'] = us['length']
		ourSnake['health'] = us['health']
		ourSnake['id'] = us['id']

		portedRequest['turn'] = request['turn']
		portedRequest['height'] = request['height']
		portedRequest['width'] = request['width']

		data = portedRequest

		self.turn = data["turn"]
		self.height = data["height"]
		self.width = data["width"]
		self.snakes = data["snakes"]
		self.foods = data["food"]
		self.ourSnake = ourSnake
		self.ourLoc = self.ourSnake["coords"][0]

	def findOurSnake(self, snakes):
		for snake in snakes:
			if snake["id"] == self.us:
				return snake
'''
	def portAPI(request):
		portedRequest = {}
		portedRequest['food'] = []
		portedRequest['snakes'] = []

		for food in request['food']:
			portedRequest['food'].append([food['x'], food['y']])

		for snake in request['snakes']:
			port_snake = {}
			port_snake['coords'] = []
			for point in snake['body']:
				port_snake['coords'].append([point['x'], point['y']])

		ourSnake = {}
		ourSnake['coords'] = []
		for point in request['you']:
			ourSnake['coords'].append([point['x'], point['y']])

		portedRequest['turn'] = request['turn']
		portedRequest['height'] = request['height']
		portedRequest['width'] = request['width']
		

		return portedRequest

'''
'''
	def __init__(self, data):
		self.turn = data['turn']
		self.height = data['height']
		self.width = data['width']
		self.snakes = data['snakes']
		self.foods = data['food']['data']
		self.ourSnake = data['you']['data']
		self.ourLoc = self.ourSnake[0]
'''





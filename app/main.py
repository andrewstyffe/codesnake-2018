'''
A battlesnake AI based on the 2016 battlesnake API. Seeks the closest food on the board.
Avoids head on collisions with other snakes and other risky moves.

Author: Elio Ferri, Lee Zeitz
'''
import bottle
import os
import random
import sys

from board_frame import BoardFrame
from snake_util import closestFood, emptyMove, foodMove, findMove, idealMove, altMove

@bottle.route('/')
def static():
    return "the server is running"


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post("/start")
def start():
	data = bottle.request.json

	return {
		"color": "#C42B3A",
		"name": "codesnek",
		"head_url": "https://s-media-cache-ak0.pinimg.com/736x/f5/ed/5e/f5ed5e6aa79d4919dde9a6253751e039.jpg",
		"taunt": "ohNO",
		"head_type": "tongue",
		"tail_type": "fat-rattle"
	}


@bottle.post("/move")
def move():

	data = bottle.request.json

	board = BoardFrame(data)

	if board.foods:
		dest = closestFood(board)
	else:
		if (board.ourLoc == [board.width-1,board.height-1]):
			dest = [0,0]
		else:
			dest = [board.width-1,board.height-1]

	if board.ourSnake['health'] > 60:
		move = emptyMove(board)

	elif board.ourSnake['health'] > 25:
		#Go towards the closest food, otherwise go towards a corner of the board. 
		move = foodMove(board)
	
	else:
		move = findMove(board, dest)
	
	#Find altrenate safe move if the desired move was not ideal.
	if not idealMove(board, move):
		move = altMove(board, move, dest)

	print ("move: " + move)

	# Catch errors and display in taunt to debug.
	if move == "no_safe":
		print ("ERROR!")
		return{
			"move": "up",
			"taunt": "ERROR!"
		}

	else:
		return {
			"move": move,
			"taunt": ":0"
		}


@bottle.post("/end")
def end():
	data = bottle.request.json

	return {
		"taunt": "dang"
	}


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', sys.argv[1]),
        debug = True)

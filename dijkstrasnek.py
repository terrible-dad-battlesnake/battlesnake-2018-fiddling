"""
Pretty dumb Dijkstra snake, but makes use of a bunch of handy-dandy utility
functions and classes I wrote, so good example usage for those interested.
:author Charlie
"""
import bottle
import pathfinding
from bottle import request
from game_objects import World

app = bottle.app()


@app.post("/start")
def start():
    return {
        "name": "Dijkstrasnek",
        "taunt": "Booo application. Yay theory!"
    }


@app.post("/move")
def move():

    world = World(request.json)
    d, p = pathfinding.dijkstra(world, world.you)

    nextfood_x, nextfood_y = world.food[0]
    path = pathfinding.find_path_dijkstra(nextfood_x, nextfood_y, p)
    next_move = pathfinding.get_next_move(world.you.body[0], path)

    return {
        "move": next_move
    }


app.run()

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
    path = pathfinding.find_path_dijkstra(0, 0, p)
    next_move = pathfinding.get_next_move(world.you.body[0], path)

    return {
        "move": next_move
    }


app.run()

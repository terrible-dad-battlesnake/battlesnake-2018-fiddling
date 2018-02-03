from bottle import request, app
from game_objects import World
from pathfinding import dijkstra, buffer_snake

snake_app = app()


@snake_app.post("/start")
def start():
    return {
        "name": "Mr. Snek",
        "taunt": "I am Mr. Snek",
        "color": "#EF5350",
        "secondary_color": "#EF5350"
    }


@snake_app.post("/move")
def move():
    world = World(request.json)
    snake = world.you

    # Check if potential move will not result in self-collision.
    # If no, make move. Otherwise, default to left.
    potential_move = dijkstra(world, snake)
    snake_buf = buffer_snake(world, snake)

    if potential_move not in snake_buf:
        move = potential_move
    else:
        move = "left"

    return {
        "move": "left"
    }


snake_app.run(host='0.0.0.0')

from bottle import request, app
from game_objects import World

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
    return {
        "move": "left"
    }


snake_app.run()

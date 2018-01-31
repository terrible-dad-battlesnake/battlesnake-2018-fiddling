import bottle

app = bottle.app()


@app.post("/start")
def start():
    return {
        "name": "Mr. Snek",
        "taunt": "I am Mr. Snek",
        "color": "#EF5350",
        "secondary_color": "#EF5350"
    }


@app.post("/move")
def move():
    return {
        "move": "left"
    }


app.run()

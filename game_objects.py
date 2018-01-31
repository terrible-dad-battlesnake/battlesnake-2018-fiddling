"""
Classes representing objects in the game (parsed from JSON).
"""


class Snake:
    def __init__(self, snake_json):
        """Create new snake from a json payload."""
        self.id = snake_json["id"]
        self.name = snake_json["name"]
        self.health = int(snake_json["health"])
        self.length = int(snake_json["length"])
        self.body = set( [(point['x'], point['y']) for point in snake_json["body"]["data"]] )


class World:
    def __init__(self, request_json):
        """Create a new world from a /move request payload."""
        self.id = request_json["id"]
        self.width = request_json["width"]
        self.height = request_json["height"]
        self.turn = request_json["turn"]

        self.food = [(item["x"], item["y"]) for item in request_json["food"]["data"]]

        # snakes are stored in a dictionary indexed by snake id
        self.snakes = {}
        for snake_data in request_json["snakes"]["data"]:
            self.snakes.update({snake_data["id"]: Snake(snake_data)})

        # get your snake by reference (API copies your snake's data)
        self.you = self.snakes[request_json["you"]["id"]]

@deprecated
# Was originally used as a test app for trying out ne path finding ideas,
# replaced and superseded by pathfinding.py
#
#
# from bottle import request, app
# from game_objects import World, Snake
#
# snake_app = app()
#
#
# @snake_app.post('/start')
# def start():
#     return {
#         'color': 'blue',
#         'name': 'Mr. Windy Miney',
#         'taunt': 'Weavin\' my \'round town',
#         'head_type': 'pixel',
#         'tail_type': 'pixel',
#         'secondary_color': 'red'
#     }
#
#
# @snake_app.post('/move')
# def move():
#     world = World(request.json)
#     me = Snake(world.you)
#
#     body_buffer = []
#     buffer_val = 1
#
#     for body_piece in me:
#         current_x = body_piece[0]
#         current_y = body_piece[1]
#
#         if ():
#
#         body_buffer.append()
#
#     # Create buffer around the snake
#     if ()
#     return {
#         'move': request_move
#     }
#
# snake_app.run(host='0.0.0.0')
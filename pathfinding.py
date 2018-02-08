"""
Assorted pathfinding algorithms.
"""

import math
from heapq import heapify, heappop, heappush

import game_objects
from utils import neighbors_of


def get_next_move(snake_head, path):
    """Get the snake's next move in a given path.
    :param snake_head: Location of the snake's head (x, y).
    :param path: List of points creating a path from the snake's head.
                 [ (x, y), (x, y) ... ]
    :return Next move. One of ("right", "left", "up", "down").
    """
    assert type(path) == list, "Path must be a list."
    assert len(path) > 0, "Cannot get next move for an empty path."

    snakehead_x, snakehead_y = snake_head
    nextpoint_x, nextpoint_y = path[0]
    assert type(nextpoint_x) == int, "Invalid X coordinate."
    assert type(nextpoint_y) == int, "Invalid Y coordinate."
    assert type(snakehead_x) == int, "Invalid X coordinate."
    assert type(snakehead_y) == int, "Invalid Y coordinate."

    assert snake_head != path[0], "Next coordinate cannot be the same as snake head"

    if nextpoint_x > snakehead_x:
        return "left"
    elif nextpoint_x < snakehead_x:
        return "right"
    elif nextpoint_y < snakehead_y:
        return "up"
    elif nextpoint_y > snakehead_y:
        return "down"


def find_path_dijkstra(x, y, p):
    """Get the shortest path to a given point in a predecessor matrix.
    :param x: X coordinate of destination
    :param y: Y coordinate of destination
    :param p: Predecessor matrix to get path from.
    :return List of points in path, starting from snake head [(0, 0),(0, 1)...]
    """
    path = []
    point = p[y][x]
    while point != -1:
        path.append(point)
        point = p[point[1]][point[0]]

    path.reverse()
    return path[1:]


def dijkstra(world, snake):
    """Gets the distance "scores" and predecessor matrix from a given snake's
    head.
    :param world: World object to map for the snake.
    :param snake: Snake to calculate distances from.
    :return: d[] and p[] matrices for each point on the map.
        - None indicates the head of the snake (source node).
        - -1 indicates an inaccessible point.
    """
    d = [[math.inf for x in range(world.width)] for y in range(world.height)]
    p = [[None for x in range(world.width)] for y in range(world.height)]
    visited = [[False for x in range(world.width)] for y in range(world.height)]

    # d at the snake's head should be 0 (we're already there, so no cost!)
    snake_head = snake.body[0]  # Assumption cleared. We are correct.
    d[snake_head[1]][snake_head[0]] = 0

    pq = [(1, snake_head)]
    heapify(pq)
    while len(pq) > 0:
        next_vert = heappop(pq)[1]
        nv_x, nv_y = next_vert[0], next_vert[1]

        # ignore if we've already visited this vertex
        if visited[nv_y][nv_x]:
            continue

        # consider neighbors of this vertex
        for x, y in neighbors_of(nv_x, nv_y, world):
            if world.map[y][x] == game_objects.MAP_SNAKE:
                d[y][x] = -1
                p[y][x] = -1
            elif d[nv_y][nv_x] + 1 < d[y][x]:
                d[y][x] = d[nv_y][nv_x] + 1
                p[y][x] = (nv_x, nv_y)

                # re-add to pq if d[] was updated
                heappush(pq, (d[y][x], (x, y)))

        visited[nv_y][nv_x] = True

    return d, p


def buffer_snake(world, snake):
    """Creates buffer around snake to prevent self-collision.
    :param snake: List of snake's body pieces' positions
    :return: List of buffered positions
    """

    # Created because thought we might need this at a later date.
    snake_head = snake.body[0] # Assumption cleared. We are correct.

    body_buffer = []

    # Add buffer points for snake
    for body_item in snake.body:
        if (body_item[0] + 1) not in snake.body:
            body_buffer.append(tuple(body_item[0] + 1, body_item[1]))
        elif (body_item[0] - 1) not in snake.body:
            body_buffer.append(tuple(body_item[0] - 1, body_item[1]))
        elif (body_item[1] + 1) not in snake.body:
            body_buffer.append(tuple(body_item[0], body_item[1] + 1))
        elif (body_item[1] - 1) not in snake.body:
            body_buffer.append(tuple(body_item[0], body_item[1] - 1))
        else:
            continue

    # If body_buffer point is outside of grid, remove.
    for item in body_buffer:
        if item[0] > world.width or item[0] < 0:
            body_buffer.remove(item)
        if item[1] > world.height or item[1] < 0:
            body_buffer.remove(item)

    return body_buffer

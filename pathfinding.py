"""
Assorted pathfinding algorithms.
"""

import math
from heapq import heapify, heappop, heappush

import game_objects
from utils import neighbors_of


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
    snake_head = snake.body[0]  # Bad assumption! FIXME!!!!!
    d[snake_head[1]][snake_head[0]] = 0

    pq = [(1, snake_head)]
    heapify(pq)
    while len(pq) > 0:
        next_vert = heappop(pq)[1]
        nv_x, nv_y = next_vert[0], next_vert[1]

        # ignore if we've already visited this vertex
        if visited[nv_x][nv_y]:
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

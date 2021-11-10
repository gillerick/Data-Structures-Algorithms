import copy


city_ids = [1, 2, 3, 4]

n = len(city_ids)
all_sets = []
visited = {}
possible_routes = []


def tsp(cities, s):
    for x in range(1, n):
        visited[x + 1, ()] = cities[x][0]
        rem = [x for x in cities if x != s]
        if n == 2:
            return cost(s, rem, cities)

    cost(s, (2, 3, 4), cities)
    # cost(s, (x for x in cities if x != s), cities)

    print(f'Solution to TSP: [{s}, ', end='')
    solution = possible_routes.pop()
    print(solution[s][0], end=', ')
    for x in range(n - 2):
        for new_solution in possible_routes:
            if tuple(solution[s]) == new_solution[0]:
                solution = new_solution
                print(solution[s][0], end=', ')
                break
    print(f"{s}]")
    return

"""
N - subset of cities
s - 
"""
def cost(s, ids, N):
    global weights
    if (s, ids) in visited:
        # Already calculated Set g[%d, (%s)]=%d' % (k, str(a), g[k, a]))
        return visited[s, ids]

    values = []
    all_min = []
    for id in ids:
        set_a = copy.deepcopy(list(ids))
        set_a.remove(id)
        all_min.append([id, tuple(set_a)])
        result = cost(id, tuple(set_a), cities)
        x = s - 1
        y = id - 1
        weights = []
        weights.append(N[x][y])
        # print(result)
        values.append(N[x][y] + result)

    # get minimun value from set as optimal solution for
    visited[s, ids] = min(values)
    possible_routes.append(((s, ids), all_min[values.index(visited[s, ids])]))
    print(possible_routes)

    return visited[s, ids]


if __name__ == '__main__':
    cities = [
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0]
    ]

    tsp(cities, 1)

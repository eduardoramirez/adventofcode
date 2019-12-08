INPUT = open('input.txt', 'r').read().split()
orbits = list(map(lambda l: l.split(')'), INPUT))


def dfs(graph, root, cb):
    seen = set()
    def dfs_internal(node, depth):
        children = graph.get(node, [])
        if node in seen or len(children) == 0:
            return

        seen.add(node)

        for child in children:
            if child not in seen:
                cb(child, depth+1)
                dfs_internal(child, depth+1)

    dfs_internal(root, 0)


'''
 {node: [edges]}
'''
def build_graph():
    graph = {}
    for [src, dst] in orbits:
        if src in graph:
            edges = graph[src]
            edges.append(dst)
        else:
            graph[src] = [dst]

        if dst in graph:
            edges = graph[dst]
            edges.append(src)
        else:
            graph[dst] = [src]
    return graph


def part1():
    graph = build_graph()

    cnts = {'direct': 0, 'indirect': 0}
    def calculate_orbit_cnts(node, depth):
        cnts['direct'] += 1
        cnts['indirect'] += (depth - 1)

    dfs(graph, 'COM', calculate_orbit_cnts)

    return cnts['direct'] + cnts['indirect']


def part2():
    graph = build_graph()

    d = {'dist': 0}
    def calculate_dist(node, depth):
        if node == 'SAN':
            d['dist'] = depth

    dfs(graph, 'YOU', calculate_dist)

    # minus 2 in order to ignore the YOU & SAN steps
    return d['dist'] - 2


if __name__ == '__main__':
    print('Part 1: {}'.format(part1()))
    print('Part 2: {}'.format(part2()))

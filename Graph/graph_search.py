"""
图的遍历

DFS 和 BFS

     A
   /    \
  C      B
  \     / \
   \    D E
    \    /
       F


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
"""


def dfs_iter(graph, start):
    """ 迭代版本 DFS
    仅返回其中一条路径
    """
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(graph[vertex] - set(visited))
    return visited


def dfs_recur(graph, start, visited=None):
    """ 递归版本 DFS
    仅返回其中一条路径
    """
    if visited is None:
        visited = []
    visited.append(start)
    for next in graph[start]:
        if next not in visited:
            dfs_recur(graph, next, visited)
    return visited


def dfs_paths_iter(graph, start, end):
    """ 迭代 DFS 从出发点到终点的所有路径
    """
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == end:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def dfs_paths_recur(graph, start, end, path=None):
    """ 递归 DFS 从出发点到终点的所有路径
    """
    if path is None:
        path = [start]
    if start == end:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths_recur(graph, next, end, path + [next])


def bfs_iter(graph, start):
    """ 迭代版本 BFS
    仅返回其中一条路径
    """
    visited, queue = [], [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex] - set(visited))
    return visited


def bfs_paths_iter(graph, start, end):
    """ 迭代 BFS 从出发点到终点的所有路径
    第一个一定是最短的
    """
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == end:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


if __name__ == "__main__":
    graph = {
        'A': set(['B', 'C']),
        'B': set(['A', 'D', 'E']),
        'C': set(['A', 'F']),
        'D': set(['B']),
        'E': set(['B', 'F']),
        'F': set(['C', 'E'])
    }
    print(dfs_iter(graph, 'A'))
    print(dfs_recur(graph, 'A'))
    print(list(dfs_paths_iter(graph, 'A', 'F')))
    print(list(dfs_paths_recur(graph, 'A', 'F')))
    print(bfs_iter(graph, 'A'))
    print(list(bfs_paths_iter(graph, 'A', 'F')))

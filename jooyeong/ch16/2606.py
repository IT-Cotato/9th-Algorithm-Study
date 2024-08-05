N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


checked = [False] * (N+1)
checked[1] = True

stack = [1]

while stack:
    curr = stack.pop()

    for next in graph[curr]:
        if not checked[next]:
            checked[next] = True
            stack.append(next)

print(checked.count(True)-1)
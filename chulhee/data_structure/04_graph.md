# 04. 그래프

그래프는 원소 간 관계를 표현하는 자료구조 입니다.

그래프는 정점(vertex)과 객체를 연결하는 간선(edge)의 집합으로 구성됩니다.

종류나 특징에 대해선 생략하도록 하겠습니다.



## 그래프의 탐색

### 깊이 우선 탐색 - DFS (Depth First Search)

시작하는 정점에서 한 방향으로 갈 수 있는 가장 먼 경로까지 깊이 탐색하다가 더 이상 갈 곳이 없으면 
갈림길이 있던 간선까지 돌아와 다른 방향의 탐색을 계속해 나가는 방법입니다.

이를 구현하기 위해선, 스택을 사용하거나, 재귀함수를 사용합니다.

```python
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
  [],
  [2,3,8], 
  [1, 7],
  [1, 4, 5],
  [1, 7],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]
visited = [False] * 9

dfs(graph, 1, visited)

```



### 너비 우선 탐색 - BFS (Breadth First Search) 

시작 정점으로부터 인접한 정점을 모두 방문한 뒤 방문했던 점을 시작하여 인접 정점을 방문합니다.

가까운 곳에서부터 먼 곳 순서로 방문을 하게 됩니다.

queue 자료 구조를 사용해 구현할 수 잇습니다.

```python
from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
              
graph = [
  [],
  [2,3,8], 
  [1, 7],
  [1, 4, 5],
  [1, 7],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]
visited = [False] * 9

bfs(graph, 1, visited)
```





## 신장트리와 최소 비용 신장 트리

### 신장 트리

그래프의 관점에선, 트리는 사이클이 없는 단순 연결 그래프라고 할 수 있습니다.

신장트리는 n개의 정점에 대해서 n-1개의 간선으로 이뤄진 트리를 말합니다.



### 최소 비용 신장 트리

가중치의 합이 최소가 되는 신장트리를 최소 비용 신장 트리라고 합니다.

이를 만들기 위해 Kruskal 알고리즘, Prime 알고리즘을 주로 사용합니다.



### Kruskal 알고리즘

- 가중치가 높은 간선을 제거하면서 최소 비용 신장트리를 만드는 방법
- 가중치가 낮은 간선을 삽입하면서 만드는 방법

2가지 방법이 있는 알고리즘입니다.



동작은 다음과 같습니다.

1. 그래프의 간선을 가중치 오름차순으로 정렬
2. 정렬된 간선 리스트 중 사이클을 생성하지 않는 간선을 선택합니다.
3. 해당 간선을 트리에 삽입합니다.

간선 e 개를 n log n 의 시간 복잡도를 갖는 알고리즘으로 정렬한다면,
크루스칼 알고리즘 시간 복잡도는 O(e log e) 입니다.







## 레퍼런스

- https://gmlwjd9405.github.io/2018/08/30/algorithm-prim-mst.html
- 자바로 배우는 쉬운 자료구조, 한빛 아카데미


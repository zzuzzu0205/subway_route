#-*- coding: utf-8 -*-
from collections import deque
from subway_graph import *

# 코드를 추가하세요
def bfs(graph, start_node):
    """최단 경로용 bfs 함수"""
    queue = deque()  # 빈 큐 생성

    # 모든 노드를 방문하지 않은 노드로 표시, 모든 predecessor는 None으로 초기화
    for station_node in graph.values():
        station_node.visited = False
        station_node.predecessor = None

    # 시작점 노드를 방문 표시한 후 큐에 넣어준다
    start_node.visited = True
    queue.append(start_node)
    
    while queue:  # 큐에 노드가 있을 때까지
        current_station = queue.popleft()  # 큐의 가장 앞 데이터를 갖고 온다
        for neighbor in current_station.adjacent_stations:  # 인접한 노드를 돌면서
            if not neighbor.visited:  # 방문하지 않은 노드면
                neighbor.visited = True  # 방문 표시를 하고
                neighbor.predecessor = current_station  # 이 노드가 어디서 왔는지 표시 
                queue.append(neighbor)  # 큐에 넣는다


def back_track(destination_node):
    """최단 경로를 찾기 위한 back tracking 함수"""
    res_str = ""  # 리턴할 결과 문자열
    temp = destination_node  #  도착 노드에서 시작 노드까지 찾아가는 데 사용할 변수
# 시작 노드까지 갈 때까지
    while temp is not None:
        res_str = f"{temp.station_name} {res_str}"  # 결과 문자열에 역 이름을 더하고
        temp = temp.predecessor  # temp를 다음 노드로 바꿔준다

    return res_str



stations = create_station_graph("./new_stations.txt")  # stations.txt 파일로 그래프를 만든다

bfs(stations, stations["장림"])  # 지하철 그래프에서 을지로3가역을 시작 노드로 bfs 실행
print(back_track(stations["동의대"]))  # 을지로3가에서 강동구청역까지 최단 경로 출력

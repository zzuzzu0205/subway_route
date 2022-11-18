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
    global res_str
    res_str = ""  # 리턴할 결과 문자열
    temp = destination_node  #  도착 노드에서 시작 노드까지 찾아가는 데 사용할 변수

    # 시작 노드까지 갈 때까지
    i = 0 #시간계산을 위한 코드
    while temp is not None:
        
        res_str = f"{temp.station_name} {res_str}"  # 결과 문자열에 역 이름을 더하고
        temp = temp.predecessor  # temp를 다음 노드로 바꿔준다
        i = i +1 #역을 하나씩 지날 때 마다 i값이 커짐
    print("약",i*2,"분 소요예정(총",i,"개 역 경유)") #역 하나당 2분으로 계산
    
    center = int(i/2)+1
    global res_str1
    res_str1 = ""  # 리턴할 결과 문자열
    temp = destination_node
    for c in range(center):
        res_str1 = temp.station_name
        temp = temp.predecessor
    
    return res_str


    

global res_str
global res_str1
res_str1 = ''       #선언 및 초기화
res_str = ''

list = ["평강 대저 체육공원","체육공원 대저 평강","동구 대저 체육공원","체육공원 대저 동구","수정 덕천 숙등","숙등 덕천 수정","수정 덕천 구포","구포 덕천 수정","구포 덕천 구명","구명 덕천 구포","구명 덕천 숙등","숙등 덕천 구명","괘법르네시뗴 사상 감전","감전 사상 괘법르네시뗴","덕포 사상 괘법르네시뗴","괘법르네시뗴 사상 덕포","만덕 미남 동래","동래 미남 만덕","사직 미남 동래","동래 미남 사직","종합운동장 거제 교대","교대 거제 종합운동장","교대 거제 연산","연산 거제 교대","연산 거제 거제해맞이","거제해맞이 거제 연산","종합운동장 거제 거제해맞이","거제해맞이 거제 종합운동장","부전 서면 부암","부암 서면 부전","부전 서면 전포","전포 서면 부전","전포 서면 범내골","범내골 서면 전포","범내골 서면 부암","부암 서면 범내골","미남 동래 명륜","명륜 동래 미남","미남 동래 교대","교대 동래 미남","수안 동래 명륜","명륜 동래 수안","수안 동래 교대","교대 동래 수안","거제 교대 동래","동래 교대 거제","연산 교대 거제","거제 교대 연산","동래_동해선 교대 동래","동래 교대 동래_동해선","동래_동해선 교대 연산","연산 교대 동래_동해선","거제 연산 교대","교대 연산 거제","거제 연산 시청","시청 연산 거제","물만골 연산 교대","교대 연산 물만골","물만골 연산 시청","시청 연산 물만골","망미 수영 민락","민락 수영 망미","망미 수영 광안","광안 수영 망미","센텀시티 벡스코 센텀","센텀 벡스코 센텀시티","센텀시티 벡스코 신해운대","신해운대 벡스코 센텀시티","동백 벡스코 센텀","센텀 벡스코 동백","동백 벡스코 신해운대","신해운대 벡스코 동백"]
list_t = []    #환승역 리스트

stations = create_station_graph("./1.txt")  # stations.txt 파일로 그래프를 만든다

start = input("출발역을 입력하시오. -> ")
end = input("도착역을 입력하시오. -> ")

while (start not in stations) or (end not in stations):
    print("잘못된 값이 입력되었습니다. 다시 입력해 주세요.")
    start = input("출발역을 입력하시오. -> ")
    end = input("도착역을 입력하시오. -> ")

    
    
bfs(stations, stations[start])  # 지하철 그래프에서 start변수를 시작 노드로 bfs 실행
back_track(stations[end])

for i in range(len(list)):
    if list[i] in res_str and "서면"  in list[i]:     #환승경유를 지나고 환승역이 포함
        if "서면" not in list_t:
            list_t.append("서면")
    if list[i] in res_str and "대저"  in list[i]:
        if "대저" not in list_t:
            list_t.append("대저")
    if list[i] in res_str and "덕천"  in list[i]:
        if "덕천" not in list_t:
            list_t.append("덕천")
    if list[i] in res_str and "사상"  in list[i]:
        if "사상" not in list_t:
            list_t.append("사상")
    if list[i] in res_str and "미남"  in list[i]:
        if "미남" not in list_t:
            list_t.append("미남")
    if list[i] in res_str and "거제"  in list[i]:
        if "거제" not in list_t:
            list_t.append("거제")
    if list[i] in res_str and "동래"  in list[i]:
        if "동래" not in list_t:
            list_t.append("동래")
    if list[i] in res_str and "교대"  in list[i]:
        if "교대" not in list_t:
            list_t.append("교대")
    if list[i] in res_str and "연산"  in list[i]:
        if "연산" not in list_t:
            list_t.append("연산")
    if list[i] in res_str and "수영"  in list[i]:
        if "수영" not in list_t:
            list_t.append("수영")
    if list[i] in res_str and "벡스코"  in list[i]:
        if "벡스코" not in list_t:
            list_t.append("벡스코")

print("환승역 =>", list_t)

print("[",start,"] 부터 [",end,"] 까지의 최단경로는 ->",res_str,"<- 입니다.")  # start에서 end까지 최단 경로 출력

    
select = input("C = 중간지점 확인, R = 재시작, X = 종료 -> ")
while (select != 'X' and select != 'x'):
    if select == 'r' or select == 'R' :
        start = input("출발역을 입력하시오. -> ")
        end = input("도착역을 입력하시오. -> ")
    
        while (start not in stations) or (end not in stations):
            print("잘못된 값이 입력되었습니다. 다시 입력해 주세요.")
            start = input("출발역을 입력하시오. -> ")
            end = input("도착역을 입력하시오. -> ")

            
        list_t = []          #재실행 했을 때 다시 선언
        bfs(stations, stations[start])  # 지하철 그래프에서 을지로3가역을 시작 노드로 bfs 실행
        back_track(stations[end])

        for i in range(len(list)):
            if list[i] in res_str and "서면"  in list[i]:
                if "서면" not in list_t:
                    list_t.append("서면")
            if list[i] in res_str and "대저"  in list[i]:
                if "대저" not in list_t:
                    list_t.append("대저")
            if list[i] in res_str and "덕천"  in list[i]:
                if "덕천" not in list_t:
                    list_t.append("덕천")
            if list[i] in res_str and "사상"  in list[i]:
                if "사상" not in list_t:
                    list_t.append("사상")
            if list[i] in res_str and "미남"  in list[i]:
                if "미남" not in list_t:
                    list_t.append("미남")
            if list[i] in res_str and "거제"  in list[i]:
                if "거제" not in list_t:
                    list_t.append("거제")
            if list[i] in res_str and "동래"  in list[i]:
                if "동래" not in list_t:
                    list_t.append("동래")
            if list[i] in res_str and "교대"  in list[i]:
                if "교대" not in list_t:
                    list_t.append("교대")
            if list[i] in res_str and "연산"  in list[i]:
                if "연산" not in list_t:
                    list_t.append("연산")
            if list[i] in res_str and "수영"  in list[i]:
                if "수영" not in list_t:
                    list_t.append("수영")
            if list[i] in res_str and "벡스코"  in list[i]:
                if "벡스코" not in list_t:
                    list_t.append("벡스코")

        print("환승역 =>", list_t)
        print("[",start,"] 부터 [",end,"] 까지의 최단경로는 ->",res_str,"<- 입니다.")
    elif select == 'c' or select == 'C':
        print(start,"와",end,"사이의 중간지점은",res_str1 )
    else :
        print("입력이 잘못됨")
    
    select = input("C = 중간지점 확인, R = 재시작, X = 종료 -> ")
    
print("프로그램 종료!")

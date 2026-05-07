from graphviz import Digraph

# 마인드맵 생성
mind_map = Digraph("MindMap", format="png")
mind_map.attr(rankdir="LR")
mind_map.attr("node", shape="box", style="filled", color="lightblue")

mind_map.node("System", "영화관 예매 시스템")

main_functions = {
    "영화 정보 관리": ["제목", "장르", "상영시간", "등급", "포스터"],
    "상영 시간표 관리": ["날짜", "시간", "상영관", "연결된 영화"],
    "좌석 관리": ["좌석 번호", "예매 상태", "상영관 연동"],
    "예매 기능": ["고객 선택", "좌석 선택", "결제"],
    "결제 관리": ["카드", "포인트", "쿠폰"],
    "고객 정보 관리": ["고객 ID", "이름", "예매 내역"],
    "매출/통계 분석": ["시간대별 통계", "영화별 인기", "지점별 수익"]
}

for function, sub_items in main_functions.items():
    mind_map.node(function)
    mind_map.edge("System", function)
    for sub in sub_items:
        node_id = f"{function}_{sub}"
        mind_map.node(node_id, sub)
        mind_map.edge(function, node_id)

mind_map.render("movie_booking_mindmap", cleanup=True)

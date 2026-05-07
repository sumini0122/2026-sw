# ---- ER 다이어그램 생성 코드 ----
# 터미널에서 먼저 설치해야 함:
# pip install graphviz
# brew install graphviz   # (Mac 전용: 시스템 그래프 도구 설치)


import os
os.environ["PATH"] += os.pathsep + "/opt/homebrew/bin"

from graphviz import Digraph  # ← 요거 꼭 있어야 해!!

# 다이어그램 객체 생성
dot = Digraph('ERD', filename='movie_reservation_system.gv', format='png')
dot.attr(rankdir='LR', fontname='NanumGothic')

node_attr = {'shape': 'plaintext', 'fontname': 'NanumGothic'}

# --- 엔터티 정의 함수 ---
def entity(name, attributes):
    label = f'''<
    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
    <TR><TD BGCOLOR="#efefef"><B>{name}</B></TD></TR>
    {''.join(f'<TR><TD ALIGN="LEFT">{attr}</TD></TR>' for attr in attributes)}
    </TABLE>>'''
    dot.node(name, label=label, **node_attr)

# --- 엔터티들 ---
entity("영화(Movie)", [
    "영화ID (PK)", "제목", "장르", "러닝타임",
    "관람등급", "포스터이미지", "감독", "출연진"
])

entity("상영(Screening)", [
    "상영ID (PK)", "영화ID (FK)", "상영관ID (FK)", "상영날짜", "상영시간"
])

entity("상영관(Theater)", [
    "상영관ID (PK)", "이름", "위치", "총좌석수", "층수"
])

entity("좌석(Seat)", [
    "좌석ID (PK)", "상영관ID (FK)", "행번호", "열번호", "상태(예매가능/예매됨)"
])

entity("고객(Customer)", [
    "고객ID (PK)", "이름", "전화번호", "생년월일", "이메일", "멤버십등급", "포인트"
])

entity("예매(Reservation)", [
    "예매ID (PK)", "고객ID (FK)", "상영ID (FK)", "좌석ID (FK)", "결제ID (FK)",
    "예매일자", "상태(완료/취소)"
])

entity("결제(Payment)", [
    "결제ID (PK)", "결제방법", "결제금액", "결제일자", "쿠폰적용여부", "포인트사용량"
])

entity("박스오피스(BoxOffice)", [
    "통계ID (PK)", "영화ID (FK)", "일매출", "주매출", "월매출", "관객수", "인기지수"
])

# --- 관계 정의 ---
dot.edge("영화(Movie)", "상영(Screening)", label="1:N")
dot.edge("상영(Screening)", "예매(Reservation)", label="1:N")
dot.edge("상영(Screening)", "상영관(Theater)", label="N:1")
dot.edge("상영관(Theater)", "좌석(Seat)", label="1:N")
dot.edge("고객(Customer)", "예매(Reservation)", label="1:N")
dot.edge("예매(Reservation)", "결제(Payment)", label="1:1")
dot.edge("영화(Movie)", "박스오피스(BoxOffice)", label="1:1")
dot.edge("좌석(Seat)", "예매(Reservation)", label="1:N")

# --- 결과 출력 ---
output_path = dot.render(cleanup=True)
print("ER 다이어그램 생성 완료:", output_path)

import streamlit as st

# 1. 앱 제목 설정
st.title("📚 도서 대출 시스템")

# 2. 도서 목록 및 세션 상태 초기화
books = ("헤리포터", "어린왕자", "데미안")

if "borrowed" not in st.session_state:
    st.session_state.borrowed = []
if "terminated" not in st.session_state:
    st.session_state.terminated = False  # 종료 상태를 저장하는 변수

# 3. 사이드바 현재 대출 현황 표시
st.sidebar.header("📊 현재 대출 현황")
st.sidebar.write(f"대출된 도서 수: {len(st.session_state.borrowed)} / 3")
for book in st.session_state.borrowed:
    st.sidebar.write(f"- {book}")

# 초기화 버튼
if st.sidebar.button("처음부터 다시 하기"):
    st.session_state.borrowed = []
    st.session_state.terminated = False
    st.rerun()

# 4. 메인 로직 처리
# 이미 '종료'를 누르거나 3권을 모두 빌린 경우
if st.session_state.terminated or len(st.session_state.borrowed) >= 3:
    if st.session_state.terminated:
        st.warning("🔒 사용자가 대출을 종료했습니다.")
    else:
        st.info("📢 최대 대출 권수(3권)를 달성하여 대출이 자동 종료되었습니다.")
        
    # 최종 대출 결과 출력
    st.divider()
    st.subheader("📋 최종 대출 목록")
    if st.session_state.borrowed:
        st.dataframe(st.session_state.borrowed, column_config={"value": "도서명"}, use_container_width=True)
    else:
        st.write("대출한 책이 없습니다.")

# 대출 진행 중인 경우
else:
    st.subheader("대출하실 책을 선택해주세요.")
    
    # 셀렉트박스로 책 선택 (1, 2, 3번)
    choice = st.selectbox(
        "도서를 선택하세요:",
        options=[1, 2, 3],
        format_func=lambda x: f"{x}. {books[x-1]}"
    )
    
    # 버튼들을 가로로 배치 (대출 신청 / 대출 종료)
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🟢 대출 신청", use_container_width=True):
            selected_book = books[choice - 1]
            if selected_book in st.session_state.borrowed:
                st.error(f"⚠️ '{selected_book}'은(는) 이미 대출하신 책입니다.")
            else:
                st.session_state.borrowed.append(selected_book)
                st.success(f"🎉 '{selected_book}' 대출 완료!")
                st.rerun()
                
    with col2:
        # 기존 코드의 '0: 종료' 역할을 하는 버튼
        if st.button("🔴 대출 종료 (0번 입력)", use_container_width=True):
            st.session_state.terminated = True
            st.rerun()
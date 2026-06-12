import streamlit as st

# 1. 앱 제목 설정
st.title("📚 도서 대출 시스템")

# 2. 도서 목록 및 세션 상태(데이터 유지) 초기화
books = ("헤리포터", "어린왕자", "데미안")

if "borrowed" not in st.session_state:
    st.session_state.borrowed = []

# 3. 사이드바 또는 메인 화면에 현재 대출 현황 표시
st.sidebar.header("📊 현재 대출 현황")
st.sidebar.write(f"대출된 도서 수: {len(st.session_state.borrowed)} / 3")

if st.session_state.borrowed:
    for book in st.session_state.borrowed:
        st.sidebar.write(f"- {book}")
else:
    st.sidebar.write("대출한 책이 없습니다.")

# 초기화 버튼 (테스트 편의용)
if st.sidebar.button("대출 기록 초기화"):
    st.session_state.borrowed = []
    st.rerun()

# 4. 메인 로직 (최대 3권까지 대출 가능)
if len(st.session_state.borrowed) < 3:
    st.subheader("대출하실 책을 선택해주세요.")
    
    # selectbox를 사용하여 직관적인 선택 제공 (기존의 1, 2, 3 선택 항목 반영)
    choice = st.selectbox(
        "도서를 선택하세요:",
        options=[1, 2, 3],
        format_func=lambda x: f"{x}. {books[x-1]}"
    )
    
    # 대출하기 버튼
    if st.button("대출 신청"):
        selected_book = books[choice - 1]
        
        # 중복 대출 확인 및 처리
        if selected_book in st.session_state.borrowed:
            st.warning(f"⚠️ '{selected_book}'은(는) 이미 대출하신 책입니다.")
        else:
            st.session_state.borrowed.append(selected_book)
            st.success(f"🎉 '{selected_book}' 대출 완료!")
            st.rerun()  # 화면을 갱신하여 사이드바와 대출 가능 상태를 업데이트

else:
    st.info("📢 최대 대출 권수(3권)를 초과하여 더 이상 대출할 수 없습니다.")

# 5. 최종 대출 완료 결과 출력
st.divider()
st.subheader("📋 최종 대출 목록")
if st.session_state.borrowed:
    st.dataframe(st.session_state.borrowed, column_config={"value": "도서명"}, use_container_width=True)
else:
    st.write("대출 목록이 비어 있습니다.")
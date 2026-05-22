import os
import streamlit as st
import streamlit.components.v1 as components

# 1. Streamlit 페이지 기본 설정 (넓은 화면, 탭 제목 설정)
st.set_page_config(
    page_title="앱 인벤터 프로젝트 기획서",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Streamlit 기본 여백 및 UI 숨기기 (더 깔끔한 독립적인 웹앱 화면을 위해)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;} /* 우측 상단 햄버거 메뉴 숨김 */
            footer {visibility: hidden;}    /* 하단 Made with Streamlit 숨김 */
            header {visibility: hidden;}    /* 상단 여백 숨김 */
            .block-container {
                padding-top: 0rem;
                padding-bottom: 0rem;
                padding-left: 0rem;
                padding-right: 0rem;
                max-width: 100%;
            }
            iframe {
                border: none; /* iframe 테두리 제거 */
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 3. HTML 파일 경로 지정
# 현재 app.py가 있는 폴더의 절대 경로를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))
# htmls 폴더 안의 index.html 경로를 합칩니다.
html_file_path = os.path.join(current_dir, "htmls", "index.html")

# 4. HTML 파일 읽어서 화면에 띄우기
try:
    # 한글 깨짐 방지를 위해 encoding="utf-8" 적용
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # components.html을 사용하여 HTML 렌더링
    # height를 2500으로 넉넉하게 주어 페이지 내에서 스크롤이 원활하게 작동하도록 합니다.
    components.html(html_content, height=2500, scrolling=True)
    
except FileNotFoundError:
    # 파일이 제 위치에 없을 경우 안내 메시지 출력
    st.error(f"🚨 HTML 파일을 찾을 수 없습니다: {html_file_path}")
    st.info("👉 현재 파이썬 파일(app.py)과 같은 위치에 'htmls' 폴더를 만들고, 그 안에 선생님이 완성하신 'index.html' 파일을 넣어주세요.")

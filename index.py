import streamlit as st
import time

print("程式起點")
st.title("這是我的第一個streamlit專案")
st.header("這是我的次標題")
st.subheader("這是我的次次標題")
st.write("這是段落1")
st.write("這是段落2")
st.write("這是段落3")
st.markdown('''
---
# H1
---
## H2
---
### H3
---
#### H4
---
##### H5
---
###### H6
---
''')

with st.sidebar:
    st.sidebar.markdown('''
    ### 這是sidebar
    ---

    這是**段落一**

    這是*段落二*

    ''')

    btn1 = st.button("按鈕1")
    if btn1:
        print("btn1被按了")

def downloadData():
    print("下載資料")

# while True:
#     time.sleep(5)
#     downloadData()
#     st.experimental_rerun()


print("程式結束點")
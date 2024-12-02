import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Customize page title
st.title("資料來源")

st.markdown(
    """
    本網頁資料源自臺中市政府資料開放平台
    """
)

st.header("資料內容")

markdown = """
資料欄位包含：編號、縣市別代碼、區域、行政區域代碼、登山步道名稱、經度(步道大約位置)、緯度(步道大約位置)、步道分類、步道等級、附屬設施、管理維護單位、長度公里

"""

st.markdown(markdown)

import streamlit as st
import pandas as pd

data = pd.read_csv("https://github.com/b6baa/20241127ex2/raw/refs/heads/main/%E8%87%BA%E4%B8%AD%E5%B8%82%E5%81%A5%E8%A1%8C%E6%AD%A5%E9%81%93%E8%B3%87%E6%96%991131024(%E4%BF%AE%E5%A2%9E%E5%8A%A0%E7%B6%93%E7%B7%AF%E5%BA%A6).csv.csv")

st.subheader("步道資訊")
df = pd.DataFrame(data)
st.dataframe(df) 

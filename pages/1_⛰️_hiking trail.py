import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Marker Cluster")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map(center=[24.14734503954353, 120.67316364818225], zoom=10)
        m.add_basemap("TERRAIN")
        data = pd.read_csv("https://github.com/b6baa/20241127ex2/raw/refs/heads/main/%E8%87%BA%E4%B8%AD%E5%B8%82%E5%81%A5%E8%A1%8C%E6%AD%A5%E9%81%93%E8%B3%87%E6%96%991131024(%E4%BF%AE%E5%A2%9E%E5%8A%A0%E7%B6%93%E7%B7%AF%E5%BA%A6).csv.csv")
        
        m.add_points_from_xy(
            data,
            x="經度(步道大約位置)",
            y="緯度(步道大約位置)",
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=700)

st.subheader("步道資訊")
df = pd.DataFrame(data)
st.dataframe(df)  # Same as st.write(df)
